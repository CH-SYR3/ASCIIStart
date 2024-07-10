import os
import shutil
import time
import pandas as pd
import numpy as np
from termcolor import colored, cprint

# Global variables
ascii_art_file = ""
ascii_art_header_visible = True
marker = "# === ASCIIStart modifications ==="
df = pd.DataFrame(np.random.randint(0, 1000, (100000, 600)))
headers_directory = "Headers"
current_header = "None"
header_counter = 1  # Counter for default header naming
initial_bashrc_backup = os.path.join(headers_directory, "initial_bashrc_backup")

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

def display_options():
    options = [
        "1. Add ASCII Header",
        "2. Update Header",
        "3. Edit Headers",
        "4. Remove Headers",
        "5. Help",
        "6. Exit"
    ]
    cprint("Select an option to get started:", "red")
    print("")
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
    cprint("\nAvailable headers:", "cyan")
    for idx, header in enumerate(headers, start=1):
        if header == current_header:
            cprint(f"  {idx}. {header} (current)", "green")
        else:
            cprint(f"  {idx}. {header}", "yellow")
    return True

def add_ascii_header():
    global header_counter
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        file_path = colored_input("Enter the full file path of the ASCII art file or type 'back' to return to the main menu: ", "yellow")
        if file_path == 'back':
            return
        if os.path.isfile(file_path):
            default_header_name = f"head_{header_counter:02}.txt"
            header_counter += 1
            
            ascii_art_file = file_path
            cprint(f"File set to: {ascii_art_file}", "green")
            
            ensure_headers_directory()
            new_header_path = os.path.join(headers_directory, default_header_name)
            shutil.copy(file_path, new_header_path)
            
            while True:
                rename_choice = colored_input("Do you want to rename the file? (y/n): ", "yellow")
                if rename_choice == 'y':
                    new_name = colored_input("Enter new name (without extension): ", "yellow")
                    new_header_path = os.path.join(headers_directory, f"{new_name}.txt")
                    os.rename(os.path.join(headers_directory, default_header_name), new_header_path)
                    cprint(f"File renamed to: {new_name}.txt", "green")
                    break
                elif rename_choice == 'n':
                    cprint(f"File saved as: {default_header_name}", "green")
                    break
                else:
                    cprint("Invalid input. Please enter 'y' or 'n'.", "red")
            time.sleep(2)  # Delay to show confirmation message
            backup_initial_bashrc()  # Backup .bashrc after the first header is added
            break
        else:
            cprint("Invalid file path. Please enter a valid file path.", "red")
        time.sleep(2)  # Add delay to allow the user to read the confirmation message

def update_header():
    global current_header
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    if not display_header_list():
        time.sleep(2)
        return
    
    headers = list_headers()
    try:
        header_index = int(colored_input("Enter the index of the header to set as current: ", "yellow")) - 1
        header_name = headers[header_index]
        header_path = os.path.join(headers_directory, header_name)
        if os.path.isfile(header_path):
            try:
                with open(header_path, 'r') as file:
                    lines = file.readlines()
                
                with open(os.path.expanduser("~/.bashrc"), 'r') as bashrc_file:
                    bashrc_lines = bashrc_file.readlines()
                
                with open(os.path.expanduser("~/.bashrc"), 'w') as bashrc:
                    added_header = False
                    for line in bashrc_lines:
                        if marker in line:
                            added_header = True
                            bashrc.write(line)
                            for ascii_line in lines:
                                bashrc.write(f'echo "{ascii_line.rstrip()}"\n')
                            bashrc.write(f"\n# === End of ASCIIStart modifications ===\n")
                        else:
                            bashrc.write(line)
                    
                    if not added_header:
                        bashrc.write(f"\n{marker}\n")
                        for ascii_line in lines:
                            bashrc.write(f'echo "{ascii_line.rstrip()}"\n')
                        bashrc.write(f"\n# === End of ASCIIStart modifications ===\n")
                    
                current_header = header_name
                cprint(f"\n{header_name} set as the current header and added to .bashrc.", "green")
            except Exception as e:
                cprint(f"An error occurred: {e}", "red")
        else:
            cprint("Invalid header index. Please enter a valid index.", "red")
    except ValueError:
        cprint("Invalid input. Please enter a valid index number.", "red")
    time.sleep(2)  # Add delay to allow the user to read the confirmation message

def edit_headers():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    if not display_header_list():
        time.sleep(2)
        return
    
    headers = list_headers()
    try:
        header_index = int(colored_input("Enter the index of the header to edit: ", "yellow")) - 1
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
                cprint("No available text editor found. Please install a text editor (e.g., nano, vim, gedit, notepad, code).", "red")
            else:
                cprint(f"\nEdits to {header_name} are saved.", "green")
        else:
            cprint("Invalid header index. Please enter a valid index.", "red")
    except ValueError:
        cprint("Invalid input. Please enter a valid index number.", "red")
    time.sleep(2)  # Add delay to allow the user to read the confirmation message

