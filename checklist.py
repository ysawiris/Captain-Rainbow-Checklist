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

def test():
    # Add your testing code here
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0,"purple socks")

    destroy(1)

    print(read(0))

    list_all_items()

#Call functions
test()
