# test list
things = ["guitar", "cup", "watch"]
# create function called list_sayer() that takes list as an argument


def list_sayer(list):
    # if list is empty return false list is empty
    if list == []:
        print(False, "The list is empty")
# if list has items return items with index and true
    for index in range(len(list)):
        print("Item: {} Index: {}".format(list[index], index))
        return (True)


list_sayer(things)
