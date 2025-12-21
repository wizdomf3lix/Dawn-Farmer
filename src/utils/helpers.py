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

def load_file(path):
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def show_banner():
    logo = [
        "██     ██ ██ ███    ██ ███████ ███    ██ ██ ██████  ",
        "██     ██ ██ ████   ██ ██      ████   ██ ██ ██   ██ ",
        "██  █  ██ ██ ██ ██  ██ ███████ ██ ██  ██ ██ ██████  ",
        "██ ███ ██ ██ ██  ██ ██      ██ ██  ██ ██ ██ ██      ",
        " ███ ███  ██ ██   ████ ███████ ██   ████ ██ ██      ",
    ]
    
    print(f"\n{Fore.CYAN}╔{'═'*58}╗{Style.RESET_ALL}")
    for line in logo:
        print(f"{Fore.CYAN}║{Fore.YELLOW}{line}{Fore.CYAN}║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╠{'═'*58}╣{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║ {Fore.GREEN}{Style.BRIGHT}🌅 DAWN FARMER v1.0 - by WINSNIP{' '*25}{Fore.CYAN}║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║ {Fore.WHITE}📱 Telegram: {Fore.YELLOW}https://t.me/winsnip{' '*22}{Fore.CYAN}║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚{'═'*58}╝{Style.RESET_ALL}\n")
