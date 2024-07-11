import os
import shutil
import time 
import pandas as pd
import numpy as np
from termcolor import colored, cprint
from alive_progress import alive_bar
from time import sleep
from tqdm import tqdm


# Global variables
df = pd.DataFrame(np.random.randint(0, 1000, (100000, 600)))
ascii_art_file = ""
ascii_art_header_visible = True
marker = "# === ASCIIStart modifications ==="
df = pd.DataFrame(np.random.randint(0, 1000, (100000, 600)))
headers_directory = "Headers"
current_header = "None"
header_counter = 1  # Counter for default header naming
bashrcSwitch = "~/.zshrc" #use ~/.bashrc for testing

def display_banner():
    ascii_art = """
  ______    ______    ______   ______  ______   ______     __                           __     
 /      \  /      \  /      \ |      \|      \ /      \   |  \                         |  \    
|  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$ \$$$$$$|  $$$$$$\ _| $$_     ______    ______  _| $$_   
| $$__| $$| $$___\$$| $$   \$$  | $$    | $$  | $$___\$$|   $$ \   |      \  /      \|   $$ \  
| $$    $$ \$$    \ | $$        | $$    | $$   \$$    \  \$$$$$$    \$$$$$$\|  $$$$$$  $$$$$$  
| $$$$$$$$ _\$$$$$$\| $$   __   | $$    | $$   _\$$$$$$\  | $$ __  /      $$| $$   \$$  | $$ __ 
| $$  | $$|  \__| $$| $$__/  \ _| $$_  _| $$_ |  \__| $$  | $$|  \|  $$$$$$$| $$       | $$| 
| $$  | $$ \$$    $$ \$$    $$|   $$ \|   $$ \ \$$    $$   \$$  $$ \$$    $$| $$        \$$  $$
 \$$   \$$  \$$$$$$   \$$$$$$  \$$$$$$ \$$$$$$  \$$$$$$     \$$$$   \$$$$$$$ \$$         \$$$$ 
"""

    if ascii_art_header_visible:
        cprint(ascii_art, "cyan")
        cprint("""                                                                              Created by: SYR3
""", "light_magenta")
        
def display_options():
    options = [
        "\n1. Add ASCII Header",
        "2. Update Header",
        "3. Edit Headers",
        "4. Remove Headers",
        "5. Help",
        "6. Exit"
    ]
    cprint("Select an option to get started:", "red")
    for option in options:
        cprint(option, "yellow")

def colored_input(prompt, color):
    cprint(prompt, color, end='')
    return input().strip().lower()

def ensure_headers_directory():
    if not os.path.exists(headers_directory):
        os.makedirs(headers_directory)

def list_headers():
    ensure_headers_directory()
    return os.listdir(headers_directory)

def display_header_list():
    headers = list_headers()
    if not headers:
        cprint("No headers found.", "red")
        return False
    cprint("Available headers:", "cyan")
    for idx, header in enumerate(headers, start=1):
        if header == current_header:
            cprint(f"\n  {idx}. {header} (current)", "green")
        else:
            cprint(f"\n  {idx}. {header}", "yellow")
    return True

