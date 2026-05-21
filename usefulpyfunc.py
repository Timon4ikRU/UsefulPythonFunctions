import random

print("UsefulPyFunc version 1.0.2")
print("(c)Timofey Yakubov 2026")
print("GPL v2")
print("Here I am!")

def get_help():
    print("="*15)
    print("UsefulPyFunc requires module random to work properly (some functions use it)")
    print("pip install random if you dont have it")

    print("=" * 10)
    print("UPF HELP")
    
    print("equal_not_strict: ")
    help(equal_not_strict)
    print("equal_strict: ")
    help(equal_strict)
    print("check_type: ")
    help(check_type)
    print("equal_not_strict_arr: ")
    help(equal_not_strict_arr)
    print("equal_strict_arr: ")
    help(equal_strict_arr)
    print("check_type_arr: ")
    help(check_type_arr)
    print("random_array_int: ")
    help(random_array_int)
    print("random_array_uni: ")
    help(random_array_uni)

def equal_not_strict(num1, num2):
    '''Not strict equality check (2 nums)'''
    if num1 == num2:
        print("True")
    else:
        print("False")
        
def equal_strict(num1, num2):
    '''Strict equality check (2 nums)'''
    if type(num1) == type(num2):
        if num1 == num2:
            print("True")
    else:
        print("False")
            
def check_type(data):
    '''Type checker'''
    print("Type of ", data, ":", type(data))

def equal_not_strict_arr(arr_data, array_name, mode):
    '''Not strict equality check (Array, array name, 2 modes)'''
    print("="*10)
    print("Array ", array_name, " equality check (Not strict, mode:", str(mode), ")")
    if mode == 1:
        for i in range(len(arr_data) - 1):
            equal_not_strict(arr_data[i], arr_data[i+1])
    elif mode == 2:
        for i in range(0, len(arr_data) - 2, 2):
            equal_not_strict(arr_data[i], arr_data[i+2])
    else:
        print("Wrong mode!")
        pass
    
def equal_strict_arr(arr_data, array_name, mode):
    '''Strict equality check (Array, array name, 2 modes)'''
    print("="*10)
    print("Array ", array_name, " equality check (Strict, mode:", str(mode), ")")
    if mode == 1:
        for i in range(len(arr_data) - 1):
            equal_strict(arr_data[i], arr_data[i+1])
    elif mode == 2:
        for i in range(0, len(arr_data) - 2, 2):
            equal_strict(arr_data[i], arr_data[i+2])
    else:
        print("Wrong mode!")
        pass
   
def check_type_arr(arr_data, array_name):
    '''Type checker (array with array_name)'''
    print("="*10)
    print("Types of ", array_name)
    for i, item in enumerate(arr_data):
        print(f"Элемент {i}: {item}, тип: {type(item)}")
        
def random_array_int(quantity, minimal, maximal, array_name, array_data):
    '''Creates random array of integers (quantity, min, max, array_name (to show), array_data (how array is named)'''
    print("="*10)
    print("Generating random.randint in ", array_name)
    for i in range (quantity):
        a = random.randint(minimal, maximal)
        array_data.append(a)
        
def random_array_uni(quantity, minimal, maximal, array_name, array_data):
    '''Creates random array of uniform (quantity, min, max, array_name (to show), array_data (how array is named)'''
    print("="*10)
    print("Generating random.uniform in ", array_name)
    for i in range (quantity):
        a = random.uniform(minimal, maximal)
        array_data.append(a)