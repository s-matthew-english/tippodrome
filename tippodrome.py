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
    
    trial = float(sys.argv[1])

    operand = float(sys.argv[2])

    candidrome = trial + (trial * 0.15)

    print(candidrome)
    candidrome = round(candidrome, 2)
 
    # check whether we have a Palindrome
    while not isPalindrome(candidrome):
        candidrome = candidrome + (0.01 * operand)
        candidrome = round(candidrome, 2)  
        print(candidrome)

    if isPalindrome(candidrome):
        print( "It's a Palindrome! " + str(candidrome) )
    
