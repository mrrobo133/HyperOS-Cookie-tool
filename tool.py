import json
import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

TOKEN_FILE = "token.txt"


def banner():
  print(
      Fore.CYAN
      + Style.BRIGHT
      + """
    =========================================
       Xiaomi HyperOS Local PassToken Tool   
       (100% Transparent Python Script)      
    =========================================
    """
  )
  print(
      Fore.YELLOW
      + "[!] DISCLAIMER: Strictly for local lab & educational use only.\n"
  )


def setup_token():
  print(Fore.GREEN + "[*] --- Option 1: Cookie Setup & PassToken Extraction ---")
  print(
      Fore.WHITE
      + "Enter your Xiaomi account cookies from Firefox Cookie-Editor:\n"
  )

  pass_token = input(
      Fore.YELLOW + "Enter your 'passToken' value: "
  ).strip()
  c_user_id = input(
      Fore.YELLOW + "Enter your 'cUserId' (or userId): "
  ).strip()
  device_id = input(Fore.YELLOW + "Enter your 'deviceId': ").strip()

  if not pass_token:
    print(Fore.RED + "[X] Error: passToken cannot be empty!")
    return

  data = {
      "passToken": pass_token,
      "cUserId": c_user_id,
      "deviceId": device_id,
  }

  # Save to local file securely
  with open(TOKEN_FILE, "w") as f:
    json.dump(data, f, indent=4)

  print(
      Fore.GREEN
      + f"\n[✓] Success! PassToken securely saved to local file: {TOKEN_FILE}"
  )

  # Show token to naked eye in terminal
  print(Fore.CYAN + "\n[i] Saved Token Preview (Naked Eye View):")
  print(Fore.WHITE + f"    -> passToken : {pass_token}")
  print(Fore.WHITE + f"    -> cUserId   : {c_user_id}")
  print(Fore.WHITE + f"    -> deviceId  : {device_id}")


def start_tool():
  print(Fore.GREEN + "[*] --- Option 2: Start Tool (Token Reuse Logic) ---")

  if not os.path.exists(TOKEN_FILE):
    print(
        Fore.RED
        + "[X] Error: No token found! Please run 'Cookie Setup' (Option 1)"
        " first."
    )
    return

  # Read token from local file
  with open(TOKEN_FILE, "r") as f:
    data = json.load(f)

  pass_token = data.get("passToken")
  c_user_id = data.get("cUserId", "N/A")
  device_id = data.get("deviceId", "N/A")

  print(Fore.CYAN + "[i] Loaded PassToken from local storage:")
  print(Fore.WHITE + f"    -> passToken : {pass_token}")
  print(Fore.WHITE + f"    -> cUserId   : {c_user_id}")
  print(Fore.WHITE + f"    -> deviceId  : {device_id}")

  print(
      Fore.YELLOW
      + "\n[i] Ready to deploy requests using local stored passToken without"
      " re-login..."
  )
  time.sleep(1)

  # Simulation of API request using loaded cookies
  cookies = {"passToken": pass_token, "cUserId": c_user_id}
  print(
      Fore.GREEN
      + f"[✓] Request engine simulated successfully using cookies: {cookies}"
  )


def main():
  while True:
    banner()
    print(Fore.WHITE + "1. Cookie Setup (Save & View PassToken)")
    print(Fore.WHITE + "2. Start Tool (Reuse Saved PassToken)")
    print(Fore.WHITE + "3. Exit")

    choice = input(
        Fore.YELLOW + "\nSelect an option [1-3]: "
    ).strip()

    if choice == "1":
      setup_token()
      input(Fore.CYAN + "\nPress Enter to return to main menu...")
    elif choice == "2":
      start_tool()
      input(Fore.CYAN + "\nPress Enter to return to main menu...")
    elif choice == "3":
      print(Fore.GREEN + "\nExiting... Stay safe and secure!")
      sys.exit(0)
    else:
      print(Fore.RED + "\n[X] Invalid option! Please choose 1, 2, or 3.")
      time.sleep(1)


if __name__ == "__main__":
  main()
