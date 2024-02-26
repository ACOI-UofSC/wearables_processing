import os
import glob
participants = []


files=glob.glob("V:/ACOI/R01 - W4K/1_Sleep Study/1_Participant Data/751[0-9][0-9][0-9][0-9][0-9][0-9][0-9]")
directory = "Kubios Output"



for file in files:
    psg_folder = file + "/PSG/"
    path = os.path.join(psg_folder, directory)
    if not os.path.isdir(path):
        print("Creating path:", path)  # Debugging line
        os.makedirs(path, exist_ok=True)