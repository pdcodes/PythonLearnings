# All functions start with def(params)
# Mind your identation!
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

# All functions must have a return statement

print(mean([1,5,12]))