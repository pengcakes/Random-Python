# def func(x):
#    return x + 1
#
# def test_answer():
#    assert func(3) == 5
#

# import nose
# nose.main()

from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Put a real number in")

    if r < 0:
        raise ValueError("R != negative number")

    return pi*(r**2)


if __name__ == "__main__":
    # testfunc
    radii=[2,3,-1,2+5j,True,"bottom text"]
    message = "Area of circiles with r = {radius} is {area}"

    for r in radii:
        A = circle_area(r)
        print(message.format(radius=r, area =A) )
