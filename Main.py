import math

def product(a):
    d=1
    for i in a:
        d*=i
    return d    
        
def ex ():

    n = float(input("N: "))
    while(n<=0 or n>15):
        n = float(input())
    rows, cols = (n, n)

    a=[]

    for i in range((int)(rows)):          
         b =[]
         for j in range((int)(cols)):      
             b.append(int(input()))
         a.append(b)

    r=[]
    k=[]

    for i in a:
        r.append(product(i))


    for i in range ((int)(rows)):
        for j in range(i + 1, (int)(cols)):
            if(r[i] < r[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp

    print ("A: ", a)

    for i in range(0, len(r)):
        for j in range(i+1, len(r)):
            if r[i] > r[j]:
                temp = r[i]
                r[i] = r[j]
                r[j] = temp
 
    print ("R: ", r)

def name(a):
    b=''
    for i in a:
        if(i is not int):
            b=i
    return b      

def ex1 ():
    a=[]

    print ("Input: ")

    for i in range((int)(3)):          
         b =[]
         for j in range((int)(1)):      
             b.append(int(input()))
             b.append(str(input()))
         a.append(b)

    a.sort()
    a.reverse()

    print ("A: "+(str)(a))

    k=[]

    for i in a:   
        k.append((str)(name(i)))

    print ("K: "+ (str)(k))

    print ("\nChampion: "+ k[0])
    print ("2 & 3: "+ k[1]+" "+k[2])
    print ("1 & 2: "+k[0]+" "+k[1])        
        

def ex2 ():
    words = {}
    words1 = {}
    n = int(input("N: "))

    for i in range(n):
        w = input("W: ")
        w1 = input("W1: ")

        words[w] = w1
        #words1[w1] = w

    #dict(map(reversed, words.items()))
    words = dict(map(reversed, words.items()))
    key = input("Word: ")
    
    print("Result: "+(words.get(key)))
    
print ("N: ")
n = int(input())

match n:
        case 1:
            ex()
        case 2:
            ex1()
        case 3:
            ex2()
        case default:
            print ("Error")