from copy import deepcopy


def beta_rules(infix_tab, general_tab, stopping_rule, new_general_tab):
    
    if (infix_tab[-1] == "NOT" or infix_tab[-1] == "~" or infix_tab[-1] == "¬") \
            and (infix_tab[-2] == "AND" or infix_tab[-2] == "&" or infix_tab[-2] == "∧"):  #NOT(a AND b)
        
        print('BETA rule for NOT(a AND b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        infix_tab.pop()
        temp_list = ["NOT"]
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
        helping_tab = deepcopy(general_tab)
        temp_list2.append('NOT')
        temp_list.reverse()

        general_tab.append(temp_list2)
        general_tab.remove(infix_tab)

        helping_tab.remove(infix_tab)
        help2 = [temp_list]
        help2.extend(helping_tab)
        new_general_tab.append(help2)
        print('Branch after rule: ', general_tab)
        print(end='\n')

    if infix_tab[-1] == "OR" or infix_tab[-1] == "|" or infix_tab[-1] == "V":  # NOT(a OR b)
        print('BETA rule for ( a OR b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
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
        helping_tab = deepcopy(general_tab)
        general_tab.append(temp_list2)
        temp_list.reverse()
        general_tab.remove(infix_tab)

        helping_tab.remove(infix_tab)
        help2=[temp_list]
        help2.extend(helping_tab)
        new_general_tab.append(help2)
        print('Branch after rule: ', general_tab)
        print(end='\n')

    if infix_tab[-1] == "IMPLIES" or infix_tab[-1] == "→":  # (a IMPLIES b)
        print('BETA rule for (a IMPLIES b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
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
        helping_tab=deepcopy(general_tab)
        temp_list2.append('NOT')
        general_tab.append(temp_list2)
        temp_list.reverse()
        general_tab.remove(infix_tab)

        helping_tab.remove(infix_tab)
        help2=[temp_list]
        help2.extend(helping_tab)
        new_general_tab.append(help2)
        print('Branch after rule: ', general_tab)
        print(end='\n')

    if (infix_tab[-1] == "NOT" or infix_tab[-1] == "~" or infix_tab[-2] == "¬") \
        and (infix_tab[-2] == "↔" or infix_tab[-2] == "IFF"):  # NOT (a ↔ b)
        
        print('BETA rule for NOT(a ↔ b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
        infix_tab.pop()
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
        help_tab.append("NOT")
        general_tab.append(help_tab)
        help_tab = []
        help_tab.extend(temp_list)
        help_tab.extend(temp_list2)
        help_tab.append("IMPLIES")
        help_tab.append("NOT")
        new_general_tab.append([temp_list])
        general_tab.remove(infix_tab)
        print('Branch after rule: ', general_tab)
        print(end='\n')

    if infix_tab[-1] == "XOR" or infix_tab[-1] == "⊕":  # a XOR b
        print('BETA rule for (a XOR b), used for: ', infix_tab)
        print('Whole branch: ', general_tab)
        infix_tab.pop()
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
        help_tab.append("NOT")
        general_tab.append(help_tab)
        help_tab = []
        help_tab.extend(temp_list)
        help_tab.extend(temp_list2)
        help_tab.append("IMPLIES")
        help_tab.append("NOT")
        new_general_tab.append([help_tab])
        general_tab.remove(infix_tab)
        print('Branch after rule:', general_tab)
        print(end='\n')

    stopping_rule += 1
    return stopping_rule
