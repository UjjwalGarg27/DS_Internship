#Task-13

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
u1 = set(input().split())

b = int(input())
u2 = set(input().split())

u3 = u2.intersection(u1)

print(len(u3))
