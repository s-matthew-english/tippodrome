import sys

# This method determines whether or not the number is a Palindrome
def isPalindrome(x):
    x = '{:.2f}'.format(x).replace('.','')
    a, z = 0, len(x) - 1
    while a < z:
        if x[a] != x[z]:
            return False
        a += 1
        z -= 1
    return True

if '__main__' == __name__:

    original = float(sys.argv[1])

    operand = float(sys.argv[2])

    tip = float(sys.argv[3])

    candidrome = original + (original * tip)

    print(candidrome)
    candidrome = round(candidrome, 2)
 
    # check whether we have a Palindrome
    while not isPalindrome(candidrome):
        candidrome = candidrome + (0.01 * operand)
        candidrome = round(candidrome, 2)  
        print(candidrome)

    if isPalindrome(candidrome):
        result = candidrome - original
        print( "It's a Palindrome!\n" + str(result) + " + " + str(original) + " = " + str(candidrome) )
    
