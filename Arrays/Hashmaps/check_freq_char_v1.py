# checking freq in strings 


def freq(s, k):
    count = 0 
    for ele in s:
         if ele == k:
            count += 1
    return count

s = "abcadabeaafac"
k = "a"
res = freq(s, k)

print(f"frequency of {k} in {res}")