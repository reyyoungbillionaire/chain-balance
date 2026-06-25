"""
EVM-compatible chain balance checker.
Supports Ethereum, BSC, Polygon, Avalanche, Arbitrum, Optimism.
"""

import json
from urllib.request import Request, urlopen
from urllib.error import URLError

# Public RPC endpoints (no API key needed for basic balance checks)
RPC_ENDPOINTS = {
    "ethereum":  "https://ethereum-rpc.publicnode.com",
    "bsc":       "https://bsc-dataseed1.binance.org",
    "polygon":   "https://polygon-bor-rpc.publicnode.com",
    "avalanche": "https://api.avax.network/ext/bc/C/rpc",
    "arbitrum":  "https://arbitrum-rpc.publicnode.com",
    "optimism":  "https://mainnet.optimism.io",
}

CHAIN_NAMES = {
    "ethereum":  "Ethereum",
    "bsc":       "BSC",
    "polygon":   "Polygon",
    "avalanche": "Avalanche C-Chain",
    "arbitrum":  "Arbitrum One",
    "optimism":  "Optimism",
}

NATIVE_CURRENCIES = {
    "ethereum":  "ETH",
    "bsc":       "BNB",
    "polygon":   "MATIC",
    "avalanche": "AVAX",
    "arbitrum":  "ETH",
    "optimism":  "ETH",
}

NATIVE_DECIMALS = 18


def _rpc_call(rpc_url: str, method: str, params: list) -> dict:
    """Make a JSON-RPC call to the given endpoint."""
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }).encode()

    req = Request(rpc_url, data=payload, headers={
        "Content-Type": "application/json",
        "User-Agent": "chain-balance/1.0",
    })

    try:
        resp = urlopen(req, timeout=15)
        return json.loads(resp.read())
    except URLError as e:
        return {"error": str(e.reason)}
    except json.JSONDecodeError:
        return {"error": "invalid JSON response"}
    except Exception as e:
        return {"error": str(e)}


def get_eth_balance(address: str, chain: str = "ethereum") -> dict:
    """
    Get native token balance for an EVM address.

    Returns dict with 'balance' (in native token string) and 'error' (if any).
    """
    # Normalize address
    addr = address.strip()
    if not addr.startswith("0x"):
        addr = "0x" + addr

    rpc = RPC_ENDPOINTS.get(chain)
    if not rpc:
        return {"error": f"unsupported chain: {chain}"}

    result = _rpc_call(rpc, "eth_getBalance", [addr, "latest"])

    if "error" in result:
        return {"error": result["error"]}

    if "result" not in result:
        return {"error": "no result in response"}

    hex_balance = result["result"]  # e.g. "0x0234..."
    try:
        wei = int(hex_balance, 16)
        token_balance = wei / 10 ** NATIVE_DECIMALS
        return {
            "balance": token_balance,
            "symbol": NATIVE_CURRENCIES.get(chain, "ETH"),
            "chain": CHAIN_NAMES.get(chain, chain.title()),
            "address": addr,
            "raw_hex": hex_balance,
        }
    except (ValueError, TypeError):
        return {"error": f"failed to parse balance: {hex_balance}"}


def get_balances(address: str, chains: list[str] | None = None) -> dict:
    """
    Get balances across multiple EVM chains.

    Args:
        address: EVM wallet address
        chains: List of chain keys (default: all supported chains)

    Returns dict mapping chain_key -> balance result.
    """
    if chains is None:
        chains = list(RPC_ENDPOINTS.keys())

    results = {}
    for chain in chains:
        if chain not in RPC_ENDPOINTS:
            results[chain] = {"error": f"unsupported chain: {chain}"}
            continue
        results[chain] = get_eth_balance(address, chain)

    return results
