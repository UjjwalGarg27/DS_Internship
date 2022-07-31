#Task-5

if __name__ == '__main__':
    N = int(input())
    
    result = [];
    for i in range(0,N):
        ip = input().split();
        if ip[0] == "print":
            print(result)
        elif ip[0] == "insert":
            result.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            result.remove(int(ip[1]))
        elif ip[0] == "pop":
            result.pop();
        elif ip[0] == "append":
            result.append(int(ip[1]))
        elif ip[0] == "sort":
            result.sort();
        else:
            result.reverse();