def add_ascii_header():
    
    global header_counter
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        
        cprint('\n                          INSTRUCTIONS', "red")

        cprint('\n1. Create or add your custom ascii art file into ASCIIStart folder.', "yellow")
        cprint('\n2. Type in the name of the saved file and click enter.', "yellow")
        cprint("\n3. Rename new file when propmted. (optional)", "yellow")
        cprint("\n4. Done! All newly added headers will be saved to ./headers.", "yellow")
        cprint("\n")
    

        # Reset header counter if no files exist in the directory
        if not list_headers():
            header_counter = 1
        
        file_path = colored_input("\nEnter file name or type 'back' to return: ", "cyan")
        if file_path == 'back':
            return
        
        if os.path.isfile(file_path):
            default_header_name = f"head_{header_counter:02}.txt"
            header_counter += 1
            
            print("\n")
            cprint("Copying file to Headers folder!", "light_magenta")
            ascii_art_file = file_path
            
            # Progress Bar
            with alive_bar(200, bar = 'bubbles', spinner = 'notes2') as bar:
                for i in range(200):
                    sleep(0.03)
                    bar()    

            cprint(f"Complete!","green") 
            
            time.sleep(2)
            
            ensure_headers_directory()
            new_header_path = os.path.join(headers_directory, default_header_name)
            shutil.copy(file_path, new_header_path)
            
            while True:
                rename_choice = colored_input("Would you like to rename this file? (y/n): ", "cyan")
                if rename_choice == 'y':
                    new_name = colored_input("\nEnter name (without extension): ", "yellow")
                    new_header_path = os.path.join(headers_directory, f"{new_name}.txt")
                    os.rename(os.path.join(headers_directory, default_header_name), new_header_path)
                    cprint(f"\nFile renamed to: {new_name}.txt", "white")
                    time.sleep(2)
                    cprint("Returning...", "red")

                    break
                elif rename_choice == 'n':
                    cprint(f"\nFile saved as: {default_header_name}", "white")
                    time.sleep(2)
                    cprint("Returning...", "red")
                    break
                else:
                    cprint("\nInvalid input. Please enter 'y' or 'n'.", "red")
                    cprint("""
   ⢀⣤⣶⣶⣤⣄⡀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠸⣿⣿⣿⣿⣿⡟⡟⡗ ⣿⠉⣿⠉⣿⡏⠹⡏⢹⡏⢹⣿⣿⠉⣿⠉⣿⡟⢋⠛⣿⠉⡟⢉⡏⠹⠏⣹⣿
⠀⠀⠙⠏⠯⠛⣉⢲⣧⠟ ⣿⠄⣿⠄⣿⡇⡄⠁⢸⡇⢸⣿⣿⠄⣿⠄⣿⠄⣿⣿⣿⠄⡀⢻⣿⡄⢠⣿⣿
⠀⠀⠠⢭⣝⣾⠿⣴⣿⠇ ⣿⣦⣤⣴⣿⣧⣿⣤⣼⣧⣬⣭⣿⣦⣤⣴⣿⣧⣤⣤⣿⣤⣷⣤⣿⣧⣼⣿⣿
⠀⠀⢐⣺⡿⠁⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣶⣶⣶⣶⣶⣶⠀
⠀⠀⣚⣿⠃ ⣶⣶⣶⣶
⢀⣿⣿⣿⣷⢒⣢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣶⣄⠄
⢰⣿⣿⡿⣿⣦⠬⢝⡄⠀⠀⠀⠀⠀⠀⢠⣿⠿⠿⠟⠛⠋⠁
⠠⢿⣿⣷⠺⣿⣗⠒⠜⡄⠀⠀⠀⠀⣴⠟⠁
⠀⣰⣿⣷⣍⡛⣯⣯⣙⡁⠀⠀⣠⡾⠁
⠀⠨⢽⣿⣷⢍⣛⣶⢷⣼⣠⣾⠋
⠀⠀⠘⢿⣿⣖⠬⣹⣶⣿⠟⠁
⠀⠀⠀⠚⠿⠿⡒⠨⠛⠋
⠀⠀⠀⠐⢒⣛⣷
⠀⠀⠀⢘⣻⣭⣭
⠀⠀⠀⡰⢚⣺⣿
⠀⠀⢠⣿⣿⣿⣿⣦⡄
⠀⠀⢸⡿⢿⣿⢿⡿⠃
⠀⠀⠘⡇⣸⣿⣿⣿⣆
⠀⠀⠀⠀⠸⣿⡿⠉⠁
⠀⠀⠀⠀⠀⢿⡟
                           """, "dark_grey")
                    cprint("Invalid input. Please enter 'y' or 'n'.", "red")
                    print("\n")
                    time.sleep(1.5)  # Delay to show confirmation message
            break
        else:
            cprint("\nInvalid file path. Please enter a valid file path.", "red")
            cprint("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠛⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⠴⠞⠛⠉⠉⠉⠉⠉⠉⠛⠒⠾⢤⣀⠀⣀⣠⣤⣄⡀⠀⠀⠀
⠀⠀⠀⣠⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢭⡀⠀⠈⣷⠀⠀⠀
⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⢀⡟⠀⠀⠀
⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡅⠀⠀⠀
⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣀⠀
⣾⠀⠀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠸⡇⠉⣷
⣿⠀⠰⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣧⡴⠋
⣿⠀⠀⢸⠛⢫⠀⠀⢠⠴⠒⠲⡄⠀⠀⠀⠀⡝⠛⢡⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀
⢸⡄⠀⢸⡀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⠀⠀⠀⠀⠀⡼⣄⠀⠀
⠀⢳⡄⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⢸⠀⠀⠀⠀⢀⡼⠁⢸⡇⠀
⠀⠀⠙⢦⣷⡈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⡇⠀⣀⡴⠟⠒⠚⠋⠀⠀
⠀⠀⠀⠀⠈⠛⠾⢤⣤⣀⣀⡀⠀⠀⠀⠀⣀⣈⣇⡤⣷⠚⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⠇⠀⠩⣉⠉⠉⠉⣩⠍⠁⠀⢷⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡟⠐⠦⠤⠼⠂⠀⠸⠥⠤⠔⠂⠘⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣧⡟⠳⠒⡄⠀⠀⠀⡔⠲⠚⣧⣀⣿⠿⠷⣶⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣄⢀⠀⠀⡗⠀⠀⠀⡇⠄⢠⠀⣼⠟⠀⢀⣨⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢶⠬⠴⢧⣤⣤⣤⣽⣬⡥⠞⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀
                   ""","light_magenta")
            cprint("Invalid file path. Please enter a valid file path.", "red")
            time.sleep(1.5)  # Add delay to allow the user to read the error message


def display_header_list():
    headers = list_headers()
    if not headers:
        cprint("\nNo headers found.", "red")
        cprint("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠒⠒⠲⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠠⢚⣂⡀⠈⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⡴⠆⠀⠀⠀⠀⠀⢎⠐⢟⡇⠀⠈⢣⣠⠞⠉⠉⠑⢄⠀⠀⣰⠋⡯⠗⣚⣉⣓⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢠⢞⠉⡆⠀⠀⠀⠀⠀⠓⠋⠀⠀⠀⠀⢿⠀⠀⠀⠀⠈⢧⠀⢹⣠⠕⠘⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠘⠮⠔⠁⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠈⣇⠀⢳⠀⠀⠘⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠉⠓⠦⣧⠀⠀⠀⠀⢦⠤⠤⠖⠋⠇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠸⡄⠈⡇⠀⠀⢹⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠈⣆⠀⠀⠀⢱⠀⡇⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠸⡄⠀⠀⠀⠳⠃⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⢠⢏⠉⢳⡀⠀⠀⢹⠀⠀⠀⠀⢠⠀⠀⠀⠑⠤⣄⣀⡀⠀⠀⠀⠀⠀⣀⡤⠚⠀⠀⠀⠀⠀⢸⢢⡀⠀⠀⠀⠀⠀⢰⠁⠀
⠀⠀⣀⣤⡞⠓⠉⠁⠀⢳⠀⠀⢸⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⢸⠀⠙⠦⣤⣀⣀⡤⠃⠀⠀
⠀⣰⠗⠒⣚⠀⢀⡤⠚⠉⢳⠀⠈⡇⠀⠀⠀⢸⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⠵⡾⠋⠉⠉⡏⠀⠀⠀⠈⠣⣀⣳⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⡰⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠲⠤⠤⠤⠴⠚⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               """, "red")
        cprint("\nNo headers found.", "red")
        sleep(1.5)

        return False
    cprint("\nAvailable headers:", "red")
    for idx, header in enumerate(headers, start=1):
        if header == current_header:
            cprint(f"  {idx}. {header} (current)", "green")
        else:
            cprint(f"\n  {idx}. {header}", "yellow")  # Changed list color to purple (magenta)
    return True

