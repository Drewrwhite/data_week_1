
# test lists
things = ["guitar", "cup", "watch"]
empty_list = []


def list_sayer(list):  # create function called list_sayer() that takes list as an argument

    if list == []:  # if list is empty return false list is empty
        print("The list is empty")
        return (False)
        # used for loop and enumerate to print list with name and index
        for i, name in enumerate(list):
            # if list has items print items with index and return true
            print(f"Index: {i} Item: {name}")
        return (True)


list_sayer(empty_list)


def dict_sayer()
