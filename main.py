#!/usr/bin/python

# Copyright (C) Anasov <me@anasov.ly> - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Anasov <me@anasov.ly>, 05, May, 2024.

import random
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt

__CHANNEL_USERNAME__ = "HadjiCpm"
__GROUP_USERNAME__   = "HadjiDiscussion"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold green]♕ HadjiNuker[/bold green]: Car Parking Multiplayer Hacking Tool.")
    console.print(f"[bold green]♕ Telegram[/bold green]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue] or [bold blue]@{__GROUP_USERNAME__}[/bold blue].")
    console.print("==================================================")
    console.print("[bold yellow]! Note[/bold yellow]: Logout from CPM before using this tool !.", end="\n\n")

def load_player_data(cpm):
    data = cpm.get_player_data().get('data')
    console.print("[bold][red]========[/red][ PLAYER DETAILS ][red]========[/red][/bold]")
    console.print(f"[bold green] Name   [/bold green]: { (data.get('Name')      if 'Name' in data else 'UNDEFINED') }.")
    console.print(f"[bold green] LocalID[/bold green]: { (data.get('localID')   if 'localID' in data else 'UNDEFINED') }.")
    console.print(f"[bold green] Money  [/bold green]: { (data.get('money')     if 'money' in data else 'UNDEFINED') }.")
    console.print(f"[bold green] Coins  [/bold green]: { (data.get('coin')      if 'coin' in data else 'UNDEFINED') }.")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(f"{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold]➤ Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold]➤ Account Password[/bold]", "Password", password=False)
        console.print("[bold cyan]↻ Trying to Login[/bold cyan]: ", end=None)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]ACCOUNT NOT FOUND[/bold red].")
                sleep(2)
            elif login_response == 101:
                console.print("[bold red]WRONG PASSWORD[/bold red].")
                sleep(2)
            else:
                console.print("[bold red]TRY AGAIN[/bold red].")
                console.print("[bold yellow]! Note:[/bold yellow]: make sure you filled out the fields !.")
                sleep(2)
        else:
            console.print("[bold green]SUCCESSFUL[/bold green].")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            console.print("[bold cyan](01): Increase Money [/bold cyan]")
            console.print("[bold cyan](02): Increase Coins [/bold cyan]")
            console.print("[bold cyan](03): King Rank  [/bold cyan]")
            console.print("[bold cyan](04): Change ID [/bold cyan]")
            console.print("[bold cyan](05): Change Name [/bold cyan]")
            console.print("[bold cyan](06): Change Name (Rainbow) [/bold cyan]")
            console.print("[bold cyan](07): Unlock All Cars [/bold cyan]")
            console.print("[bold cyan](08): Account Delete [/bold cyan]")
            console.print("[bold cyan](09): Account Register [/bold cyan]")
            console.print("[bold cyan](10): Delete Friends [/bold cyan]")
            console.print("[bold cyan](11): Number Plates [/bold cyan]")
            console.print("[bold cyan](00): Exit[/bold cyan]", end="\n\n")
            service = IntPrompt.ask("[bold]➤ Select a Service [red][0-9 or 0][/red][/bold]", choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"], show_choices=False)
            if service == 0: # Exit
                console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
            elif service == 1: # Increase Money
                console.print("[bold cyan]✶ Insert how much money do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold]➤ Amount[/bold]")
                console.print("[bold cyan]↺ Saving your data[/bold cyan]: ", end=None)
                if cpm.set_player_money(amount):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                console.print("[bold cyan]✶ Insert how much coins do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold]➤ Amount[/bold]")
                console.print("[bold cyan]↺ Saving your data[/bold cyan]: ", end=None)
                if cpm.set_player_coins(amount):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold cyan]↺ Giving you a King Rank[/bold cyan]: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print("[bold cyan]✶ Enter your new ID.[/bold cyan]")
                new_id = Prompt.ask("[bold]➤ ID[/bold]")
                console.print("[bold cyan]↺ Saving your data[/bold cyan]: ", end=None)
                if cpm.set_player_localid(new_id):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print("[bold cyan]✶ Enter your new Name.[/bold cyan]")
                new_name = Prompt.ask("[bold]➤ Name[/bold]")
                console.print("[bold cyan]↺ Saving your data[/bold cyan]: ", end=None)
                if cpm.set_player_name(new_name):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                console.print("[bold cyan]✶ Enter your new Rainbow Name.[/bold cyan]")
                new_name = Prompt.ask("[bold]➤ Name[/bold]")
                console.print("[bold cyan]↺ Saving your data[/bold cyan]: ", end=None)
                if cpm.set_player_name(rainbow_gradient_string(new_name)):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 7: # Unlock All Cars
                continue
            elif service == 8: # Account Delete
                console.print("[bold cyan]✶ After deleting your account there is no going back !!.[/bold cyan]")
                answ = Prompt.ask("[bold cyan]➤ Do You want to Delete this Account ?![/bold cyan]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print("[bold cyan]↺ Deleting Your Account[/bold cyan]: [bold green]SUCCESSFUL.[/bold green].")
                    console.print("==================================")
                    console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                else: continue
            elif service == 9: # Account Register
                console.print("[bold cyan]✶ Registring new Account.[/bold cyan]")
                acc2_email = prompt_valid_value("[bold]➤ Account Email[/bold]", "Email", password=False)
                acc2_password = prompt_valid_value("[bold]➤ Account Password[/bold]", "Password", password=False)
                console.print("[bold cyan]↺ Creating new Account[/bold cyan]: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    console.print(f"[bold yellow]! You've been automatically signed in as[/bold yellow]: [blue]{acc2_email}[/blue]")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ This email is already exists !.[/bold yellow]")
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[bold cyan]↺ Deleting your Friends[/bold cyan]: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 11: # Number Plates
                console.print("[bold cyan]↺ Giving you a Number Plates[/bold cyan]: ", end=None)
                if cpm.set_player_plates():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            else:   continue
            break
        break