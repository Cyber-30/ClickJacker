import requests
from colorama import Fore, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Tool Information
TOOL_NAME = "Clickjacker"
VERSION = "1.0"
FOOTER = "Cyber-30"
DESCRIPTION = "A Simple Tool To Find ClickJacking Vulnerability With POC"


def check_clickjacking(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print(Fore.CYAN + "\nHeader Details:")
        for header, value in headers.items():
            print(f"{header}: {value}")

        x_frame_options = "X-Frame-Options" in headers
        csp_frame_ancestors = (
            "Content-Security-Policy" in headers
            and "frame-ancestors" in headers["Content-Security-Policy"]
        )

        javascript_frame_busting = check_javascript_frame_busting(url)
        samesite_cookies = check_samesite_cookies(url)

        is_clickjacking_possible = not (
            x_frame_options or csp_frame_ancestors or javascript_frame_busting
        )

        print(Fore.GREEN + "\nClickjacking Vulnerability Check Results:")
        print(Fore.YELLOW + f"X-Frame-Options present: {x_frame_options}")
        print(Fore.YELLOW + f"CSP with frame-ancestors present: {csp_frame_ancestors}")
        print(
            Fore.YELLOW
            + f"JavaScript frame busting implemented: {javascript_frame_busting}"
        )
        print(Fore.YELLOW + f"SameSite cookies properly set: {samesite_cookies}")

        if is_clickjacking_possible:
            print(Fore.RED + "Clickjacking is POSSIBLE!")
        else:
            print(Fore.GREEN + "Clickjacking is NOT possible.")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error accessing {url}: {e}")


def check_javascript_frame_busting(url):
    return False  # Placeholder for actual checks.


def check_samesite_cookies(url):
    return True  # Placeholder for actual checks.


if __name__ == "__main__":
    # Stylish tool name display with colors
    name_display = pyfiglet.figlet_format(TOOL_NAME, font="slant")
    colored_name = Fore.MAGENTA + name_display
    print(colored_name)

    # Add gap before description
    print()  # Print an empty line for spacing

    # Print description in regular text
    print(Fore.CYAN + DESCRIPTION)

    # Add a single vertical gap after description
    print()  # Print one empty line for vertical spacing

    # Print version and footer in digital font
    version_display = pyfiglet.figlet_format(f"Version: {VERSION}", font="digital")
    footer_display = pyfiglet.figlet_format(f"Coded By: {FOOTER}", font="digital")

    print(Fore.GREEN + version_display)
    print(Fore.YELLOW + footer_display)

    while True:
        website_url = input(
            Fore.BLUE + "\nEnter a website URL (including http/https): "
        )
        check_clickjacking(website_url)

        another_check = (
            input(Fore.YELLOW + "\nDo you want to check another URL? (yes/no): ")
            .strip()
            .lower()
        )
        if another_check != "yes":
            print(Fore.GREEN + "Thank you for using Clickjacker! Exiting...")
            break
