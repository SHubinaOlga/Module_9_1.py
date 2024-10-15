def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
       result = i(int_list)
       results[i.__name__] = result
    return results
    
def __min__(results):
    for i in results:
        if i < min_result:
            return i
            
def __max__(results):
    for i in results:
        if i > max_result:
            return i
            
def __len__(results):
    count = len(results)
    return count
    
def __sum__(results):
    sum = 0
    for item in results:
        sum = sum + item
        return sum
        
def __sorted__(results):
    for i in results:
        return i.sorted(results)
    

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))    