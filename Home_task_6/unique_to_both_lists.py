def unique_to_both_lists(list1, list2):


    set1, set2 = set(list1), set(list2)

    unique_elements = (set1 - set2) | (set2 - set1)

    return list(unique_elements)
