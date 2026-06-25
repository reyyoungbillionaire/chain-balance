<div align="center">
  <h1>⛓️ chain-balance</h1>
  <p><b>Multi-chain wallet balance checker</b><br/>
  <i>Ethereum · BSC · Polygon · Avalanche · Arbitrum · Optimism · Solana</i></p>
  <p>
    <a href="https://github.com/reyhansaeed/chain-balance/stargazers"><img src="https://img.shields.io/github/stars/reyhansaeed/chain-balance?style=flat&color=00FFAA" /></a>
    <a href="https://github.com/reyhansaeed/chain-balance/issues"><img src="https://img.shields.io/github/issues/reyhansaeed/chain-balance?style=flat&color=00FFAA" /></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/python-3.8%2B-00FFAA?style=flat&logo=python" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-00FFAA?style=flat" /></a>
  </p>
</div>

---

**chain-balance** is a lightweight, zero-dependency tool that reads native token balances across major blockchain networks — right from your terminal. No API keys, no registrations, no third-party trackers. Just you, Python, and public RPC nodes.

---

## ✨ Features

| Feature | Detail |
|---------|--------|
| 🌐 **7 Networks** | Ethereum, BSC, Polygon, Avalanche, Arbitrum, Optimism, Solana |
| 🔌 **Zero Dependencies** | Pure Python stdlib — no pip install required |
| 🔑 **No API Keys** | Uses public RPC endpoints out of the box |
| 🧠 **Auto-Detect** | Paste any address — EVM or Solana — we figure out the chain |
| 🎯 **Single or Multi** | Check one chain or all supported networks at once |
| ⚡ **Fast** | Parallel EVM checks, sub-second response per chain |
| 🔧 **Customizable** | Bring your own RPC endpoints via `.env` |

## 📦 Installation

```bash
git clone https://github.com/reyhansaeed/chain-balance.git
cd chain-balance
```

No pip install. No requirements. Pure Python.

## 🚀 Usage

### Check any address across all chains

```bash
python run.py 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18
```

### Check a single chain

```bash
python run.py 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18 bsc
python run.py 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18 solana
```

### Check Solana address

```bash
python run.py 7EcDhSYGxXyscszYEp35KHN8vvw3svAuLKTzXwCFLtV
```

## 📋 Example Output

```
==================================================
  Checking 0x742d35Cc...f2bD18 across all EVM chains
==================================================
  ✓ Ethereum             0.006052 ETH
  ✓ BSC                  0.000628 BNB
  ✓ Polygon              0.000000 MATIC
  ✓ Avalanche C-Chain    0.000003 AVAX
  ✓ Arbitrum One         0.000185 ETH
  ✓ Optimism             0.000000 ETH
  ✓ Solana               2.2496 SOL
```

## 🌍 Supported Networks

| Chain | Token | RPC Source |
|-------|-------|------------|
| Ethereum | ETH | publicnode.com |
| BSC | BNB | binance.org |
| Polygon | MATIC | publicnode.com |
| Avalanche | AVAX | avax.network |
| Arbitrum | ETH | publicnode.com |
| Optimism | ETH | optimism.io |
| Solana | SOL | solana.com |

All public and free. For higher rate limits, use your own RPC via `.env`.

## 🔧 Configuration

Copy `.env.example` to `.env` and set custom RPC endpoints:

```env
ETHEREUM_RPC=https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY
BSC_RPC=https://bsc-dataseed1.binance.org
SOLANA_RPC=https://api.mainnet-beta.solana.com
```

## 💡 Use Cases

- **Airdrop hunters** — Quick wallet checks across chains before claiming
- **Portfolio tracking** — See all wallets without 10 explorer tabs
- **Bridge monitoring** — Verify funds arrived on destination chain
- **Dust collectors** — Find forgotten tokens across old wallets
- **Trading bots** — Lightweight pre-trade balance check

## 🤝 Contributing

1. Fork it
2. Create branch: `git checkout -b feat/arbitrum-nova`
3. Commit: `git commit -m 'add arbitrum nova support'`
4. Push: `git push origin feat/arbitrum-nova`
5. Open a Pull Request

## ⚠️ Disclaimer

This tool reads public blockchain data. It does not store, transmit, or request private keys. Use at your own risk.

## 📄 License

MIT © 2026 — [reyhansaeed](https://github.com/reyhansaeed)

---

<div align="center">
  <sub>⚡ Built because checking 5 explorers for 1 wallet is dumb.</sub>
  <br/>
  <img src="https://komarev.com/ghpvc/?username=reyhansaeed&style=flat-square&color=00FFAA&label=repo+views" />
</div>