#Task-3

if __name__ == '__main__':
    result =[]
    scorelist = []
    
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        result+=[[name,score]]
        scorelist+=[score]
    
    b=sorted(list(set(scorelist)))[1] 
    
    for a,c in sorted(result):
        if c==b:
            print(a)
