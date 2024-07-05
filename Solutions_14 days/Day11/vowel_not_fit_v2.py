# all vowel in string
def all_vowels(string):
    vowels = 'aeiou'  
    for char in string:
        if char not in vowels:
            return False
    return True

# no vowel
def no_vowels(string):
    vowels = 'aeiou'  # Set of vowels (both lowercase and uppercase)
    for char in string:
        if char in vowels:
            return False
    return True


# all sub_strings of string
def all_sub_strings(s):
    sub_str = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str.append(s[i:j+1])
    return sub_str

# Meet condition 
def solve(arr):

    ans = []

    for ele in arr:
        n = len(ele)
        mid = n // 2

        if n > 2:
            # print(ele)
            if n % 2 == 0:
                first = ele[:mid-1]
                middle = ele[mid-1:mid+1]
                last = ele[mid+1:]
                # print(f"first: {first}, middle: {middle}, last: {last}")
            else:
                first = ele[:mid]
                middle = ele[mid:mid+1]
                last = ele[mid+1:]
                # print(f"first: {first}, middle: {middle}, last: {last}")

            if no_vowels(middle) and all_vowels(first) and all_vowels(last):
                ans.append(ele)
    return ans

def main():
    
    sub1 = all_sub_strings("abezi")
    sub2 = all_sub_strings("beufiazoet")
    sub3 = all_sub_strings("afezai")
    sub4 = all_sub_strings("affegihhu")
    
    print()
    print("List of substrings: ",sub1)
    print("number of substrings: ",len(sub1))
    print("Meeting condition: ",solve(sub1))
    print()
    print("List of substrings: ",sub2)
    print("number of substrings: ",len(sub2))
    print("Meeting condition: ",solve(sub2))
    print()
    print("List of substrings: ",sub3)
    print("number of substrings: ",len(sub3))
    print("Meeting condition: ",solve(sub3))
    print()
    print("List of substrings: ",sub4)
    print("number of substrings: ",len(sub4))
    print("Meeting condition: ",solve(sub4))



if __name__ == "__main__":
    main()