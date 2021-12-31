from pprint import pp

"""

5 * 4 * 3 * 2 * 1 
factorial(n) = n * factorial(n-1)

factorial(1) = 1

fact(5) = 5 * fact(4)
        = 5 * 4 * fact(3)
        = 5 * 4 * 3 * fact(2)
        = 5 * 4 * 3 * 2 * fact(1)
        = 120
"""


# FACTORIAL
def factorial(n):
    """
    factorial(n) = n * factorial(n-1)
    e.g. factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n == 1:
        return 1

    # fact = factorial(n-1)
    return n * factorial(n - 1)


print(factorial(5))

"""
factorial(4)
    factorial(3)
        factorial(2)
            factorial(1)
            return 1
        return 2 * 1 = 2
    return 3 * 2 = 6
return 4 * 6 = 24
"""

print(factorial(10))


# COUNT DOWN
def count_down(n):
    for i in range(n, 0, -1):
        print(i)

    print("go")


def count_down_rec(n):
    if n < 1:
        print("go")
        return

    print(n)
    count_down_rec(n - 1)
    return


count_down(3)
count_down_rec(3)

"""
count_down_rec(3)
    count_down_rec(2)
        count_down_rec(1)
            count_down_rec(0)
            return
        return
    return
return
"""


# SUM RANGE
def sum_range(n):
    total = 0
    for i in range(n):
        total += i
    return total


def sum_range_rec(n, total=0):
    if n == 0:
        return total
    return sum_range_rec(n - 1, total + n)


print(sum_range_rec(3))

"""
sum_range_rec(3, 0)
    sum_range_rec(2, 3)
      sum_range_rec(1, 5)
        sum_range_rec(0, 6)
        return 6
      return 6
    return 6
return 6
"""


# PRINT PATTERN
def print_pattern(num):
    if num < 1:
        return
    else:
        print(num, end=" ")
        print_pattern(num - 1)
        print(num, end=" ")
        return


my_number = 3
print_pattern(my_number)

"""
print_pattern(3)
"3"
    print_pattern(2)
    "2"
        print_pattern(1)
        "1"
            print_pattern(0)
            return
        "1"
    "2"
"3"
"""

# TREE TRAVERSAL
table_of_contents = {
    "title": "Get Started",
    "expand": False,
    "children": [
        {
            "title": "Introduction",
            "expand": False,
            "children": []
        },
        {
            "title": "Tutorials",
            "expand": False,
            "children": [
                {
                    "title": "Your first app",
                    "expand": False,
                    "children": []
                },
                {
                    "title": "Advanced",
                    "expand": False,
                    "children": [
                        {"title": "Recursion", "children": [], "expand": False},
                        {"title": "Hash Tables", "children": [], "expand": False}]
                }]

        }]
}

pp(table_of_contents)


def expand_all(node):
    if len(node["children"]) == 0:
        return

    node["expand"] = True
    for child in node["children"]:
        expand_all(child)


expand_all(table_of_contents)

pp(table_of_contents)

"""
expand_all("Get Started")
    expand_all("Introduction")
    return
    expand_all("Tutorials")
        expand_all("Your first app")
        return
        expand_all("Advanced")
            expand_all("Recursion")
            return
            expand_all("Hash Tables")
            return
        return
    return
return    

"""


# FIBONACCI
# Fibonacci series of 5 is : 0 1 1 2 3
def fib(n):
    """
    fib(0) = 0
    fib(1) = 1
    fib(2) = 1
    fib(n) = fib(n-1) + fib(n-2)
    """


print(fib(5))


# #######################################################
#
# """
# Return all possible combinations of strings of given length,
# which can be formed from a set of supplied characters.
#
# Input:
# char_set = {'a', 'b'}, length = 3
#
# Output:
# aaa
# aab
# aba
# abb
# baa
# bab
# bba
# bbb
#
# NB: we cannot use itertools product or permutations functions.
# """
#
def get_str_combinations(char_set, length):
    """
    The function that prints all possible strings of length l.
    """
    num_chars = len(char_set)
    get_str_combinations_rec(char_set, "", num_chars, length)


def get_str_combinations_rec(char_set, prefix, num_chars, length):
    """
    Main recursive method that prints all possible strings of length l.
    """
    if length == 0:
        print(prefix)
        return

    # One by one add all characters
    # from char_set and recursively
    # call for length equals to length -1
    for i in range(num_chars):
        new_prefix = prefix + char_set[i]

        # required_length is decreased, because we have added a new character
        get_str_combinations_rec(char_set, new_prefix, num_chars, length - 1)


print("Test No1")
set1 = ['a', 'b']
k = 3
get_str_combinations(set1, k)

print("\nTest No2")
set2 = ['a', 'b', 'c', 'd']
k = 2
get_str_combinations(set2, k)
