import os
import time
import subprocess

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""
:::::::. :::::::..    :::.  .::    .   .::::::     :::::::.      ...   :::::::::::::::         ...       :::.   :::::::-.  .,:::::: :::::::..   
 ;;;'';;';;;;``;;;;   ;;`;; ';;,  ;;  ;;;' ;;;      ;;;'';;'  .;;;;;;;.;;;;;;;;'''';;;      .;;;;;;;.    ;;`;;   ;;,   `';,;;;;'''' ;;;;``;;;;  
 [[[__[[\.[[[,/[[['  ,[[ '[[,'[[, [[, [['  [[[      [[[__[[\.,[[     \[[,   [[     [[[     ,[[     \[[, ,[[ '[[, `[[     [[ [[cccc   [[[,/[[['  
 $$""""Y$$$$$$$$c   c$$$cc$$$c Y$c$$$c$P   $$'      $$""""Y$$$$$,     $$$   $$     $$'     $$$,     $$$c$$$cc$$$c $$,    $$ $$""""   $$$$$$c    
_88o,,od8P888b "88bo,888   888, "88"888   o88oo,.___88o,,od8P"888,_ _,88P   88,   o88oo,.__"888,_ _,88P 888   888,888_,o8P' 888oo,__ 888b "88bo,
""YUMMMP" MMMM   "W" YMM   ""`   "M "M"   """"YUMMM""YUMMMP"   "YMMMMMP"    MMM   """"YUMMM  "YMMMMMP"  YMM   ""` MMMMP"`   """"YUMMMMMMM   "W" 
                                             
""")
    # Loading animation
    print("\nLoading: ", end="")
    for _ in range(20):  # Create a loading bar of 20 steps
        print("|", end="", flush=True)
        time.sleep(0.25)
    print("\n")
    
    # Prompt user for the script path
    print("Please paste the full path to the BrawlBot Python script.")
    script_path = input("Path: ").strip()
    
    # Check if the provided path is valid
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
    if os.name == 'nt':  # Windows
        subprocess.Popen(["start", "cmd", "/k", f"python {script_path}"], shell=True)
    else:  # Unix-like systems (Linux, macOS)
        subprocess.Popen(["xterm", "-e", f"python3 {script_path}"], start_new_session=True)
    print("A new terminal has been opened to run the BrawlBot Loader.")
    time.sleep(2)

if __name__ == "__main__":
    if "new_terminal" not in os.environ:
        # Set environment variable and open in new terminal
        os.environ["new_terminal"] = "1"
        open_in_new_terminal()
    else:
        main()