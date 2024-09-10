# freq checking using hashing 
def freq(arr, quries):
    # create a freq map of array
    freq_map = {}
    for ele in arr:
        if ele in freq_map:
            freq_map[ele] += 1
        else:
            freq_map[ele] = 1
    
    # create a list of seen freq
    seen = []
    for qurie in quries:
        if qurie in freq_map:
            seen.append(freq_map[qurie])
        else:
            seen.append(0)
    return seen

A = [1, 2, 1, 1, 4, 5, 6, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 8]
B = [1, 2, 4, 5, 6]

res = freq(A, B)
print(f"frequencies for {B} are {res}")