def update_header():
    global current_header
    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        if not display_header_list():
            time.sleep(2)
            return


        headers = list_headers()
        ct = print("")
        header_input = colored_input("\nChoose header or type 'back' to return: ", "blue")
        
        if header_input == 'back':
            return

        try:
            header_index = int(header_input) - 1
            header_name = headers[header_index]
            header_path = os.path.join(headers_directory, header_name)
            if os.path.isfile(header_path):
                try:
                    with open(header_path, 'r') as file:
                        lines = file.readlines()
                    
                    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen before loading progress bar
                    display_banner()

                    # Modify .bashrc to add the selected header
                    with open(os.path.expanduser(bashrcSwitch), 'a') as zshrc:
                        zshrc.write(f"\n{marker}\n")
                        for line in lines:
                            zshrc.write(f'echo "{line.rstrip()}"\n')
                        zshrc.write(f"# === End of ASCIIStart modifications ===\n")
                    
                    cprint("\nModifying heder file ...", "light_magenta")
                    
                    # Progress Bar
                    with alive_bar(200, bar='bubbles', spinner='notes2') as bar:
                        for i in range(100):
                            sleep(0.03)
                            bar() 

                             
                    cprint("Updating terminal header...", "light_magenta")
                    
                    # Progress Bar
                    with alive_bar(200, bar='bubbles', spinner='notes2') as bar:
                        for i in range(100):
                            sleep(0.03)
                            bar() 



                    current_header = header_name
                    cprint(f"Update Complete!", "green")
                    cprint(f"\nThe current header is now set to: {header_name}", "white")
                    time.sleep(3.5)
                    cprint("Returning...", "red")
                    time.sleep(2)
                    break
                except Exception as e:
                    cprint(f"An error occurred: {e}", "red")
            else:
                cprint("Invalid header index. Please enter a valid index.", "red")
        except ValueError:
            cprint("Invalid input. Please enter a valid index number.", "red")
        time.sleep(2)  # Add delay to allow the user to read the error message

