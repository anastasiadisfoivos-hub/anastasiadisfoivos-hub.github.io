# Example usage script for MacFinder
import sys
from pathlib import Path

# Ensure src is on sys.path (run this script from the repo root)
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from macfinder import Macbook

def main():
    user = Macbook(
        name="Alex",
        exp=3,
        model="Apple MacBook Air (2024)",
        response="Apple MacBook Air (2024)",
        money_av=2000,
        cond="NEW"
    )

    user.intro()
    print()
    user.mac()
    print()
    user.mac_extended()
    print()
    user.mac_cash()

if __name__ == "__main__":
    main()