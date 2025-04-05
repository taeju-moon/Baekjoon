def solution(sizes):
    max_sizes = [max(size) for size in sizes]
    max_size_index = max_sizes.index(max(max_sizes))
    
    initial_data = sizes[max_size_index]
    
    index_of_max_size_in_initial_data = initial_data.index(max(initial_data))
    
    standard_index = 1 if index_of_max_size_in_initial_data == 0 else 0
    
    for size in sizes:
        if initial_data[0] >= size[0] and initial_data[1] >= size[1]:
            continue
            
        if initial_data[0] >= size[1] and initial_data[1] >= size[0]:
            continue
            
        
        initial_data[standard_index] = min(size)
        
    return initial_data[0] * initial_data[1]