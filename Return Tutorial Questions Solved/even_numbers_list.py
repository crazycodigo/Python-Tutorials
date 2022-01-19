# defining function
def new_lst(input_lst):
    new_list = []

    # looping through elements of input list
    for i in input_lst:

        # checking if element is even
        if i % 2 == 0:

            # adding even element to list
            new_list.append(i)
    
    # returning the new list
    return new_list

# taking input
lst = eval(input("Enter a list: "))

# printing
print("New list: ", new_lst(lst)) 
