require('dotenv').config();
const express = require('express');
const { Configuration, PlaidApi, PlaidEnvironments } = require('plaid');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(express.json());

// Plaid client setup
const configuration = new Configuration({
  basePath: PlaidEnvironments[process.env.PLAID_ENV || 'sandbox'],
  baseOptions: {
    headers: {
      'PLAID-CLIENT-ID': process.env.PLAID_CLIENT_ID,
      'PLAID-SECRET': process.env.PLAID_SECRET,
    },
  },
});

const plaidClient = new PlaidApi(configuration);

// Store access tokens (in production, use a database)
const tokensFile = path.join(__dirname, 'tokens.json');
let accessTokens = {};

if (fs.existsSync(tokensFile)) {
  accessTokens = JSON.parse(fs.readFileSync(tokensFile, 'utf8'));
}

function saveTokens() {
  fs.writeFileSync(tokensFile, JSON.stringify(accessTokens, null, 2));
}

// Serve static files
app.use(express.static('public'));

// Create Link token (step 1 of Plaid Link flow)
app.post('/api/create_link_token', async (req, res) => {
  try {
    const response = await plaidClient.linkTokenCreate({
      user: { client_user_id: 'tax-user-1' },
      client_name: 'Tax Document Collector',
      products: ['transactions'],
      country_codes: ['US'],
      language: 'en',
    });
    res.json(response.data);
  } catch (error) {
    console.error('Error creating link token:', error.response?.data || error);
    res.status(500).json({ error: error.message });
  }
});

// Exchange public token for access token (step 2)
app.post('/api/exchange_token', async (req, res) => {
  try {
    const { public_token, institution } = req.body;
    const response = await plaidClient.itemPublicTokenExchange({
      public_token,
    });

    const accessToken = response.data.access_token;
    const itemId = response.data.item_id;

    // Store the token
    accessTokens[itemId] = {
      access_token: accessToken,
      institution: institution,
      connected_at: new Date().toISOString(),
    };
    saveTokens();

    console.log(`Connected to ${institution?.name || 'bank'}!`);
    res.json({ success: true, item_id: itemId });
  } catch (error) {
    console.error('Error exchanging token:', error.response?.data || error);
    res.status(500).json({ error: error.message });
  }
});

// Get all transactions for a date range
app.get('/api/transactions', async (req, res) => {
  try {
    const startDate = req.query.start || '2023-01-01';
    const endDate = req.query.end || '2024-12-31';

    let allTransactions = [];

    for (const [itemId, tokenData] of Object.entries(accessTokens)) {
      console.log(`Fetching transactions from ${tokenData.institution?.name || itemId}...`);

      let hasMore = true;
      let cursor = undefined;

      // Use sync endpoint for complete transaction history
      while (hasMore) {
        const response = await plaidClient.transactionsSync({
          access_token: tokenData.access_token,
          cursor: cursor,
        });

        const data = response.data;
        allTransactions = allTransactions.concat(
          data.added.map(t => ({
            ...t,
            institution: tokenData.institution?.name || 'Unknown',
          }))
        );

        hasMore = data.has_more;
        cursor = data.next_cursor;
      }
    }

    // Filter by date range
    allTransactions = allTransactions.filter(t => {
      return t.date >= startDate && t.date <= endDate;
    });

    // Sort by date
    allTransactions.sort((a, b) => new Date(a.date) - new Date(b.date));

    res.json({
      count: allTransactions.length,
      transactions: allTransactions,
    });
  } catch (error) {
    console.error('Error fetching transactions:', error.response?.data || error);
    res.status(500).json({ error: error.message });
  }
});

// Export transactions to CSV
app.get('/api/export', async (req, res) => {
  try {
    const startDate = req.query.start || '2023-01-01';
    const endDate = req.query.end || '2024-12-31';
    const year = req.query.year;

    // If year specified, override dates
    const actualStart = year ? `${year}-01-01` : startDate;
    const actualEnd = year ? `${year}-12-31` : endDate;

    let allTransactions = [];

    for (const [itemId, tokenData] of Object.entries(accessTokens)) {
      let hasMore = true;
      let cursor = undefined;

      while (hasMore) {
        const response = await plaidClient.transactionsSync({
          access_token: tokenData.access_token,
          cursor: cursor,
        });

        const data = response.data;
        allTransactions = allTransactions.concat(
          data.added.map(t => ({
            ...t,
            institution: tokenData.institution?.name || 'Unknown',
          }))
        );

        hasMore = data.has_more;
        cursor = data.next_cursor;
      }
    }

    // Filter and sort
    allTransactions = allTransactions
      .filter(t => t.date >= actualStart && t.date <= actualEnd)
      .sort((a, b) => new Date(a.date) - new Date(b.date));

    // Create CSV
    const headers = ['Date', 'Description', 'Amount', 'Category', 'Account', 'Institution', 'Type'];
    const rows = allTransactions.map(t => [
      t.date,
      `"${(t.name || '').replace(/"/g, '""')}"`,
      t.amount,
      `"${(t.category || []).join(', ')}"`,
      t.account_id?.slice(-4) || '',
      t.institution,
      t.amount > 0 ? 'Expense' : 'Income',
    ]);

    const csv = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');

    // Save to file
    const filename = `transactions_${actualStart}_to_${actualEnd}.csv`;
    const filepath = path.join(__dirname, '..', '..', 'exports', filename);

    // Ensure exports directory exists
    const exportsDir = path.join(__dirname, '..', '..', 'exports');
    if (!fs.existsSync(exportsDir)) {
      fs.mkdirSync(exportsDir, { recursive: true });
    }

    fs.writeFileSync(filepath, csv);

    res.json({
      success: true,
      count: allTransactions.length,
      file: filepath,
      message: `Exported ${allTransactions.length} transactions to ${filename}`,
    });
  } catch (error) {
    console.error('Error exporting:', error.response?.data || error);
    res.status(500).json({ error: error.message });
  }
});

// List connected accounts
app.get('/api/accounts', async (req, res) => {
  try {
    const accounts = [];

    for (const [itemId, tokenData] of Object.entries(accessTokens)) {
      try {
        const response = await plaidClient.accountsGet({
          access_token: tokenData.access_token,
        });

        accounts.push({
          institution: tokenData.institution?.name || 'Unknown',
          item_id: itemId,
          accounts: response.data.accounts.map(a => ({
            name: a.name,
            type: a.type,
            subtype: a.subtype,
            mask: a.mask,
            balance: a.balances.current,
          })),
        });
      } catch (e) {
        accounts.push({
          institution: tokenData.institution?.name || 'Unknown',
          item_id: itemId,
          error: 'Could not fetch accounts',
        });
      }
    }

    res.json({ accounts });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

const PORT = process.env.PORT || 3456;
app.listen(PORT, () => {
  console.log(`
====================================
  Tax Bank Connector Running!
====================================

Open http://localhost:${PORT} in your browser to connect your banks.

Connected banks: ${Object.keys(accessTokens).length}

API Endpoints:
- GET  /api/accounts     - List connected accounts
- GET  /api/transactions - Get all transactions
- GET  /api/export?year=2023 - Export to CSV

====================================
  `);
});
