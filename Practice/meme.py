"""
4/20/20

Takes normal text --> returns sarcastic

1. make single word meme
2. make phrases work
3. allow expections for nums and special chars
4. ???
5. Runtime
6. Make application
7. Option to auto copy to clipboard

"""
import random


def change_word(word):
    var=[]
    for letter in word:
            if random.random() >=  0.5:
                var.append(letter.lower())
            else:
                var.append(letter.upper())

    word = "".join(var)
    return word


def meme_it(input):
    phrase, meme = input.split(), []

    for word in phrase:
        meme.append(change_word(word))

    meme=" ".join(meme)
    print(meme)
    return meme



if __name__ == "__main__":
    print("Input word:")
    word = input()
    meme_it(word)
