## we have a palindrome given, we need to fin the all combinations of the string from the given palindrome and find palindrome from the combinations if the strings
##  eg: 'aba' -> combinations -> ['a', 'b', ab, aba, ba] -> now palindrome in the list -> ['a', 'b', aba]


debug = True
# to check palindrome
def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
def solve(s):
    # logic to make combination of substring
    combinations = []
    for i in range(len(s)):
        print(len(s))
        for j in range(i+1, len(s)+1):
                print("adding elements between ", i, j, " are ", s[i:j])
                combinations.append(s[i:j])
    # for debugging purposes
    if debug == True:
        print("unique combinations of the string: ",combinations)

    # chech anf store plaindrome in that substrings 
    palindromes = []
    for i in combinations:
         if isPalindrome(i):
             palindromes.append(i)
    if debug == True:
        print("Palindrome in the combinations: ",palindromes)
    
    return palindromes

# solve("abba")

def main():
    s = "a"
    palindromes = solve(s)
    print("palindromes in the combinations are ",palindromes)

if __name__ == "__main__":
     main()