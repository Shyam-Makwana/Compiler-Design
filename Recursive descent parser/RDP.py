print("\nRecursive Desent Parsing For following grammar\n")
print("E->TE'\nE'->+TE'|^\nT->FT'\nT'->*FT'|^\nF->(E)|a\n")
global inp
inp = (input("Enter the string want to be checked : "))
global i
i=0
global flag
flag=0

def match(ch):
    global inp
    global i
    if(i>=len(inp)):
        return False
    elif(inp[i]==ch):
        return True
    else:
        return False

def F():
    global inp
    global i
    global flag

    if match('a'):
        i = i + 1
    elif match('('):
        i = i + 1
        E()
        if match(')'):
            i = i + 1
        else:
            flag=1
    else:
        flag=1

def Tdash():
    global i
    if match('*'):
        i+=1
        F()
        Tdash()

def T():
    F()
    Tdash()

def Edash():
    global i
    if match('+'):
        i+=1
        T()
        Edash()

def E():
    T()
    Edash()

E()
if len(inp)==i and flag==0:
    print("\n",inp,"is Valid String")
else:
    print("\n",inp,"is Invalid String")

