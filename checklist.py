# Create our Checklist

checklist = list()

# Define Functions

def create(item):
    # CREATE
    checklist.append(item)

def read(index):
    # READ
    return checklist[index]

def update(index, item):
    # UPDATE
    checklist[index] = item

def destroy(index):
    # DESTROY
     checklist.pop(index)

def list_all_items():
    # Code to list all items in list
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    # Add code here that marks an item as completed
     update(index, "√ " + checklist[index])

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
        return True

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number: ")

        # Remember that item_index must actually exist or our program will crash.
        print(read(int(item_index)))
        return True

    # Print all items
    elif function_code == "P":
        list_all_items()
        return True

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    elif function_code == "D":
        item_index = user_input("Index Number: ")
        destroy(int(item_index))
        return True

    elif function_code == "M":
        item_index = user_input("Index Number: ")
        mark_completed(int(item_index))
        return True

    elif function_code == "U":
        item_index = user_input("Index Number: ")
        item_input = user_input("Item to update: ")
        update(int(item_index), str(item_input))
        return True


    # Catch all
    else:
        print("Unknown Option")
        return True

def test():
    # Add your testing code here

    # Call your new function with the appropriate value
    select("C")
    #View results
    list_all_items()
    #Call function with new value
    select("R")
    #View results

    list_all_items()
    mark_completed(0)

    user_value = user_input("Please Enter a value: ")
    print(user_value)


#Call functions

running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list, U to update list, M to mark list, D to destory list and Q to quit ")
    running = select(selection)
