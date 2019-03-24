"""
===================   TASK 2   ====================
* Name: Most Frequent Letter
*
* Write a script that takes the stirng as user
* input and displays which letter has the most
* occurences and how many. If two or more letters
* have the same number of occurences print any.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
===================================================
"""
string=str(input("Unesite string: "))

velika_slova=string.upper()

abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ponavljanje=0

for i in range(len(abc)):
    br=0
    for j in range(len(velika_slova)):
        if abeceda[i]==velika_slova[j]:
            br+=1
    if br>ponavljanje:
        naj_pon=abeceda[i]
        ponavljanje=br

def main():

    najvise_ponavljanja = naj_pon
    print("Najvise ponavljanja ima slovo: ", najvise_ponavljanja, " ,broj ponavljanja:", ponavljanje)

main()
