# Simple Crypto Tracker

Simple Crypto Tracker is a CLI tool to keep track of your crypto portfolio and your defi positions.

## Environment

For the tool to work you will need to create a `.env` file with inside your etherscan API key. Example:
```
ETHERSCAN_API_KEY=<key content>
```

## Components

- Transaction ledger, contains your transaction history. You give in input (platform, tx_hash) or directly the link of the tx explorer and the transaction details are saved.
- Plotter, plots values of your portfolio overtime and other plots.
- Data analyzer, computes values regarding transaction history (e.g. amount spent in fees), transaction frequency, etc
- DeFi module, provides data about your defi positions.
