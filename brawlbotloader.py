import os
import time
import subprocess

def run_loading_bar(duration=5, total_blocks=30):
    # Duration is in seconds, default is 5 seconds
    fill_char = '█'  # Character to represent filled part
    empty_char = '▒'  # Character to represent empty part

    print("\nLoading: ", end="")
    
    # Loop to simulate the loading bar progress
    for i in range(total_blocks + 1):  # +1 to show the fully completed bar
        filled_blocks = int(i)
        empty_blocks = total_blocks - filled_blocks
        progress_bar = fill_char * filled_blocks + empty_char * empty_blocks
        print(f"\r[{progress_bar}] {int(i / total_blocks * 100)}%", end="", flush=True)
        time.sleep(duration / total_blocks)  # Sleep to adjust the speed (5 seconds / total_blocks)
    
    print("\n")  # New line after the loading bar

def run_main_py():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, 'main.py')

    # Check if main.py exists in the current directory
    if os.path.isfile(file_path):
        print(f"Found 'main.py' in the current directory.")
        choice = input(f"Do you want to run 'main.py' from {current_dir}? (y/n): ").strip().lower()
        if choice == 'y':
            print(f"\nRunning 'main.py' from {current_dir}...")
            run_loading_bar()  # Fancy loading bar for 5 seconds
            subprocess.run(['python', file_path])  # Run the file directly
        elif choice == 'n':
            print("You chose not to run 'main.py'.")
        else:
            print("Invalid input. Exiting.")
            time.sleep(2)
    else:
        print(f"Error: The file 'main.py' does not exist in the directory: {current_dir}")
        time.sleep(2)  # Wait before prompting for the path

        # Prompt user for the full path to the script
        script_path = input("Please paste the full path to the 'main.py' Python script: ").strip()
        
        if os.path.isfile(script_path):
            print(f"Found 'main.py' at {script_path}.")
            choice = input(f"Do you want to run 'main.py' from {script_path}? (y/n): ").strip().lower()
            if choice == 'y':
                print(f"\nRunning 'main.py' from {script_path}...")
                run_loading_bar()  # Fancy loading bar for 5 seconds
                subprocess.run(['python', script_path])  # Run the user-provided file
            elif choice == 'n':
                print("You chose not to run 'main.py'.")
            else:
                print("Invalid input. Exiting.")
                time.sleep(2)
        else:
            print("Error: The path provided does not point to a valid file. Exiting . . .")
            time.sleep(2)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""
 ___                   _  ___        _    _                _           
| . > _ _  ___  _ _ _ | || . > ___ _| |_ | |   ___  ___  _| | ___  _ _ 
| . \| '_><_> || | | || || . \/ . \ | |  | |_ / . \<_> |/ . |/ ._>| '_>
|___/|_|  <___||__/_/ |_||___/\___/ |_|  |___|\___/<___|\___|\___.|_|  
                                             
""")
    # Call the fancy loading bar instead of a static one
    run_loading_bar(duration=5)  # Fancy loading bar for 5 seconds
    
    run_main_py()  # Run the function to execute 'main.py'

def open_in_new_terminal():
    script_path = os.path.abspath(__file__)
    if os.name == 'nt':
        subprocess.Popen(["start", "cmd", "/k", f"python {script_path}"], shell=True)
    else:
        subprocess.Popen(["xterm", "-e", f"python3 {script_path}"], start_new_session=True)
    print("A new terminal has been opened to run the BrawlBot Loader.")
    time.sleep(2)

if __name__ == "__main__":
    if "new_terminal" not in os.environ:
        os.environ["new_terminal"] = "1"
        open_in_new_terminal()  # Open a new terminal if not already done
    else:
        main()  # Run the main process
