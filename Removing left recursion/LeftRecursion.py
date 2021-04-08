"""

The following Program is a Python Code for Removing Left Recursion.
@author="Shyam Makwana"

"""

# function for removing left Recursion


def rec(nonterm, transition):

    prod = transition[nonterm]
    prod1 = nonterm + "->"
    prod2 = nonterm + "'->"
    rec = list()
    nonRec = list()

    for i in prod:
        if nonterm == i[0]:
            rec.append(i)
        else:
            nonRec.append(i)

    if len(rec) == 0:
        return 0

    for j in nonRec:
        prod1 = prod1 + j + nonterm + "'"
        if(nonRec.index(j) != (len(nonRec)-1)):
            prod1 = prod1 + "|"

    for j in rec:
        prod2 = prod2 + j[1::] + nonterm + "'|"

    prod2 = prod2 + "^"
    return(prod1 + "$" + prod2)


def split_grammar(production):
    split_prod = production.split("->")
    nonterm = split_prod[0]
    temp = split_prod[1].split("|")
    transition[nonterm] = temp
    return nonterm, transition


def print_grammar(grammar):
    grammar = grammar.split("$")
    print(grammar[0])
    print(grammar[1])


###################   Starting of Code   ###################
n = int(input("\nEnter total number of productions : "))
char = '$'

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

    production = rec(nonterm, transition)
    if production != 0:
        print("\nProduction " + str(iter+1) + " has Left Recursion\n")
        print_grammar(production)
        production = production.split("$")
        production = production[0]
    else:
        print("\nProduction " + str(iter+1) + " doesn't have Left Recursion")
        production = temp_production

    production = production.split("$")
    production = production[0]
    split_grammar1 = production.split("->")
    char = split_grammar1[0]
    split_grammar1 = split_grammar1[1].split("|")
