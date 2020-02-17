acc=70000
def withdrawn(a):
    global acc
    acc=acc-a
def deposit(g):
    global acc
    acc=acc+g
u=int(input("1.depost 2.withdraw "))
if(u==1):
    r=int(input("enter the amount "))
    deposit(r)
if(u==2):
     j=int(input("enter the amount "))
     withdrawn(j)
print("account balance ",acc)   
          
