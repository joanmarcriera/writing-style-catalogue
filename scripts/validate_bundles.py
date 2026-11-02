#!/usr/bin/env python3
"""Validate all worked examples against the professional bundle contract."""

from pathlib import Path

from bundle_contract import BundleContractError, load_bundles


def main() -> int:
    base_path = Path(__file__).parent.parent
    notices: list[str] = []
    try:
        bundles = load_bundles(base_path, notices)
    except BundleContractError as error:
        print(f"✗ Bundle validation failed: {error}")
        return 1

    for notice in notices:
        print(f"ℹ Notice: {notice}")
    print(f"✓ Professional bundle contract valid ({len(bundles)} bundles)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
