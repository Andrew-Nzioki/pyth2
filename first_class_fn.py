# def divide (divided,divisor):
#     if divisor==0:
#         raise ZeroDivisionError('Divisor cannot be zero')
#     return divided/divisor

# def calculate(*values,operator):
#     return operator(*values)

# #first class function means functions can be used as varibales

# result=calculate(20,4,operator=divide )

def search(sequence,expected,finder):
    for elem in sequence:
        if finder(elem)==expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

def get_friend_name(friend):
    return friend["name"]

friends=[
    {"name":"Rolf Smith","age":24}
]

print(search(friends,"Rolf Smith",get_friend_name))