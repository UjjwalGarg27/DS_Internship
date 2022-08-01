#Task-14

def merge_the_tools(string, k):
    # your code goes here
    t = []
    tlen = 0
    for item in string:
        tlen += 1
        if item not in t:
            t.append(item)
        if tlen == k:
            print (''.join(t))
            t = []
            tlen = 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
