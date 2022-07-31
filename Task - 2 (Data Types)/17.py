#Task-17

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

u = map(int, input().split())
u = sorted(u)

for i in range(len(u)):
    if(i != len(u)-1):
        if(u[i]!=u[i-1] and u[i]!=u[i+1]):
            print(u[i])
            break;
    else:
        print(u[i])
