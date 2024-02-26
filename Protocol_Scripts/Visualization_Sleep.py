import warnings
import glob
import os
from matplotlib import pyplot as plt

warnings.filterwarnings("ignore")
sleep_dir="V:/ACOI/R01 - W4K/1_Sleep Study/1_Participant Data/"
participants=glob.glob(sleep_dir+"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")
participants[0][len(sleep_dir):len(sleep_dir)+10]
cur=1
for participant in participants:

    p_id=participant[len(sleep_dir):len(sleep_dir)+10]
    if int(p_id)>2678:

        fitbit_file=sleep_dir+f"{p_id}/Fitbit/Batch Data/"
        if os.path.exists(fitbit_file):
            ENMO_dir_1=sleep_dir+f"{p_id}/{p_id}_ENMO_fig.png"
            ENMO_dir_2 = sleep_dir + f"{p_id}/{p_id}_ENMO.png"
            if os.path.isfile(ENMO_dir_1):
                img = plt.imread(ENMO_dir_1)
            elif os.path.isfile(ENMO_dir_2):
                img = plt.imread(ENMO_dir_2)
            plt.imshow(img)
            plt.title(p_id)
            plt.show(block=True)
    cur+=1