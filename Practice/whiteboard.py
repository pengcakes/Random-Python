def func():
    print('pls')

def bruh(number):
    return number%2 == 0



""" O(n) """

def solutionN(number):
    if number <= 0:
        return 0

    sum_list=[]
    for x in range(0, number+1):
        if x%3==0 or x%5==0:
            sum_list.append(x)

    return sum(sum_list)

# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


def solution1(number):
    a3 = (number-1)//3
    a5 = (number-1)//5
    a15 = (number-1)//15
    result = (a3*(a3+1)//2)*3 + (a5*(a5+1)//2)*5 - (a15*(a15+1)//2)*15
    return result



if __name__ == "__main__":
    print(solutionN(1000))
