#!/usr/bin/env python3
"""Validate all worked examples against the professional bundle contract."""

from pathlib import Path

from bundle_contract import BundleContractError, load_bundles


def main() -> int:
    base_path = Path(__file__).parent.parent
    try:
        bundles = load_bundles(base_path)
    except BundleContractError as error:
        print(f"✗ Bundle validation failed: {error}")
        return 1

    print(f"✓ Professional bundle contract valid ({len(bundles)} bundles)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
