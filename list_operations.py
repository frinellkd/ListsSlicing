# Part 1: Fundamental operations on lists
# ---------------------------------------
#
# The fundamental operations on lists in Python are those that are part of the
# language syntax and/or cannot be implemented in terms of other list operations:
#
#     * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
#     * List indexing (some_list[index])
#     * List indexing assignment (some_list[index] = value)
#     * List slicing (some_list[start:end])
#     * List slicing assignment (some_list[start:end] = another_list)
#     * List index deletion (del some_list[index])
#     * List slicing deletion (del some_list[start:end])
#
# In this section you will implement functions that each use just one of the above
# operations. The docstring of each function describes what it should do. Consult
# test_list_operations.py for concrete examples of the expected function behavior.
#
# DO NOT USE ANY OF THE BUILT IN LIST METHODS, OR len(l)


def head(input_list):
    """
    Return the first element of the input list.
    [ A, B, C, D, E, F ] --> A
    """

    return input_list[0]    


def tail(input_list):
    """
    Return all elements of the input list except the first.
    [ A, B, C, D ] --> [ B, C, D ]
    """

    return input_list[1:]


def last(input_list):
    """
    Return the last element of the input list.
    [ A, B, C, D ] --> D
    """

    return input_list[-1]


def init(input_list):
    """
    Return all elements of the input list except the last.
    [ A, B, C, D ] --> [ A, B, C ]
    """

    return input_list[:-1]


##############################################################################
# Do yourself a favor and get a short code review here.
# You can also get reviewed by a neighbor who has been reviewed.


def first_three(input_list):
    """
    Return the first three elements of the input list.
    [ A, B, C, D, E, F ] --> [ A, B, C ]
    """

    return input_list[0:3]


def last_five(input_list):
    """
    Return the last five elements of the input list.
    [ A, B, C, D, E, F ] --> [ B, C, D, E, F ]
    """

    return input_list[-5:]


def middle(input_list):
    """
    Return all elements of the input list except the first two and the last two.
    [ A, B, C, D, E, F ] --> [ C, D ]
    """

    return input_list[2:-2]


def inner_four(input_list):
    """
    Return the third, fourth, fifth, and sixth elements of the input list.
    [ A, B, C, D, E, F, G ] --> [ C, D, E, F ]
    """

    return input_list[2:6]


def inner_four_end(input_list):
    """
    Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.
    [ A, B, C, D, E, F, G, H, I, J, K, L] --> [ G, H, I, J ]
    """

    return input_list[-6:-2]


def replace_head(input_list):
    """
    Replace the head of the input list with the value 42.
    [ A, B, C, D ] --> [ 42, B, C, D]
    """

    input_list[0] = 42


def replace_third_and_last(input_list):
    """
    Replace the third and last elements of the input list with the value 37.
    [ A, B, C, D, E, F ] --> [ A, B, 37, D, E, 37 ]
    """

    input_list[2] = 37
    input_list[-1] = 37


def replace_middle(input_list):
    """
    Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    [ A, B, C, D, E, F, G, H, I ] --> [ A, B, 42, 37, H, I ]
    """

    input_list[2:-2] = [42,37]


def delete_third_and_seventh(input_list):
    """
    Remove the third and seventh elements of the input list.
    [ A, B, C, D, E, F, G, H ] --> [ A, B, D, E, F, H ]
    """
    input_list[6:7] = []
    input_list[2:3] = []



def delete_middle(input_list):
    """
    Remove all elements from the input list except for the first two and the
    last two.
    [ A, B, C, D, E, F, G, H ] --> [ A, B, G, H ]
    """

    input_list[2:-2] = []


##############################################################################
# END OF MAIN EXERCISE
#
# Please ask for a code review from an instructor/TA before proceeding.


# Further Study / Extra Credit
# ----------------------------
#
# In this section you will implement your own versions of the standard list methods.
# You should use only the primitive operations from Part 1 and 2 in your implementations.
# For loops are also allowed, such as the following:
#     for element in some_list:
#         # Do something with element
#
# Each custom method imitates a built-in list method, as described by the docstring
# for each function. Play with the built-in methods in the Python REPL to get a feel
# for how they work before trying to write your custom version. You may also look at
# the test_list_operations.py file for concrete examples of expected behavior.


def custom_len(input_list):
    """
    like len(input_list), should return the number of items in the list
    """
    count = 0
    for item in input_list:
        count += 1
    return count


# For the next four exercises, you'll need to be clever and think about ways
# to use "list slice assignment" to solve these problems.
#
# NOTE: these are especially contrived--for example, you wouldn't really want
# to typically append things to a list like this (you'd want to to use the
# list.append() method), but we want you to practice list slicing assignment
# in different ways so it sticks in your brain.


def custom_append(input_list, value):
    """
    like input_list.append(value), should add the value to the end of the list
    and return nothing
    """

    input_list[len(input_list):] = [value] 


def custom_extend(input_list, second_list):
    """
    like input_list.extend(second_list), should append every item in the second
    list to the end of the first list and return nothing
    """

    input_list[len(input_list):] = second_list


def custom_insert(input_list, index, value):
    """
    like input_list.insert(index, value), should insert (not replace) the value
    at the specified index of the input list and return nothing
    """
    input_list[:] = input_list[:index] + [value] + input_list[index:]
    

def custom_remove(input_list, value):
    """
    like input_list.remove(value), should remove the first item of the
    value specified and return nothing
    """
    input_list[:] = input_list[:input_list.index(value)] + input_list[input_list.index(value)+1:]

    
def custom_pop(input_list):
    """
    like input_list.pop(), should remove the last item in the list and
    return it
    """
    last_item = input_list[-1]
    input_list[:] = input_list[:-1]
    return last_item


def custom_index(input_list, value):
    """
    like input_list.index(value), should return the index of the first item
    which matches the specified value
    """
    index_counter = 0
    
    for items in input_list:
        if items == value:
            return index_counter
        else:
            index_counter += 1



def custom_count(input_list, value):
    """
    like input_list.count(value), should return the number of times the specified
    value appears in the list.
    """
    value_counter = 0
    
    for items in input_list:
        if items == value:
            value_counter += 1
        
    return value_counter

def custom_reverse(input_list):
    """
    like input_list.reverse(), should reverse the elements of the original list
    and return nothing (we call this reversing "in place")
    """

    input_list[:] = input_list[::-1]


def custom_contains(input_list, value):
    """
    like (value in input_list), should return True if the list contains the
    specified value and False if it does not. Remember, do not use the `in`
    statement -- find another way to solve it!
    """
    try:
        input_list.index(value) 
        return True
    except:
        return False

def custom_equality(some_list, another_list):
    """
    like (some_list == another_list), should return True if both lists contain
    the same values in the same indexes
    """
    

    status = True

    if len(some_list) != len(another_list):
        status = False

    else:
        for num in range(len(some_list)):

            if some_list[num] != another_list[num]:
                status = False
                break

    return status
##############################################################################
# END OF EXTRA CREDIT
#
# Please ask for a code review. Also, give your partner a high-five!