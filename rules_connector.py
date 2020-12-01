import Alpha_rule
import Gamma_rule
import Delta_rule
import Beta_rule


def is_satisfiable(tab):  # Checking satisfiability of final formula.
    is_not = False
    is_not_in_all = 0
    for i in tab:
        for j in range(len(i)):
            for z in range(j+1, len(i)):
                if len(i) > 1 and (i[j] == i[z][0:-1] or i[j][0:-1] == i[z]):
                    is_not = True
        if is_not:
            is_not_in_all += 1
        is_not=False
    if is_not_in_all == len(tab):
        return "UNSATISFIABLE"
    else:
        return "SATISFIABLE"

# Input from the user.
infix = input("Your formula goes here (in postfix): ")

# Constant needed using MTS, declared from the beginning.
constants_tab = [i for i in input('Constants declaration (split by spaces: ').split()]  
print(end='\n')
infix_tab = infix.split()  # Input splitted to list.


used_dict = {}  # Dictionary of used constant: [formula, ...].
new_general_tab = [[infix_tab]]  # Main tab for our satisfiability.
stopping_rule = 0
branch_limit = 25

for i in new_general_tab:
    while True:
        stopping_rule = aplha_rules(i[0], i, stopping_rule)
        stopping_rule = beta_rules(i[0], i, stopping_rule, new_general_tab)
        stopping_rule = gamma_rules(i[0], i, constants_tab, used_dict, stopping_rule)
        stopping_rule = delta_rules(i[0], i, constants_tab, used_dict, stopping_rule)
        if stopping_rule >= branch_limit:
            break
    stopping_rule = 0
    print('Branch ready: ', new_general_tab, end='\n')

print(end='\n')
print('RESULTS: ')
for i in new_general_tab:
    print('Leaf:', i)

print(new_general_tab)

print('Satisfiability: ', is_satisfiable(new_general_tab))
