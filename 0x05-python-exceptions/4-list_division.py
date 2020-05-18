#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
            continue
        except TypeError:
            print("wrong type")
            result = 0
            continue
        except IndexError:
            result = 0
            print("out of range")
            continue
        finally:
            new_list.append(result)
    return (new_list)
