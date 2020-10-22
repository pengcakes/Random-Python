# BRUH X 12

# def remove_parentheses(s):
#     split = [char for char in s]
#     temp = list(split)
#
#     tracker=0 # delete or not
#     kill_me=0 # matches indexes...
#     for char in temp:
#         print(tracker)
#         print(temp[kill_me])
#         if char == "(":
#             tracker+=1
#         if char == ")":
#             print("bruh")
#             tracker-=1
#             split.pop(kill_me)
#             kill_me-=1
#         if tracker > 0:
#             split.pop(kill_me)
#             kill_me-=1
#
#         kill_me+=1
#     return "".join(split)


def not_braindead(s):
    characters = [char for char in s]
    new=[]
    paren_count=0

    for x in characters:
        print(x, paren_count)
        if x == "(":
            paren_count+=1
        elif x == ")":
            paren_count-=1
        elif paren_count == 0:
            new.append(x)

    return "".join(new)

""" Actual Regex """

def remove_parentheses(s):
    while (t := re.sub(r'\([^()]*\)', '', s)) != s:
        s = t
    return s

"""
sorted()

I'll state the obvious up front: sorted() returns a list of sorted elements and if we want to sort in a particular way or if we want to sort a complex list of elements (e.g. nested lists or a list of tuples) we can invoke the key argument.

Lambda is a one time use function used to sort a list.

adder_lambda = lambda parameter1,parameter2: parameter1+parameter2
def adder_regular(parameter1, parameter2): return parameter1+parameter2

"""

def move_zeros(array):
    new=[]
    zeros=0
    for x in array:
        if x==0  and x is not False:
            zeros+=1
        else:
            new.append(x)
    for x in range(zeros):
        new.append(0)

    return new

def move_zeros1(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)


if __name__ == "__main__":
    import re
    # print(remove_parentheses("example(unwanted thing)example"))
    # print(remove_parentheses("a(b(c))"))
    # print(remove_parentheses("hello example (words(more words) here) something"))
    # print(remove_parentheses("(first group) (second group) (third group)"))
    # print(not_braindead("hello example (words(more words) here) something"))
