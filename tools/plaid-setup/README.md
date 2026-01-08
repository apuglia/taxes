# Tax Bank Connector - Plaid Integration

Automatically pull bank transactions for tax preparation.

## Quick Setup (5 minutes)

### 1. Get Plaid API Keys (Free)

1. Go to https://dashboard.plaid.com/signup
2. Create an account (no credit card needed)
3. Go to **Developers > Keys**
4. Copy your **Client ID** and **Sandbox Secret**

### 2. Configure

```bash
cd taxes/tools/plaid-setup
copy .env.example .env
```

Edit `.env` and paste your keys:
```
PLAID_CLIENT_ID=your_client_id_here
PLAID_SECRET=your_sandbox_secret_here
PLAID_ENV=sandbox
```

### 3. Install & Run

```bash
npm install
npm start
```

### 4. Connect Banks

Open http://localhost:3000 in your browser and click "Connect a Bank Account"

---

## Testing vs Real Banks

### Sandbox Mode (Default)
- Uses fake test data
- Test credentials: `user_good` / `pass_good`
- Good for testing the setup works

### Development Mode (Real Banks)
1. In Plaid dashboard, go to **Account > Billing**
2. Add payment method (they give 100 free connections)
3. Change `.env` to:
```
PLAID_SECRET=your_development_secret
PLAID_ENV=development
```
4. Restart the server
5. Now you can connect real banks!

---

## How It Works

1. **Connect**: Click "Connect a Bank Account" → Log in through Plaid's secure window
2. **Sync**: Plaid downloads all your transaction history
3. **Export**: Click "Export 2023" or "Export 2024" to generate CSV files
4. **Analyze**: Claude will process the CSV files and calculate your taxes

---

## Files Created

```
taxes/
├── tools/plaid-setup/
│   ├── tokens.json      # Stores bank connections (keep private!)
│   └── ...
└── exports/
    ├── transactions_2023-01-01_to_2023-12-31.csv
    └── transactions_2024-01-01_to_2024-12-31.csv
```

---

## Troubleshooting

**"Invalid credentials" error**
- Make sure you copied the right secret (Sandbox vs Development)
- Check that PLAID_ENV matches the secret type

**No transactions showing**
- In Sandbox mode, it takes a moment to generate fake data
- Click "Refresh Accounts" and try again

**Can't connect real bank**
- You need Development mode (not Sandbox)
- Some banks require additional verification in Plaid dashboard

---

## Security Notes

- Plaid is used by Venmo, Robinhood, Coinbase, and thousands of other apps
- Your bank credentials are never stored by this tool
- Plaid uses bank-level encryption
- The `tokens.json` file contains access tokens - don't share it!
