import asyncio
import sys
from pathlib import Path

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from config import CONFIG
from core import FarmManager
from utils import load_file, show_banner

async def main():
    show_banner()
    
    tokens = load_file(CONFIG['tokens_file'])
    proxies = load_file(CONFIG['proxies_file'])
    
    if not tokens:
        print(f"✗ No tokens found in {CONFIG['tokens_file']}")
        print(f"\nPlease add your x-privy-token to tokens.txt (one per line)")
        return
    
    print(f"\n✓ Found {len(tokens)} token(s)")
    if proxies:
        print(f"✓ Found {len(proxies)} proxy(ies)")
    else:
        print(f"⚠ No proxies.txt - running without proxy")
        print(f"  To use proxy, create proxies.txt (see proxies.example.txt)")
    
    fm = FarmManager(CONFIG)
    await fm.start(tokens, proxies if proxies else None)

if __name__ == "__main__":
    asyncio.run(main())
