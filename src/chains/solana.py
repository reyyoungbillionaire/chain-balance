"""
Solana balance checker.
"""

import json
from urllib.request import Request, urlopen
from urllib.error import URLError

SOLANA_RPC = "https://api.mainnet-beta.solana.com"
LAMPORTS_PER_SOL = 1_000_000_000


def _sol_rpc(method: str, params: list) -> dict:
    """Make a JSON-RPC call to Solana."""
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }).encode()

    req = Request(SOLANA_RPC, data=payload, headers={
        "Content-Type": "application/json",
        "User-Agent": "chain-balance/1.0",
    })

    try:
        resp = urlopen(req, timeout=15)
        return json.loads(resp.read())
    except URLError as e:
        return {"error": str(e.reason)}
    except Exception as e:
        return {"error": str(e)}


def get_sol_balance(address: str) -> dict:
    """
    Get SOL balance for a Solana address.

    Returns dict with 'balance', 'symbol', 'address', or 'error'.
    """
    addr = address.strip()

    result = _sol_rpc("getBalance", [addr])

    if "error" in result:
        return {"error": str(result["error"])}

    if "result" not in result:
        return {"error": "no result from Solana RPC"}

    try:
        lamports = result["result"]["value"]
        sol = lamports / LAMPORTS_PER_SOL
        return {
            "balance": sol,
            "symbol": "SOL",
            "chain": "Solana",
            "address": addr,
            "raw_lamports": lamports,
        }
    except (KeyError, TypeError, ValueError) as e:
        return {"error": f"failed to parse Solana balance: {e}"}


def is_valid_solana_address(address: str) -> bool:
    """Basic validation: base58, 32-44 chars."""
    import re
    return bool(re.match(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$", address.strip()))
