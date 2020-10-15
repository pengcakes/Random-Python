# %matplotlib inline
# %conifg InlineBackend.figure_format = "svg"
#
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
#
# mpl.style.use('ggplot')
#
# x = np.linspace(0,10,500)
#
# x= 2*x


import matplotlib
matplotlib.use('Qt5Agg')
# This should be done before `import matplotlib.pyplot`
# 'Qt4Agg' for PyQt4 or PySide, 'Qt5Agg' for PyQt5
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 20, 500)
plt.plot(t, np.sin(t))
plt.show()

bruh= 'hello example something'
bruh2='hello example  something'

if bruh == bruh2 : print("True")
