# All functions start with def(params)
# Mind your identation!
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

# All functions must have a return statement

print(mean([1,5,12]))

# In order to fr a function to take multiple params
# we need to add those to the function definition
def area(a, b):
    return a * b

"""
Python functions can have keyword and non-keyword arguments.
Non-keyword arguments are also known as positional arguments
because their usage is determined by the position or order
in which they are passed to the function defiintion.

Keyword arguments are defined more explicitly and can have
default values defined that are set regardless of position.

The only catch is that a default parameter CANNOT be before
a non-default argument.
"""

def area_with_kwargs(a, b=6):
    return a * b

print(area(3, 4))
print(area_with_kwargs(3))

"""
You can define a function with an arbitrary number of arguments
by using the syntax def func(*parameter):

The standard convention is to do so using def func(*args):

By default, these functions return their entries as a tuple.
"""
def mean_with_args(*args):
    return sum(args) / len(args)

"""
Functions with an arbitrary number of keyword args
are defined using the convention def func(**kwargs):

By default, these functions return their entries as a dictionary.
This is why we use .values() in the function below.
"""
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3, b=3, c=3))