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


# import matplotlib
# matplotlib.use('Qt5Agg')
# # This should be done before `import matplotlib.pyplot`
# # 'Qt4Agg' for PyQt4 or PySide, 'Qt5Agg' for PyQt5
# import matplotlib.pyplot as plt
# import numpy as np
#
# t = np.linspace(0, 20, 500)
# plt.plot(t, np.sin(t))
# plt.show()

bruh= 'test(words)'#'hello example (words(more words) here) something'
var = [char for char in bruh]
to_remove=[]
paren_count=0


for i,x in enumerate(var):
    #print(i,x,paren_count)

    if x == "(":
        to_remove.append(i)
        paren_count+=1
    if x == ")":
        paren_count-=1
    if paren_count > 0:
        to_remove.append(i)


print(to_remove)

print("".join(var))
