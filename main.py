
# test lists
things = ["guitar", "cup", "watch"]
empty_list = []
# write function called list_sayer() that takes list as an argument


def list_sayer(list):
    # if list is empty return false list is empty
    if list == []:
        print("The list is empty")
        return (False)
        # used for loop and enumerate to print list with name and index
        for i, name in enumerate(list):
            # if list has items print items with index and return true
            print(f"Index: {i} Item: {name}")
        return (True)


list_sayer(empty_list)

# test dictionaries
dict_test = {"A": 1, "B": 7, "C": 3}
dict_empty = {}
# write function called dict_sayer that takes dict as an argument


def dict_sayer(dict):
  # if dict empty return false
    if len(dict) == 0:
        print("Dictionary Empty!")
        return (False)
    # if dict has items return key, value true
    for key, value in dict.items():
        print("Key: {} Value: {}".format(key, value))
    return (True)


dict_sayer(dict_test)

# write function called greatest() that takes dict as argument


def greatest(dict):
    # define top value and corresponding key
    top_value = max(dict.values())
    top_key = max(dict, key=dict.get)
    return (top_key, top_value)


    # get top value and key to return together
greatest(dict_test)


# test lists for zipper()
list_a = ["Aengus", "Bear", "Cali"]
list_b = ["6yo", "15yo", "9yo"]
list_c = ["a", "b", "c", "d"]
list_d = ["tan", "sesame", "spotted"]

# write function called zipper() that take 2 lists as arguments


def zipper(list1, list2):
  # if list1 = list2 then return dict
    if len(list1) == len(list2):
        return dict(zip(list1, list2))
  # if list1 not equal to list2 then return tuple with lists and number of items
    else:
        return tuple([list1, len(list1), [list2, len(list2)]])


zipper(list_a, list_d)
