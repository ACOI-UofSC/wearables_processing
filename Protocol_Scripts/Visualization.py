
import warnings
import glob
import os
from matplotlib import pyplot as plt

warnings.filterwarnings("ignore")
pa_dir="V:/ACOI/R01 - W4K/3_PA protocol/1_Participants/"
participants=glob.glob(pa_dir+"[0-9][0-9][0-9][0-9]")
participants[0][len(pa_dir):len(pa_dir)+4]
cur=1
for participant in participants:

    p_id=participant[len(pa_dir):len(pa_dir)+4]
    if int(p_id)>2678:

        fitbit_file=pa_dir+f"{p_id}/Fitbit data/Batch data/"
        if os.path.exists(fitbit_file):
            ENMO_dir=pa_dir+f"{p_id}/{p_id}_ENMO_fig.png"
            img = plt.imread(ENMO_dir)
            plt.imshow(img)
            plt.title(p_id)
            plt.show(block=True)
    cur+=1