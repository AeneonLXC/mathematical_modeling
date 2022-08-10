import numpy as np
from numpy import shape
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import numpy as pd
import matplotlib.pyplot as plt
A12 = np.load("npy/A12.npy")
print(shape(A12))
print(A12)
print(A12[299, 0])

plt.plot([1.4, 3.5, 6.9, 19.9, 44.5], lw=3, label='A12 - CH3CH2OH')
plt.plot([0.13606033, 3.2357593, 8.40198, 22.619238, 47.20208], lw=3, label='A12 - CH3CH2OH-BP')
# plt.plot(data_test[100:200, 4], out[100:200], lw=3, label='B')
# plt.plot(data_test[200:300, 4], out[200:300], lw=3, label='C')
# plt.plot(data_test[300:400, 4], out[300:400], lw=3, label='D')
plt.xlabel('var')
plt.ylabel('CH3CH2OH%')
plt.legend()
plt.savefig("./img/BPA12.jpg")
plt.show()