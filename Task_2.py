def merge_k_lists(lists):
    merged_list = []
    
    for lst in lists:
        merged_list = merge_two_sorted_lists(merged_list, lst)
        
    return merged_list

def merge_two_sorted_lists(l1, l2):
    merged = []
    i = j = 0
    
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
            
    while i < len(l1):
        merged.append(l1[i])
        i += 1
        
    while j < len(l2):
        merged.append(l2[j])
        j += 1
        
    return merged
