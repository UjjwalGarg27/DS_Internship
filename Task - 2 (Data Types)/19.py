#Task-19

# Enter your code here. Read input from STDIN. Print output to STDOUT

u = set(input().split())
n = int(input())
result = True

for i in range(n):
    u2 = set(input().split())
    if not u2.issubset(u):
        result = False
    if len(u2) >= len(u):
        result = False

print(result)
