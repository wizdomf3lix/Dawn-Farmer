import asyncio
from .client import DawnClient

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except:
    HAS_COLOR = False
    class Fore:
        GREEN = YELLOW = RED = CYAN = MAGENTA = BLUE = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""

class FarmManager:
    def __init__(self, _cfg):
        self._cfg = _cfg
        self._clients = []
    
    async def _init_client(self, token, proxy=None):
        c = DawnClient(token, proxy)
        await c.auth()
        return c
    
    async def _show_stats(self, c):
        print(f"\n{Fore.CYAN}╔{'═'*58}╗")
        print(f"║{Fore.YELLOW}{Style.BRIGHT}{'📊 ACCOUNT STATISTICS':^58}{Fore.CYAN}{Style.RESET_ALL}║")
        print(f"║{Fore.WHITE}  User: {Fore.CYAN}{c._uid}{' '*(51-len(c._uid))}{Fore.CYAN}║")
        print(f"╠{'═'*58}╣{Style.RESET_ALL}")
        
        try:
            pts = await c.get_pts()
            curr_pts = pts.get('points', 0)
            ref_pts = pts.get('referral_points', 0)
            total = curr_pts + ref_pts
            print(f"{Fore.CYAN}║ {Fore.GREEN}{Style.BRIGHT}💰 POINTS{' '*48}{Fore.CYAN}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║{Fore.WHITE}   Current Points  : {Fore.YELLOW}{curr_pts:>15,}{' '*22}{Fore.CYAN}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║{Fore.WHITE}   Referral Points : {Fore.YELLOW}{ref_pts:>15,}{' '*22}{Fore.CYAN}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║{Fore.WHITE}   {Style.BRIGHT}Total Points    : {Fore.GREEN}{total:>15,}{Style.RESET_ALL}{' '*22}{Fore.CYAN}║{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.CYAN}║ {Fore.RED}💰 Error loading points{' '*34}{Fore.CYAN}║{Style.RESET_ALL}")
        
        try:
            st = await c.get_streak()
            streak = st.get('currentStreak', 0)
            print(f"{Fore.CYAN}╠{'─'*58}╣{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║ {Fore.MAGENTA}{Style.BRIGHT}🔥 STREAK{' '*48}{Fore.CYAN}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║{Fore.WHITE}   Current Streak  : {Fore.YELLOW}{streak:>3} days{' '*28}{Fore.CYAN}║{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.CYAN}║ {Fore.RED}🔥 Error loading streak{' '*33}{Fore.CYAN}║{Style.RESET_ALL}")
        
        try:
            ref = await c.get_ref()
            code = ref.get('referralCode', 'N/A')
            total_ref = ref.get('totalReferrals', 0)
            earned = ref.get('totalPointsEarned', 0)
            print(f"{Fore.CYAN}╠{'─'*58}╣{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║ {Fore.BLUE}{Style.BRIGHT}👥 REFERRALS{' '*45}{Fore.CYAN}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║{Fore.WHITE}   Referral Code   : {Fore.CYAN}{code:<37}{Fore.CYAN}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║{Fore.WHITE}   Total Referrals : {Fore.YELLOW}{total_ref:>15,}{' '*22}{Fore.CYAN}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║{Fore.WHITE}   Points Earned   : {Fore.GREEN}{earned:>15,}{' '*22}{Fore.CYAN}║{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.CYAN}║ {Fore.RED}👥 Error loading referrals{' '*30}{Fore.CYAN}║{Style.RESET_ALL}")
        
        try:
            h = await c.get_history()
            pings = len(h) if isinstance(h, list) else 0
            print(f"{Fore.CYAN}╠{'─'*58}╣{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║ {Fore.CYAN}{Style.BRIGHT}📈 ACTIVITY{' '*46}{Fore.CYAN}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║{Fore.WHITE}   Pings (24h)     : {Fore.YELLOW}{pings:>3}{' '*31}{Fore.CYAN}║{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.CYAN}║ {Fore.RED}📈 Error loading activity{' '*31}{Fore.CYAN}║{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}╚{'═'*58}╝{Style.RESET_ALL}\n")
    
    async def _farm_worker(self, c, idx):
        cnt = 0
        print(f"{Fore.GREEN}✓ Account #{idx+1} Authenticated")
        print(f"{Fore.WHITE}  User ID: {Fore.CYAN}{c._uid}{Style.RESET_ALL}")
        
        await self._show_stats(c)
        
        while True:
            try:
                r = await c.ping()
                if r.get("message") == "pong":
                    from datetime import datetime
                    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{Fore.GREEN}✓ {Fore.WHITE}Account #{idx+1} │ {Fore.CYAN}Ping Success {Fore.WHITE}│ {Fore.YELLOW}{ts}{Style.RESET_ALL}")
                    cnt += 1
                    
                    if cnt % 5 == 0:
                        await self._show_stats(c)
                else:
                    print(f"{Fore.RED}✗ {Fore.WHITE}Account #{idx+1} │ {Fore.RED}Ping Failed {Fore.WHITE}│ {r}{Style.RESET_ALL}")
                
                print(f"{Fore.MAGENTA}⏳ {Fore.WHITE}Account #{idx+1} │ {Fore.CYAN}Next ping in {Fore.YELLOW}{self._cfg['interval']}s{Style.RESET_ALL}\n")
                await asyncio.sleep(self._cfg['interval'])
            except Exception as e:
                print(f"{Fore.RED}✗ Account #{idx+1} Error: {e}{Style.RESET_ALL}")
                await asyncio.sleep(60)
    
    async def start(self, tokens, proxies=None):
        print(f"\n{Fore.YELLOW}🌾 Initializing {len(tokens)} farmer(s)...{Style.RESET_ALL}\n")
        
        for i, t in enumerate(tokens):
            px = proxies[i] if proxies and i < len(proxies) else None
            if px:
                print(f"{Fore.CYAN}  Account #{i+1}: Using proxy {px[:30]}...{Style.RESET_ALL}")
            else:
                print(f"{Fore.CYAN}  Account #{i+1}: No proxy (direct){Style.RESET_ALL}")
            
            c = await self._init_client(t, px)
            self._clients.append(c)
        
        print()
        tasks = [self._farm_worker(c, i) for i, c in enumerate(self._clients)]
        
        try:
            await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}🛑 Stopping all farmers...{Style.RESET_ALL}")
            for c in self._clients:
                await c.close()
            print(f"{Fore.GREEN}✓ All farmers stopped successfully{Style.RESET_ALL}")

