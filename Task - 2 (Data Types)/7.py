#Task-7

def average(array):
    # your code goes here
    arr_sum = sum(set(array))
    arr_len = len(set(array))
    result = arr_sum/arr_len
    return result;

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
