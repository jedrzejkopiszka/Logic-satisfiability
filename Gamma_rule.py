from copy import deepcopy


def gamma_rules(infix_tab, general_tab, variables_tab, used_dict, stopping_rule):
    
    if infix_tab[-1] == 'FORALL' or infix_tab[-1] == "∀":
        
        for j in variables_tab:
            if j in used_dict:
                if infix_tab not in used_dict[j]:
                    print('GAMMA rule for FORALL( ), used for: ', infix_tab)
                    print('Whole branch: ', general_tab)
                    used_dict[j].append(infix_tab)
                    new_tab = deepcopy(infix_tab)
                    used_dict[j] = deepcopy(infix_tab)
                    new_tab.pop()  # Removing FORALL
                    new_tab.pop(0)  # Removing old variable from beginning
                    # Replacing old variables with var from variables tab
                    new_tab = [j if el == infix_tab[0] else el for el in new_tab]  
                    general_tab.insert(0, new_tab)
                    print("Branch after rule: ", general_tab)
                    print(end='\n')

                else:
                    stopping_rule += 1
            else:
                print('GAMMA rule for FORALL( ), used for: ', infix_tab)
                print('Whole branch: ', general_tab)
                used_dict[j] = [infix_tab]
                new_tab = deepcopy(infix_tab)
                new_tab.pop()  # Removing FORALL
                new_tab.pop(0)  # Removing old variable from beginning
                # Replacing old variables with var from variables tab
                new_tab = [j if el == infix_tab[0] else el for el in new_tab]  
                general_tab.insert(0, new_tab)  # Inserting tab with replaced values to general tab
                print("Branch after rule: ", general_tab)
                print(end='\n')

    elif (infix_tab[-1] == 'NOT' or infix_tab[-1] == "~" or infix_tab[-1] == "¬") \
            and (infix_tab[-2] == "EXISTS" or infix_tab[-2] == "∃"):
        
        print('GAMMA rule for NOT( EXISTS( )), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        for j in variables_tab:
            if j in used_dict:
                if infix_tab not in used_dict[j]:
                    used_dict[j].append(infix_tab)
                    new_tab = deepcopy(infix_tab)
                    new_tab.pop()  # Removing NOT
                    new_tab[-1] = "NOT"
                    new_tab.pop(0)  # Removing old variable from beginning
                    # Replacing old variables with var from variables tab
                    new_tab = [j if el == infix_tab[0] else el for el in new_tab]  
                    general_tab.insert(0, new_tab)
                    print("Branch after rule: ", general_tab)
                    print(end='\n')
                else:
                    stopping_rule+=1
            else:
                used_dict[j] = [infix_tab]
                new_tab = deepcopy(infix_tab)
                new_tab.pop()  # Removing NOT
                new_tab[-1] = "NOT"
                new_tab.pop(0)  # Removing old variable from beginning
                # Replacing old variables with var from variables tab
                new_tab = [j if el == infix_tab[0] else el for el in new_tab]  
                general_tab.insert(0, new_tab)
                print("Branch after rule: ", general_tab)
                print(end='\n')

    return stopping_rule
