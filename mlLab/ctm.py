import numpy as np
import statistics as st
user =[1,2,3,4,5,6,7,8,9,12,45,64]

mean = np.mean(user)
med  = np.median(user)
mode = st.mode(user)
var = np.var(user)
std = np.std(user)

print(f"Mean is {mean}\nMedian is {med}\nMode is {mode}\nVariance is {var}\nStandard Deviation is {std}")
