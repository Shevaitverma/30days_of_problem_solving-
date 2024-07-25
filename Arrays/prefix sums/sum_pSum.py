# using p-smu method
def aum(arr, l, r):
    pass


# testing 
arr = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
quries = [[4,8], [3,7], [1,3], [0,4]]
# for each quries
for query in quries:
    l, r = query
    print(f"Sum of elements between indices {l} and {r}: {aum(arr, l, r)}")