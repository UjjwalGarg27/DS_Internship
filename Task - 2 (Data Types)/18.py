#Task-18

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for _ in range(t):
    x = input()
    A = set(input().split())
    y = int(input())
    B = set(input().split())
    print(A.issubset(B))