def edit_headers():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        if not display_header_list():
            time.sleep(2)
            return
        
        headers = list_headers()
        choice = colored_input("\nChoose file to edit or type 'back' to return: ", "blue").lower()

        if choice == 'back':
            return

        try:
            header_index = int(choice) - 1
            if 0 <= header_index < len(headers):
                header_name = headers[header_index]
                header_path = os.path.join(headers_directory, header_name)
                if os.path.isfile(header_path):
                    available_editors = ["nano", "vim", "gedit", "notepad", "code"]  # List of common text editors
                    editor_found = False
                    for editor in available_editors:
                        if shutil.which(editor):
                            os.system(f"{editor} {header_path}")
                            editor_found = True
                            break
                    if not editor_found:
                        cprint("\nNo available text editor found. Please install a text editor (e.g., nano, vim, gedit, notepad, code).", "red")
                    else:
                        cprint(f"\nEdits to {header_name} are saved.", "green")
                        time.sleep(2)
                else:
                    cprint("Invalid header index. Please enter a valid index.", "red")
            else:
                cprint("Invalid header index. Please enter a valid index.", "red")
        except ValueError:
            cprint("Invalid input. Please enter a valid index number.", "red")
        time.sleep(2)  # Add delay to allow the user to read the error message


def remove_headers():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        if not display_header_list():
            time.sleep(2)
            return
        
        headers = list_headers()
        choice = colored_input("\nEnter header to remove or type 'back' to return: ", "blue").lower()
        
        if choice == 'back':
            return

        try:
            header_index = int(choice) - 1
            if 0 <= header_index < len(headers):
                header_name = headers[header_index]
                header_path = os.path.join(headers_directory, header_name)
                
                if header_name == current_header:
                    cprint("\nCannot remove the current header. Please set a different current header first.", "red")
                    cprint("""
⣿⣿⡿⣫⣾⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣀⣀⠄⠄⠄⠄⠄⠄
⣿⡇⠱⠉⠁⠄⠄⠄⠄⠄⠄⢀⣀⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣦⠄⠄⠄⠄⠄
⣿⡇⠄⠄⠄⠄⠄⢀⣠⣛⡩⣩⣭⡹⣿⣿⣿⣿⠞⣛⣛⣛⡲⣿⡇⠄⠄⠄⠄
⣿⡇⠄⠄⠄⡾⣡⣾⣿⣷⣹⣿⣿⡿⣪⡻⠟⣱⣿⣿⣿⣿⣿⣷⡹⠄⠄⠄⠄
⣿⡇⠄⠄⣼⡇⣿⣻⣿⠟⡛⢿⣿⣾⣿⡇⢰⣍⢻⡿⠛⢿⣿⡭⣿⣷⠄⠄⠄
⣿⣧⣄⡀⣿⡇⣮⣽⣿⣮⣉⣾⣿⣿⣿⣇⡸⣿⣿⣆⠛⣰⣿⣾⡿⣿⠄⠄⠄
⣿⣇⡼⣄⣿⣿⡄⠙⢿⣏⣿⣿⡮⠁⣉⣾⣷⡈⠃⢿⣿⣬⡭⠝⣀⣿⠄⠄⠐
⡆⡇⣹⣿⣿⣿⣿⡿⠓⠛⣉⣉⣉⣉⣙⣛⠓⠾⣟⢿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠙
⠁⡇⣞⣿⡿⠋⠁⠄⠄⠈⠉⠙⠛⠛⠻⠿⠿⠿⣶⣌⠻⣿⣿⣿⣿⣿⢗⢴⣆⢣
⠸⣇⡻⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢻⣷⡌⢿⣿⣿⣿⢸⠼⣣⣾
⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⠙⠛⠈⣿⡫⡼⢠⣾⣿⣿
⣿⣇⠄⣀⣠⡀⠄⠄⠴⠾⠿⠿⠶⠶⣦⣤⡀⠄⠄⠄⠄⠄⠄⢨⠯⢁⣿⣿⣿⣿
⣿⣿⣦⢒⠤⣅⡶⣶⣶⣾⣿⣿⣿⣷⣶⣮⣍⠢⠄⠄⠄⠄⠄⠐⢠⣾⣿⣿⣿⣿
⣿⣿⣿⣧⡐⠫⣉⡿⣬⡞⢿⣿⢯⠽⣶⡽⢟⣛⢖⣨⣛⠛⢃⣴⣿⣿⣿⣿⣿⣿
                           """, "red")
                    cprint("Cannot remove the current header. Please set a different current header first.", "red")

                else:
                    if os.path.isfile(header_path):
                        try:
                            # Remove header from .bashrc
                            print("\n")
                            os.system(f"sed -i -e '/^echo /d' -e '/^# /d' {bashrcSwitch}")
                            
                            # Delete header file from Headers directory
                            os.remove(header_path)
                            

                            cprint("\nRemoving header from headers directory", "light_magenta")
                             # Progress Bar
                            with alive_bar(50, bar='bubbles', spinner='notes2') as bar:
                                for i in range(50):
                                    sleep(0.03)
                                    bar() 
                                    
                            cprint("\nRemoving header from system file", "light_magenta")
                            # Progress Bar
                            with alive_bar(100, bar='bubbles', spinner='notes2') as bar:
                                for i in range(100):
                                    sleep(0.03)
                                    bar() 


                            
                            cprint(f"\n{header_name} has been removed from both Headers directory and system file!", "green")
                            time.sleep(2)
                        except Exception as e:
                            cprint(f"An error occurred: {e}", "red")
                    else:
                        cprint("Header file not found.", "red")
            else:
                cprint("Invalid header index. Please enter a valid index.", "red")
        except ValueError:
            cprint("Invalid input. Please enter a valid index number.", "red")
        time.sleep(2)  # Add delay to allow the user to read the error message


