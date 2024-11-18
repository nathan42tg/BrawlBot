import os
import time
import subprocess

def open_main_py():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, 'main.py')

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"\nContent of 'main.py':\n{content}")
    except FileNotFoundError:
        print(f"Error: The file 'main.py' does not exist in the directory: {current_dir}")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""
 ___                   _  ___        _    _                _           
| . > _ _  ___  _ _ _ | || . > ___ _| |_ | |   ___  ___  _| | ___  _ _ 
| . \| '_><_> || | | || || . \/ . \ | |  | |_ / . \<_> |/ . |/ ._>| '_>
|___/|_|  <___||__/_/ |_||___/\___/ |_|  |___|\___/<___|\___|\___.|_|  
                                             
""")
    print("\nLoading: ", end="")
    for _ in range(20):
        print("|", end="", flush=True)
        time.sleep(0.25)
    print("\n")
    
    open_main_py()
    
    print("Please paste the full path to the BrawlBot Python script.")
    script_path = input("Path: ").strip()
    
    if not os.path.isfile(script_path):
        print("Error: The path provided does not point to a valid file. Closing . . .")
        time.sleep(2)
        return
    
    while True:
        choice = input("Do you want to launch BrawlBot? (y/n): ").strip().lower()
        if choice == 'y':
            os.system(f'python "{script_path}"')
            break
        elif choice == 'n':
            print("Closing . . .")
            time.sleep(1)
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

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
        open_in_new_terminal()
    else:
        main()
