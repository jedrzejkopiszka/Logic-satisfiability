from copy import deepcopy


def delta_rules(infix_tab, general_tab, variables_tab, used_dict, stopping_rule):
    
    if infix_tab[-1] == 'EXISTS' or infix_tab[-1] == "∃":
        
        print('DELTA rule for EXISTS( ), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        copy_of_infix_tab = deepcopy(infix_tab)
        # Replacing old variables to newly generated
        copy_of_infix_tab = [chr(ord(variables_tab[-1])+1) if el == infix_tab[0] else el for el in copy_of_infix_tab] 
        copy_of_infix_tab.pop(0)  # Removing old variable from beginning
        variables_tab.append(chr(ord(variables_tab[-1])+1))  # Append tab of variables with new variable used in delta rule
        general_tab.remove(infix_tab)
        general_tab.append(copy_of_infix_tab)
        print("Branch after rule: ", general_tab)
        print(end='\n')

    elif (infix_tab[-2] == 'FORALL' or infix_tab[-2] == "∀") \
            and (infix_tab[-1] == "NOT" or infix_tab[-1] == "¬" or infix_tab[-1] == "~"):
        
        print('DELTA rule for NOT(FORALL( )), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        copy_of_infix_tab = deepcopy(infix_tab)
        # Replacing old variable with newly generated
        copy_of_infix_tab = [chr(ord(variables_tab[-1])+1) if el == infix_tab[0] else el for el in copy_of_infix_tab]
        copy_of_infix_tab.pop(0)  # Removing old variable
        copy_of_infix_tab.pop(-1)
        copy_of_infix_tab[-1] = "NOT"  # Adding NOT at the beginning of newly generated statement
        variables_tab.append(chr(ord(variables_tab[-1])+1))  # Append tab of variables with new variable used in delta rule
        general_tab.remove(infix_tab)
        general_tab.append(copy_of_infix_tab)
        print("Branch after rule: ", general_tab)
        print(end='\n')

    return stopping_rule