def display_help():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
   
    cprint("Help - ASCII Header Manager", "red")
    help_text = """
1. Add ASCII Header:
    - Allows you to add a new ASCII header from a file.
    - 

2. Update Header:
    - Sets a selected header as the current header on terminal and adds it to system file.
    - Each line is prefixed with echo " and suffixed with ".
    - Includes a comment tracker for easier removal from system file..

3. Edit Headers:
    - Opens the selected header file in a text editor for editing.
    - Requires a text editor installed (e.g., nano, vim, gedit, notepad, code).

4. Remove Headers:
    - Deletes the selected header file from both Headers directory and system file.

5. Help:
    - Displays this help page with basic commands and usage of the program.

6. Exit:
    - Closes the program.

Footer text: Buy me a coffee
    """
    cprint(help_text, "yellow")

if __name__ == "__main__":
    ensure_headers_directory()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        display_options()
        choice = colored_input("\nEnter your choice: ", "blue")
        
        if choice == '1':
            add_ascii_header()
        
        elif choice == '2':
            update_header()
        
        elif choice == '3':
            edit_headers()
        
        elif choice == '4':
            remove_headers()
        
        elif choice == '5':
            display_help()
            colored_input("\nPress Enter to return to the main menu: ", "blue")
        
        elif choice == '6' or choice == 'exit':
            cprint("Exiting the program. Goodbye!", "red")
            break
        
        else:
            cprint("Invalid choice. Please enter a number from 1 to 6 or 'exit'.", "red")
            time.sleep(2)  # Add delay to allow the user to read the error message
