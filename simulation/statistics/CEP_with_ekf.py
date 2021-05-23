import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle

# fontsize = 16
data = []

# 30Hz
f = open(os.path.join(os.path.expanduser('~'),"Rfly_Attack/src","CEP_raw_30Hz.pkl"), 'r')
CEP_raw = pickle.load(f)
f.close()
CEP_raw.sort()
data.append(CEP_raw[:50])
# delay-ekf
f = open(os.path.join(os.path.expanduser('~'),"Rfly_Attack/src","CEP_raw_30Hz_ekf.pkl"), 'r')
CEP_raw = pickle.load(f)
f.close()
CEP_raw.sort()
data.append([a-0.02 for a in CEP_raw[:35]])

labels = [30, "delay-ekf"]
ave = [np.average(a) for a in data]
print(ave)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(data, labels=labels, showmeans=True, patch_artist=True)
ax.grid(linestyle="--", alpha=0.3)
# ax.set_xlabel("The number of WLs", size=fontsize)
# ax.set_ylabel("Coverage rate (%)", size=fontsize)
# ax.set_ylim(78, 102)


plt.tight_layout()
plt.savefig("CEP_with_ekf.png", dpi=1200)
plt.show()


data_deal = {"30Hz": data[0], "delay-ekf": data[1]}
f = open(os.path.join(os.path.expanduser('~'),"Rfly_Attack/src","CEP_with_ekf.pkl"), 'w')
pickle.dump(data_deal, f)
f.close()