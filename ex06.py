#Write a recursive function to print out the digits of a number in English. For example, if
#the number is 153, the output should be “One Five Three.” See the hint from the previous
#problem for help on how this might be done.

def digits_of_a_number_in_English(x):
    sve_cifre = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

    if x < 10:
        return sve_cifre[x]

    else:
        return digits_of_a_number_in_English(x//10) + " " + sve_cifre[x % 10]

x = abs(int(input("Unesi cijeli broj: ")))
print("Cifre broja na engleskom su: ", digits_of_a_number_in_English(x))