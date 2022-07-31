#Task-11

n = int(input())
s = set(map(int, input().split()))

operation = int(input())

for x in range(operation):
  op = input().split()
  if op[0] == "remove":
    s.remove(int(op[1]))
  elif op[0] == "discard":
    s.discard(int(op[1]))
  else:
    s.pop()
    
print(sum(s))
