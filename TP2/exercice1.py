def combine_dic(dic_1, dic_2):
    dic_3 = dic_1
    for key in dic_2:
       if key not in dic_3 or dic_2[key] > dic_3[key]:
         dic_3[key] = dic_2[key]
    return dic_3

if __name__ == '__main__':
    # Combinaison de dictionnaire
    dic_1 = {'a': 5, 'b': 2, 'c': 9}
    dic_2 = {'a': 1, 'b': 8, 'd': 17}

    dic_3 = combine_dic(dic_1,dic_2)
    print(dic_3)