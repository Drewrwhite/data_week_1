
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

# Example dictionaries
dict_test = {"A": 1, "B": 2, "C": 3}
dict_empty = {}
# write function that takes dictionary as an argument


def dict_sayer(dictionary):

    for key, value in dictionary.items():
      print("Key: {} Value: {}".format(key, value))
      return (True)
    if len(dictionary) == 0:
      print("Dictionary empty"
    return (False)
