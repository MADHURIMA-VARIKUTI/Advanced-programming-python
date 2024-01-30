def count_local_variables():
    var1 = 10.5
    var2 = "madhu"
    var3 = [5 ,6 ,7]
    var4 = {"a": "value1", "b": 2}
    
    local_variables = locals()
    return len(local_variables)

num_local_variables = count_local_variables()
print("Number of local variables:", num_local_variables)

# Number of local variables: 4

# def func():
#     a=15.5
#     b=9
#     name='MADHURIMA'
# print("no.of local variables",func.__code__.co_nlocals)    
# # no.of local variables3