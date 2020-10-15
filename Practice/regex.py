def remove_parentheses(s):
    split = [char for char in s]
    temp = list(split)

    tracker=0 # delete or not
    kill_me=0 # matches indexes...
    for char in temp:
        print(tracker)
        print(temp[kill_me])
        if char == "(":
            tracker+=1
        if char == ")":
            print("bruh")
            tracker-=1
            split.pop(kill_me)
            kill_me-=1
        if tracker > 0:
            split.pop(kill_me)
            kill_me-=1

        kill_me+=1
    return "".join(split)


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


if __name__ == "__main__":
    # print(remove_parentheses("example(unwanted thing)example"))
    # print(remove_parentheses("a(b(c))"))
    # print(remove_parentheses("hello example (words(more words) here) something"))
    # print(remove_parentheses("(first group) (second group) (third group)"))
    print(not_braindead("hello example (words(more words) here) something"))
