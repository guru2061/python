a=input("enter the user id ")
#b=input("enter the password")
def password():
    b=list(map(str,input("enter the password ")))
    v,k,h=0,0,0;
    for j in b:
        if(j.isupper()):
            v+=1
        if(j.islower()):
            k+=1
        if(j.isdigit()):
            h+=1
    if((v and k and h)>0):
        print("valid password")
    else:
        print("invalid")
for i in range(len(a)):
    if(a[i]=='@'):
        d=a[i]
    if(a[i]=='.'):
        c=a[i]
if(d>c):
    print("email id is verified")
    password()
else:
    print("email id is not valid")
