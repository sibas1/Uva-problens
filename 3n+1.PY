b=int (input())
a=int (input())
res = 0;
while a<b:
    a =a +1
    cont = 1
    print ("w1")
    print (a)
    c=a;
    while c > 1:
        if c%2 == 0:
            c=c/2  
            print ("w2 si") 
            print (c) 
        else:
            c = c*3+1 
            print ("w2 no") 
            print (c) 
        cont = cont + 1
    if res<cont:
        print (cont)
        res=cont;
print (res)