def remove_headers():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    if not display_header_list():
        time.sleep(2)
        return
    
    headers = list_headers()
    try:
        header_index = int(colored_input("Enter the index of the header to remove: ", "yellow")) - 1
        header_name = headers[header_index]
        header_path = os.path.join(headers_directory, header_name)
        
        # Check if the selected header is currently set in .bashrc
        current_header_in_bashrc = get_current_header_in_bashrc()
        
        if header_name == current_header_in_bashrc:
            try:
                restore_initial_bashrc()
            except Exception as e:
                cprint(f"Error restoring initial .bashrc backup: {e}", "red")
                time.sleep(2)
                return
        
        # Remove the header file
        if os.path.isfile(header_path):
            try:
                os.remove(header_path)
                cprint(f"\n{header_name} has been removed from Headers directory.", "green")
            except Exception as e:
                cprint(f"Error removing {header_name} from Headers directory: {e}", "red")
        else:
            cprint("Invalid header index. Please enter a valid index.", "red")
            time.sleep(2)
            return
        
        # Remove the header from .bashrc if it's currently set
        if header_name == current_header_in_bashrc:
            try:
                with open(os.path.expanduser("~/.bashrc"), 'r') as bashrc_file:
                    lines = bashrc_file.readlines()
                
                with open(os.path.expanduser("~/.bashrc"), 'w') as bashrc_file:
                    in_marker_block = False
                    for line in lines:
                        if marker in line:
                            in_marker_block = True
                        if in_marker_block and "# === End of ASCIIStart modifications ===" in line:
                            in_marker_block = False
                        if in_marker_block and line.strip().startswith('echo "'):
                            # Replace echo lines with empty lines
                            bashrc_file.write("\n")
                        else:
                            bashrc_file.write(line)
                
                cprint(f"{header_name} has been removed from .bashrc as well.", "yellow")
                
            except Exception as e:
                cprint(f"Error removing {header_name} from .bashrc: {e}", "red")
        
    except ValueError:
        cprint("Invalid input. Please enter a valid index number.", "red")
    time.sleep(2)  # Add delay to allow the user to read the confirmation message

def display_help():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    help_text = """
Help - ASCII Header Manager

1. Add ASCII Header:
    - Allows you to add a new ASCII header from a file.
    - You can choose to rename the saved file.

2. Update Header:
    - Sets a selected header as the current header and adds it to .bashrc.
    - Each line is prefixed with echo " and suffixed with ".
    - Includes a comment tracker for easier removal from .bashrc.

3. Edit Headers:
    - Opens the selected header file in a text editor for editing.
    - Requires a text editor installed (e.g., nano, vim, gedit, notepad, code).

4. Remove Headers:
    - Deletes the selected header file.

5. Help:
    - Displays this help page with basic commands and usage of the program.

6. Exit:
    - Closes the program.

Footer text: Buy me a coffee
    """
    cprint(help_text, "yellow")

def backup_initial_bashrc():
    try:
        if not os.path.exists(initial_bashrc_backup):
            shutil.copy(os.path.expanduser("~/.bashrc"), initial_bashrc_backup)
    except Exception as e:
        cprint(f"Error backing up initial .bashrc: {e}", "red")

def restore_initial_bashrc():
    try:
        with open(initial_bashrc_backup, 'r') as backup_file:
            backup_content = backup_file.read()
        
        with open(os.path.expanduser("~/.bashrc"), 'w') as bashrc_file:
            bashrc_file.write(backup_content)
    except Exception as e:
        cprint(f"Error restoring initial .bashrc backup: {e}", "red")
        raise  # Re-raise the exception to handle it in the caller

def get_current_header_in_bashrc():
    try:
        with open(os.path.expanduser("~/.bashrc"), 'r') as bashrc_file:
            for line in bashrc_file:
                if marker in line:
                    # Find the next line to determine the current header
                    next_line = next(bashrc_file).strip()
                    if next_line.startswith('echo "') and next_line.endswith('"'):
                        return next_line[6:-1].strip()  # Extract header name from echo line
    except Exception as e:
        cprint(f"Error reading .bashrc: {e}", "red")
    return "None"

if __name__ == "__main__":
    ensure_headers_directory()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        display_options()
        choice = colored_input("\nEnter your choice: ", "yellow")
        
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
            colored_input("\nPress Enter to return to the main menu: ", "yellow")
        
        elif choice == '6' or choice == 'exit':
            cprint("Exiting the program. Goodbye!", "yellow")
            break
        
        else:
            cprint("Invalid choice. Please enter a number from 1 to 6 or 'exit'.", "red")
            time.sleep(2)  # Add delay to allow the user to read the error message
