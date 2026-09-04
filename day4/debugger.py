import pdb 

def add_numbers(x, y):
    result = x + y
    pdb.set_trace()
    return result

result = add_numbers(2, 3)
print(result)
