import os
import numpy as np
from coherence_length_analyser.lib.functions import round
import matplotlib
from  matplotlib import pyplot as plt

path = r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\converted_videos"


tmp = next(os.walk(path))[1]
folders = [os.path.abspath(os.path.join(path, x)) for x in tmp]
files = []

for item in folders:
    tmp = os.listdir(item)
    for item2 in tmp:
        if item2.endswith(".txt") is True:
            files.append(os.path.join(item, item2))

dic = {}
for item in files:
    with open(item, "r") as file:
        tmp = [x.split("\t") for x in file.read().split("\n")]
        for x in tmp:
            pos1 = x[2].find("(")
            pos2 = x[2].find(")")
            x[2] = x[2].replace(x[2][pos1:pos2+1], "").split()[-1]
            key = x[0] + "/" +x[1]
            tmp_value = dic.get(key)
            if tmp_value is not None:
                tmp_value.append(x[2])
                dic[key] = tmp_value
            else:
                dic[key] = [x[2]]

lis = []
for item in dic:
    window, filter = item.split("/")
    tmp = dic.get(item)

    temp = tmp.copy()
    temp = [float(x) for x in temp]
    temp = np.array(temp)
    tmp.append(str(round(temp.mean(),3)))
    tmp.append(str(round(temp.std(ddof=1),5)))
    tmp.insert(0, filter)
    tmp.insert(0, window)
    tmp = ','.join(tmp)
    lis.append(tmp)

string = '\n'.join(lis)
with open("window_filter.csv", "w") as file:
    file.write(string)

new_dic = {}
with open("window_filter.csv", "r") as file:
    tmp = [x.split(",") for x in file.read().split("\n")]
    for x in tmp:
        key = x[0] + "/" +x[1]
        tmp_value = new_dic.get(key)
        if tmp_value is not None:
            tmp_value.append(x[-2])
#            tmp_value.append(x[-1])
            new_dic[key] = tmp_value
        else:
            new_dic[key] = x[-2]#, x[-1]]

boxcar = [float(v) for k,v in new_dic.items() if 'Boxcar' in k]
gauss = [float(v) for k,v in new_dic.items() if 'Gauss' in k]
hanning = [float(v) for k,v in new_dic.items() if 'Hanning' in k]
hamming = [float(v) for k,v in new_dic.items() if 'Hamming' in k]
kaiser = [float(v) for k,v in new_dic.items() if 'Kaiser' in k]
slepian = [float(v) for k,v in new_dic.items() if 'Slepian' in k]
array = np.array([boxcar, gauss, hanning, hamming, kaiser, slepian])


windows = ["Boxcar", "Gaussian", "Hanning", "Hamming",
              "Kaiser", "Slepian"]
filters = ["w/o", "moving average", "savitzky-golay",
           "moving average and savitzky-golay", "median",
           "median  and savitzky-golay", "FFT", "FFT and savitzky-golay"]



fig, ax = plt.subplots() #fig,
im = ax.imshow(array)

# We want to show all ticks...
ax.set_xticks(np.arange(len(filters)))
ax.set_yticks(np.arange(len(windows)))
# ... and label them with the respective list entries
ax.set_xticklabels(filters)
ax.set_yticklabels(windows)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(windows)):
    for j in range(len(filters)):
        text = ax.text(j, i, array[i, j],
                       ha="center", va="center", color="black")
ax.set_title("Coherence Length in µm")
plt.show()
plt.savefig("compare_window_filter.png", dpi=600, bbox_inches = "tight")