n1 = int(input("dati primul numar mai mic ca 32000 "))
n2 = int(input("dati a doilea numar mai mic ca 32000 "))
n3 = int(input("dati a 3 numar mai mic ca 32000 "))
if(n1<32000 and n2<32000 and n3<32000):
    if(n1<n2+n3)and(n2<n3+n1)and(n3<n2+n1):
    
        print("DA")
    else:
        print("NU")