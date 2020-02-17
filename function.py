def s():
    print("1.go to the college")
    print("2.go on vacation")
    print("3.take rest")
    print("4.play quit")
    print("q.quit")
a=input()
if(a=='1' or a=='2' or a=='3' or a=='4'):
    while(a=='1' or a=='2' or a=='3' or a=='4'):
        s()
        a=input()
if(a=='q'):
    print("quit")
    
