
# Python program to demonstrate
# selenium

# # import webdriver
# from selenium import webdriver
# # create webdriver object
# driver = webdriver.Firefox(executable_path=r"C:\Users\14\Documents\GeckoDriver\geckodriver.exe")
# # get google.co.in
# driver.get("https://google.com")


# chrome test - chrome is faster

# import webdriver
from selenium import webdriver
# create webdriver object
driver = webdriver.Chrome(r"C:\Users\14\Documents\ChromeDriver\chromedriver.exe")
# get google.co.in
driver.get("https://google.com")




def bruh(number):
    return number%2 == 0



""" O(n) """

def solutionN(number):
    if number <= 0:
        return 0

    sum_list=[]
    for x in range(0, int(number)+1):
        if x%3==0 or x%5==0:
            sum_list.append(x)

    return sum(sum_list)

def solutionN2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

""" O(1) """
def solution1(number):
    a3 = (number-1)//3
    a5 = (number-1)//5
    a15 = (number-1)//15
    result = (a3*(a3+1)//2)*3 + (a5*(a5+1)//2)*5 - (a15*(a15+1)//2)*15
    return result


""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

if __name__ == "__main__":
    start = time.time()
    print(solutionN(10000000))
    print(solutionN2(10000000))
    print(solution1(10000000))
    end = time.time()
    print(end - start)
