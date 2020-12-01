from copy import deepcopy


def aplha_rules(infix_tab, general_tab, stopping_rule):
    if (infix_tab[-1] == 'NOT' or infix_tab[-1] == '~' or infix_tab[-1] == '¬') and (
            infix_tab[-2] == 'NOT' or infix_tab[-2] == '~' or infix_tab[-2] == '¬'):
        print('ALPHA rule for NOT(NOT()), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        infix_tab.pop()
        print('Branch after rule:', general_tab)

    elif infix_tab[-1] == "AND" or infix_tab[-1] == "&" or infix_tab[-1] == "∧":
        print('ALPHA rule for (a AND b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        copy_of_infix_tab=infix_tab[:]
        temp_list = []
        temp_list2 = []
        numerator = 1000
        exists_flag = 0
        for i in reversed(infix_tab):
            if (len(i) != 3 or i == "NOT" or i == "AND" or i == "IFF" or i == "XOR") and numerator > 0:
                temp_list.append(i)
                numerator -= 1
                if i == "EXISTS" or i == "∀" or i == "FORALL" or i == "∃" or i == "AND" \
                    or i == "OR" or i == "XOR" or i == "IMPLIES" or i == "⊕" or i == "↔" \
                    or i == "IFF" or i == "→" or i == "∨" or i == "∧" or i == "&" or i == "|":
                    exists_flag += 1
            else:
                temp_list.append(i)
                if numerator < 800:
                    numerator += int(i[2])-1
                else:
                    numerator = int(i[2])
                if exists_flag >= 1:
                    numerator += exists_flag
                    exists_flag = 0
            if numerator <= 0:
                temp_list2 = infix_tab[0:len(infix_tab) - len(temp_list)]
                break
        general_tab.append(temp_list2)
        temp_list.reverse()
        general_tab.append(temp_list)
        general_tab.remove(copy_of_infix_tab)
        print("Branch after rule: ", general_tab)
        print(end='\n')

    elif (infix_tab[-1] == "NOT" or infix_tab[-1] == "~" or infix_tab[-1] == "¬") and (
            infix_tab[-2] == "OR" or infix_tab[-2] == "∨" or infix_tab[-2] == "|"):
        print('ALPHA rule for NOT(a OR b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        infix_tab.pop()
        copy_of_infix_tab = infix_tab[:]
        temp_list = ["NOT"]
        temp_list2 = []
        numerator = 1000
        exists_flag = 0
        for i in reversed(infix_tab):
            if (len(i) != 3 or i == "NOT" or i == "AND" or i == "IFF" or i == "XOR") and numerator > 0:
                temp_list.append(i)
                numerator -= 1
                if i == "EXISTS" or i == "∀" or i == "FORALL" or i == "∃" or i == "AND" \ 
                    or i == "OR" or i == "XOR" or i == "IMPLIES" or i == "⊕" or i == "↔"  \
                    or i == "IFF" or i == "→" or i == "∨" or i == "∧" or i == "&" or i == "|":
                    exists_flag += 1
            else:
                temp_list.append(i)
                if numerator < 800:
                    numerator += int(i[2])-1
                else:
                    numerator = int(i[2])
                if exists_flag >= 1:
                    numerator += exists_flag
                    exists_flag = 0
            if numerator <= 0:
                temp_list2 = infix_tab[0:len(infix_tab) - len(temp_list) + 1]
                break
        temp_list2.append('NOT')
        general_tab.append(temp_list2)
        temp_list.reverse()
        general_tab.append(temp_list)
        general_tab.remove(copy_of_infix_tab)
        print("Branch after rule:", general_tab)
        print(end='\n')

    elif (infix_tab[-1] == "NOT" or infix_tab[-1] == "~" or infix_tab[-1] == "¬") and (
            infix_tab[-2] == "IMPLIES" or infix_tab[-2] == "→"):
        print('ALPHA rule for NOT(a IMPLIES b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        infix_tab.pop()
        copy_of_infix_tab = infix_tab[:]
        temp_list = ['NOT']
        temp_list2 = []
        numerator = 1000
        exists_flag = 0
        for i in reversed(infix_tab):
            if (len(i) != 3 or i == "NOT" or i == "AND" or i == "IFF" or i == "XOR") and numerator > 0:
                temp_list.append(i)
                numerator -= 1
                if i == "EXISTS" or i == "∀" or i == "FORALL" or i == "∃" or i == "AND" \ 
                    or i == "OR" or i == "XOR" or i == "IMPLIES" or i == "⊕" or i == "↔" \
                    or i == "IFF" or i == "→" or i == "∨" or i == "∧" or i == "&" or i == "|":
                    exists_flag += 1

            else:
                temp_list.append(i)
                if numerator < 800:
                    numerator += int(i[2])-1
                else:
                    numerator = int(i[2])
                if exists_flag >= 1:
                    numerator += exists_flag
                    exists_flag = 0

            if numerator <= 0:
                temp_list2 = infix_tab[0:len(infix_tab) - len(temp_list)+1]
                break
        general_tab.append(temp_list2)
        temp_list.reverse()
        general_tab.append(temp_list)
        general_tab.remove(copy_of_infix_tab)
        print("Branch after rule: ", general_tab)
        print(end='\n')

    elif infix_tab[-1] == "↔" or infix_tab[-1] == "IFF":
        print('ALPHA rule for (a IFF b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        copy_of_infix_tab = infix_tab[:]
        help_tab = []
        temp_list = []
        temp_list2 = []
        numerator = 1000
        exists_flag = 0
        for i in reversed(infix_tab):
            if (len(i) != 3 or i == "NOT" or i == "AND" or i == "IFF" or i == "XOR") and numerator > 0:
                temp_list.append(i)
                numerator -= 1
                if i == "EXISTS" or i == "∀" or i == "FORALL" or i == "∃" or i == "AND" \ 
                    or i == "OR" or i == "XOR" or i == "IMPLIES" or i == "⊕" or i == "↔" \ 
                    or i == "IFF" or i == "→" or i == "∨" or i == "∧" or i == "&" or i == "|":
                    exists_flag += 1
            else:
                temp_list.append(i)
                if numerator < 800:
                    numerator += int(i[2])-1
                else:
                    numerator = int(i[2])
                if exists_flag >= 1:
                    numerator += exists_flag
                    exists_flag = 0
            if numerator <= 0:
                temp_list2 = infix_tab[0:len(infix_tab) - len(temp_list)]
                break
        help_tab.extend(temp_list2)
        temp_list.reverse()
        help_tab.extend(temp_list)
        help_tab.append("IMPLIES")
        general_tab.append(help_tab)
        help_tab = []
        help_tab.extend(temp_list)
        help_tab.extend(temp_list2)
        help_tab.append("IMPLIES")
        general_tab.append(help_tab)
        general_tab.remove(copy_of_infix_tab)
        print("Branch after rule", general_tab)
        print(end='\n')

    elif (infix_tab[-2] == "XOR" or infix_tab[-2] == "⊕") and (
            infix_tab[-1] == "NOT" or infix_tab[-1] == "~" or infix_tab[-1] == "¬"):
        print('ALPHA rule for NOT(a XOR b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        infix_tab.pop()
        copy_of_infix_tab = deepcopy(infix_tab)
        help_tab = []
        temp_list = []
        temp_list2 = []
        numerator = 1000
        exists_flag = 0
        for i in reversed(infix_tab):
            if (len(i) != 3 or i == "NOT" or i == "AND" or i == "XOR" or i == "IFF") and numerator > 0:
                temp_list.append(i)
                numerator -= 1
                if i == "EXISTS" or i == "∀" or i == "FORALL" or i == "∃" or i == "AND" \ 
                    or i == "OR" or i == "XOR" or i == "IMPLIES" or i == "⊕" or i == "↔" \ 
                    or i == "IFF" or i == "→" or i == "∨" or i == "∧" or i == "&" or i == "|":
                    exists_flag += 1
            else:
                temp_list.append(i)
                if numerator < 800:
                    numerator += int(i[2])-1
                else:
                    numerator = int(i[2])
                if exists_flag >= 1:
                    numerator += exists_flag
                    exists_flag = 0
            if numerator <= 0:
                temp_list2 = infix_tab[0:len(infix_tab) - len(temp_list)]
                break
        help_tab.extend(temp_list2)
        temp_list.reverse()
        help_tab.extend(temp_list)
        help_tab.append("IMPLIES")
        general_tab.append(help_tab)
        help_tab = []
        help_tab.extend(temp_list)
        help_tab.extend(temp_list2)
        help_tab.append("IMPLIES")
        general_tab.append(help_tab)
        general_tab.remove(copy_of_infix_tab)
        print("Branch after rule: ", general_tab)
        print(end='\n')

    else:
        copy_of_infix_tab=deepcopy(infix_tab)  # Copy of infix_tab.
        general_tab.remove(copy_of_infix_tab)  # Remove from the front of general tab.
        general_tab.append(copy_of_infix_tab)  # Add to the end of general tab.
        stopping_rule += 1

    return stopping_rule

