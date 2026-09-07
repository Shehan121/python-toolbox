#!/usr/bin/env python3
"""Run the doctests for every module in the toolbox package.

Exits non-zero if any doctest fails, so this is safe to use in CI.
"""

import doctest
import importlib
import pkgutil
import sys


def main():
    total = failed = 0
    for module_info in sorted(pkgutil.iter_modules(["toolbox"]), key=lambda m: m.name):
        module = importlib.import_module(f"toolbox.{module_info.name}")
        result = doctest.testmod(module, verbose=False)
        total += result.attempted
        failed += result.failed
        status = "FAIL" if result.failed else "ok"
        print(f"{module_info.name:16} {result.attempted - result.failed:>3}/{result.attempted:<3} {status}")

    print(f"\n{total - failed}/{total} doctests passed across the toolbox.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
