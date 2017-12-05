def bubble(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def quick(arr):
    if arr: return quick([x for x in arr if x < arr[0]]) + [x for x in arr if x == arr[0]] + quick([x for x in arr if x > arr[0]])
    return []

if __name__ == "__main__":

    import timeit

    print("TIMEIT")
    print("bubble : ", end = '')
    print(timeit.timeit("bubble([6,7,3,8,3,8,3,9,4,5,4,4,89,4,77,34,56,33,87,7,9,6,8,4])", setup = "from __main__ import bubble", number = 10))
    print("quick : ", end='')
    print(timeit.timeit("quick([6,7,3,8,3,8,3,9,4,5,4,4,89,4,77,34,56,33,87,7,9,6,8,4])", setup="from __main__ import quick", number=10))