"""
===================   TASK 4   ====================
* Name: Can String Be Float
*
* Write a script that will take integer number as
* user input and return the product of digits. 
* The script should be able to handle incorrect
* input, as well as the negative integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def main():
    int_num = input("Unesite broj: ")

    dozvoljeni_karakteri = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in int_num:
        if i not in dozvoljeni_karakteri:
            print("Unos nije validan!")
            quit()

    product_of_dig = 1
    for dg in int_num:
        product_of_dig *= int(dg)
    print(product_of_dig)


main()