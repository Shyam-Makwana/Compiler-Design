"""

The following Program is a Python Code for Removing Left Factoring.
@auther="Shyam Makwana"

"""

#function for removing left Factoring
def fact(nonterm,transition):

    prod = transition[nonterm]
    prod1 = nonterm + "->"
    prod2 = nonterm + "'->"

    minn = 1000
    comp = prod[0]
    for i in prod:
        count=0
        for j in i:
            if j!=comp[i.index(j)]:
                minn=min(minn,count)
            count = count+1      

    if minn==0:
        return 0

    count=0
    for i in comp:
        if count<minn:
            prod1 = prod1 + i
            count = count + 1
            
    prod1 = prod1 + nonterm + "'"

    for i in prod:
        count = 0
        for j in i:
            count = count + 1
            if count>minn:
                prod2 = prod2 + j
            
        if(prod.index(i) != (len(prod)-1)):
            prod2 = prod2 + "|"

    return(prod1 + "$" + prod2)

def split_grammar(production):
    split_prod = production.split("->")
    nonterm=split_prod[0]
    temp = split_prod[1].split("|")
    transition[nonterm]=temp
    return nonterm,transition

def print_grammar(grammar):
    grammar = grammar.split("$")
    print(grammar[0])
    print(grammar[1])

###################   Starting of Code   ###################
n = int(input("\nEnter total number of productions : "))
char = '$'
transition = dict()

for iter in range(n):
    production = input("\nEnter Production " + str(iter+1) + " : ")
    temp_production = production
    temp_list = list()
    transition = dict()
    nonterm, transition = split_grammar(production)

    for j in transition[nonterm]:
        if j[0] == char:
            for k in split_grammar1:
                temp_string = k + j[1::]
                temp_list.append(temp_string)
        else:
            temp_list.append(j)
        
    transition[nonterm] = temp_list
    production = fact(nonterm, transition)

    if production != 0:
        print("\nProduction " + str(iter+1) + " has Left Factoring\n")
        print_grammar(production)
        production = production.split("$")
        production = production[0]
    else:
        print("\nProduction " + str(iter+1) + " doesn't have Left Factoring")
        production = temp_production

    production = production.split("$")
    production = production[0]
    split_grammar1 = production.split("->")
    char = split_grammar1[0]
    split_grammar1 = split_grammar1[1].split("|")
        

