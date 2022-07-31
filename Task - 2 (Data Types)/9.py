#Task-9

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
aset = set(map(int, input().split()))
b = int(input())
bset = set(map(int, input().split()))

adef = aset.difference(bset)
bdef = bset.difference(aset)

result = adef.union(bdef)

for i in sorted(list(result)):
    print(i)
