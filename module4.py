def idx_of_inputs():
    print("How many number in the list?")
    n = int(input())
    input_n_list = []
    print("Input your number and press enter")
    for i in range(n):
        temp = int(input())
        input_n_list.append(temp)
    
    print("Input the number you want to check")
    x = int(input())

    for idx,val in enumerate(input_n_list):
        if x==val:
            return idx+1
    return -1

print(idx_of_inputs())