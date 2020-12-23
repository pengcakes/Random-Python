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

# for i,x in enumerate(var):
#     #print(i,x,paren_count)
#
#     if x == "(":
#         to_remove.append(i)
#         paren_count+=1
#     if x == ")":
#         paren_count-=1
#     if paren_count > 0:
#         to_remove.append(i)
#
#
# print(to_remove)
#
# print("".join(var))

# def move_zeros(array):
#     new=[]
#     zeros=0
#     for x in array:
#         if x==0  and x is not False:
#             zeros+=1
#         else:
#             new.append(x)
#     for x in range(zeros):
#         new.append(0)
#
#     return new
#
# def move_zeros1(array):
#     return sorted(array, key=lambda x: x == 0 and x is not False)
#
#
#
# print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
#
# corr = ['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# print(move_zeros([0,1,None,2,False,1,0]))
# # [1, None, 2, False, 1, 0, 0]
#
# corr == move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
#
#
# test=[]
# test.append(False)
# test.append(1)
# test.append(True)
# print(type(False))
#
# x=False
#
# if x==0  and (isinstance(x, int) or isinstance(x, float)):
#     print("yes")

def digital_root(n):
    separate = list(str(n))
    print(separate)
    if len(separate) == 1:
        return separate[0]
    else:
        to_int = [int(x) for x in separate]
        return digital_root(sum(to_int))



print(digital_root(16))
