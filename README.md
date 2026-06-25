# ⛓️ chain-balance

**Multi-chain wallet balance checker — from your terminal.**

Check native token balances across Ethereum, BSC, Polygon, Avalanche, Arbitrum, Optimism, and Solana with a single command. No API keys required. No third-party services. Just Python and public RPC nodes.

![demo](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Feedvibes%2Fchain-balance%2Fcommits%3Fper_page%3D1&query=%24%5B0%5D.commit.author.date&label=last%20commit&color=2ea043)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/eedvibes/chain-balance/pulls)

---

## why

Every crypto wallet checker out there either wants your seed phrase, charges for API access, or is a web app that tracks your IP. This one runs locally, needs zero config, and tells you exactly what you own — nothing more.

## features

- **6+ EVM chains** — Ethereum, BSC, Polygon, Avalanche, Arbitrum, Optimism
- **Solana support** — base58 address detection
- **Zero API keys** — uses public RPC nodes
- **Auto-detect** — paste any address, we figure out the chain
- **Batch check** — comma-separated addresses (coming soon)
- **Clean output** — no noise, just balances

## quick start

```bash
# No install needed — just run
git clone https://github.com/eedvibes/chain-balance.git
cd chain-balance
python run.py 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18
```

### check one chain

```bash
python run.py 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18 ethereum
```

### check solana

```bash
python run.py 7EcDhSYGxXyscszYEp35KHN8vvw3svAuLKTzXwCFLtV
```

## supported networks

| Chain       | Native Token | How it works                     |
|-------------|-------------|----------------------------------|
| Ethereum    | ETH         | eth_getBalance via public RPC    |
| BSC         | BNB         | eth_getBalance via Binance seed  |
| Polygon     | MATIC       | eth_getBalance                   |
| Avalanche   | AVAX        | eth_getBalance                   |
| Arbitrum    | ETH         | eth_getBalance                   |
| Optimism    | ETH         | eth_getBalance                   |
| Solana      | SOL         | getBalance via public RPC        |

All RPC endpoints are public and free. Rate limits apply — if you hit them, switch to your own RPC via environment variable.

## .env support

Optionally set custom RPC endpoints in `.env`:

```env
ETHEREUM_RPC=https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY
BSC_RPC=https://bsc-dataseed1.binance.org
```

Copy `.env.example` to `.env` to get started.

## use cases

- Check your wallets before bridging
- Verify airdrop eligibility across chains
- Monitor dust collectors
- Quick portfolio snapshot without logging into 5 explorers

## contributing

PRs welcome. If you want to add a chain, open an issue first so we don't step on each other.

1. Fork the repo
2. Create your feature branch (`git checkout -b feat/arbitrum-nova`)
3. Commit your changes (`git commit -m 'add arbitrum nova support'`)
4. Push to the branch (`git push origin feat/arbitrum-nova`)
5. Open a Pull Request

## disclaimer

This tool reads public blockchain data. It does not store, transmit, or request private keys. Your wallet address is sent to public RPC nodes — same as using any block explorer. Use at your own risk.

## license

MIT © 2026 [eedvibes](https://github.com/eedvibes)

---

<p align="center">
  <sub>Built because checking 5 explorers for 1 wallet is dumb.</sub>
</p>
