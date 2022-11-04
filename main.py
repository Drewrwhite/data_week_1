
# test lists
things = ["guitar", "cup", "watch"]
empty_list = []


def list_sayer(list):  # write function called list_sayer() that takes list as an argument

    if list == []:  # if list is empty return false list is empty
        print("The list is empty")
        return (False)
        # used for loop and enumerate to print list with name and index
        for i, name in enumerate(list):
            # if list has items print items with index and return true
            print(f"Index: {i} Item: {name}")
        return (True)


list_sayer(empty_list)

# Example dictionaries
dict_test = {"A": 1, "B": 2, "C": 3}
dict_empty = {}
# write function called dict_sayer that takes dictionary as an argument


def dict_sayer(dictionary):
  # if dict empty return false
    if len(dictionary) == 0:
        print("Dictionary empty")
        return (False)
    # if dictionary has items return key, value true
    for key, value in dictionary.items():
        print("Key: {} Value: {}".format(key, value))
    return (True)


dict_sayer(dict_test)

# write function called greatest() that takes dictionary as argument


def greatest(dictionary):
    # define top value and corresponding key
    top_value = max(dictionary.values())
    top_key = max(dictionary, key=dictionary.get)
    return (top_key, top_value)


    # get top value and key to return together
greatest(dict_test)

# write function called zipper() that take 2 lists as arguments


def zipper(list1, list2):
