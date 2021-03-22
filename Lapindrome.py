for _ in range(int(input())):
    string = input()
    if len(string)%2==0:
        
        s1 = string[:len(string)//2]
        s2 = string[len(string)//2:len(string)]
    else:
        index = len(string)//2
        index2 = index+1
        s1 = string[:index]
        s2 = string[index2:]
    
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    
    out1 = str(l1)
    out2 = str(l2)
    
    if (out1==out2):
        print("YES")
    else:
        print("NO")