"""
===================   TASK 5   ====================
* Name: Average Value
*
* Write a function `averageval` that will take a
* integer list as an argument and return the 
* average value of the list elements.  
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""
def averageval(listt):

    summ = 0
    for el in listt:
        summ += int(el)
    a = 0
    for el in listt:
        a += 1
    return summ / a


def main():
    print(averageval([2, 8, 16]))


main()