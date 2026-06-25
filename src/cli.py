"""
chain-balance CLI — check wallet balances across multiple chains.
"""

import os
import sys
from src.chains.evm import get_eth_balance, get_balances, RPC_ENDPOINTS, CHAIN_NAMES
from src.chains.solana import get_sol_balance, is_valid_solana_address


def detect_address_type(address: str) -> str:
    """Detect if address is EVM (0x...) or Solana (base58)."""
    addr = address.strip()
    if addr.startswith("0x") or (len(addr) == 42 and all(c in "0123456789abcdefABCDEF" for c in addr.lstrip("0x"))):
        return "evm"
    if is_valid_solana_address(addr):
        return "solana"
    return "unknown"


def format_balance(bal: float, symbol: str) -> str:
    """Pretty-print a balance value."""
    if bal >= 1000:
        return f"{bal:,.4f} {symbol}"
    if bal >= 1:
        return f"{bal:.4f} {symbol}"
    if bal >= 0.001:
        return f"{bal:.6f} {symbol}"
    return f"{bal:.9f} {symbol}"


def print_header(text: str):
    """Print a section header."""
    width = 50
    print()
    print("=" * width)
    print(f"  {text}")
    print("=" * width)


def print_result(label: str, result: dict):
    """Print a single chain result."""
    if "error" in result:
        print(f"  ✗ {label:<20} ERROR: {result['error']}")
    else:
        bal = result["balance"]
        sym = result["symbol"]
        print(f"  ✓ {label:<20} {format_balance(bal, sym)}")


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print("Usage: python run.py <wallet_address> [chain]")
        print()
        print("Check wallet balance across multiple blockchain networks.")
        print()
        print("Arguments:")
        print("  address    Wallet address (EVM 0x... or Solana address)")
        print("  chain      Optional: specific chain to check")
        print(f"             Default: all supported chains")
        print()
        print("Supported EVM chains:")
        for key, name in CHAIN_NAMES.items():
            print(f"  - {key:<12} {name}")
        print("  - solana     Solana")
        print()
        print("Examples:")
        print("  python run.py 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18")
        print("  python run.py 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18 ethereum")
        print("  python run.py <solana_address>")
        return

    address = args[0]
    addr_type = detect_address_type(address)

    if addr_type == "unknown":
        print("✗ Could not detect address type.")
        print("  EVM addresses start with '0x' (42 chars hex)")
        print("  Solana addresses are base58 (32-44 chars)")
        sys.exit(1)

    chain_filter = args[1].lower() if len(args) > 1 else None

    if addr_type == "evm":
        # Normalize
        if not address.startswith("0x"):
            address = "0x" + address

        if chain_filter:
            print_header(f"Checking {address[:10]}...{address[-6:]} on {chain_filter.title()}")
            result = get_eth_balance(address, chain_filter)
            print_result(CHAIN_NAMES.get(chain_filter, chain_filter.title()), result)
        else:
            print_header(f"Checking {address[:10]}...{address[-6:]} across all EVM chains")
            results = get_balances(address)
            for chain_key, result in results.items():
                print_result(CHAIN_NAMES.get(chain_key, chain_key.title()), result)

    elif addr_type == "solana":
        print_header(f"Checking Solana address: {address[:10]}...{address[-6:]}")
        result = get_sol_balance(address)
        print_result("Solana", result)

    print()
    print(f"  Data from public RPC nodes — may have rate limits.")
    print()
