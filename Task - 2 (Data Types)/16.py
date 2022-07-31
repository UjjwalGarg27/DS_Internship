#Task-16

# Enter your code here. Read input from STDIN. Print output to STDOUT

len_set = int(input())
u = set(map(int, input().split()))
op_len = int(input())

for i in range(op_len):
    operation = input().split()
    if operation[0] == 'intersection_update':
        a = set(map(int, input().split()))
        u.intersection_update(a)
    elif operation[0] == 'update':
        a = set(map(int, input().split()))
        u.update(a)
    elif operation[0] == 'symmetric_difference_update':
        a = set(map(int, input().split()))
        u.symmetric_difference_update(a)
    elif operation[0] == 'difference_update':
        a = set(map(int, input().split()))
        u.difference_update(a)

print(sum(u))
