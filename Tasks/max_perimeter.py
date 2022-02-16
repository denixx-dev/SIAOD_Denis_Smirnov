def max_perimeter(arr):
    new_arr = sorted(arr)
    i = len(new_arr)-3
    #for i in range(length-3, -1, -1):
    while i>=0:
        if new_arr[i] + new_arr[i+1]>new_arr[i+2]:
            return new_arr[i] + new_arr[i+1] + new_arr[i+2]
        i-=1
    return 0
 


n = int(input("enter length of the array\n"))
print()
arr = []
for i in range(n):
    arr.append(int(input()))

print(max_perimeter(arr))