import glob
import tkinter as tk
from tkinter import filedialog
import os.path
import datetime
def find_garmin_processed():
    root = tk.Tk()
    root.winfo_toplevel().title("Select directories")
    root.withdraw()
    # Start of dialogue
    print("Please select the folder housing all the participant folders you wish to process")
    home_dir = filedialog.askdirectory()
    files = glob.glob(home_dir + "/[0-9][0-9][0-9][0-9]")
    print(f"List of participants: {files}")
    # Get path to V drive
    v_dir = "V:/R01 - W4K/3_PA protocol/"
    if not os.path.isdir(v_dir):
        v_dir = "V:/ACOI/R01 - W4K/3_PA protocol/"

    # Process all PA participants with Garmin
    participants_not_processed = []
    for file in files:
        participant = file[-4:]
        garmin_path = file+f"/Garmin data/"
        if os.path.exists(garmin_path):

            for filename in os.listdir(garmin_path):
                file_path = os.path.join(garmin_path, filename)
                # Check if the file is a regular file and its extension is not ".fit"
                if os.path.isfile(file_path) and not filename.endswith('.fit'):
                    modification_timestamp = os.path.getmtime(file_path)
                    modification_date = datetime.datetime.fromtimestamp(modification_timestamp).date()
                    comparison_date = datetime.date(2024, 2, 9)
                    if modification_date<comparison_date:
                        print(participant)
                        participants_not_processed.append(participant)




            else:
                print(f"No Garmin Files")

        else:
            print(f"No garmin path could not process {participant}")
            participants_not_processed.append(participant)
    print(participants_not_processed)
find_garmin_processed();