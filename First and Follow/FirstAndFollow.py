'''

    The following program is a Python code to generate First and Follow. 
    @author="Shyam Makwana"

'''

def find_first(string):

    first_grammar = set()
    if string in non_terminals:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_grammar2 = find_first(alternative)
            first_grammar = first_grammar |first_grammar2

    elif string in terminals:
        first_grammar = {string}

    elif string=='' or string=='^':
        first_grammar = {'^'}

    else:
        first_grammar2 = find_first(string[0])
        if '^' in first_grammar2:
            i = 1
            while '^' in first_grammar2:
                first_grammar = first_grammar | (first_grammar2 - {'^'})
                if string[i:] in terminals:
                    first_grammar = first_grammar | {string[i:]}
                    break
                elif string[i:] == '':
                    first_grammar = first_grammar | {'^'}
                    break
                first_grammar2 = find_first(string[i:])
                first_grammar = first_grammar | first_grammar2 - {'^'}
                i += 1
        else:
            first_grammar = first_grammar | first_grammar2
    return  first_grammar


def find_follow(nT):
    follow_grammar = set()
    prods = productions_dict.items()
    if nT==starting_symbol:
        follow_grammar = follow_grammar | {'$'}
    for nt,rhs in prods:
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_grammar = follow_grammar | find_follow(nt)
                    else:
                        follow_grammar2 = find_first(following_str)
                        if '^' in follow_grammar2:
                            follow_grammar = follow_grammar | follow_grammar2-{'^'}
                            follow_grammar = follow_grammar | find_follow(nt)
                        else:
                            follow_grammar = follow_grammar | follow_grammar2
    return follow_grammar

def split_grammar(production):
    split_prod = production.split("->")
    nonterm=split_prod[0]
    temp = split_prod[1].split("|")
    transition[nonterm]=temp
    return nonterm,transition

terminals = list()
non_terminals = list()

starting_symbol = input("Enter the starting symbol: ")

no_of_productions = int(input("Enter no of productions: "))

productions = []

print("Enter the productions:")
for _ in range(no_of_productions):
    temp=input()
    productions.append(temp)
    temp_list = list()
    transition = dict()
    nonterm, transition = split_grammar(temp)
    non_terminals.append(nonterm)
    for value in transition.values():
    # print(value)
        for val in value:
            for va in val:
                # print(va)
                if ((va.isupper()==False) and (va!='^')):
                    terminals.append(va)

# print(terminals)
# print(non_terminals)

productions_dict = {}

for nT in non_terminals:
    productions_dict[nT] = []

for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("|")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

# print(productions_dict)

FIRST = dict()
FOLLOW = dict()

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

# print("FIRST = ",FIRST)
# print("FOLLOW = ",FOLLOW)

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | find_first(non_terminal)


FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | find_follow(non_terminal)

print("\nFirst && Follow of following Grammar\n")

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal])))

