def increment(number, by):
    return number, number + by


print(increment(2, 1))


def increment_by_default_parameter_value(number, by=2):
    return number, number + by


print(increment_by_default_parameter_value(2))


def increment_return_type(number, by=3) -> tuple:
    return number, number + by


print(increment_return_type(2))


def multiply_passing_variable_arguments_and_coming_as_tuple_param(*numbers):  # treats the arguments coming here as TUPLE parameter
    print(f"multiply_passing_variable_arguments_and_coming_as_tuple_param {numbers}")
    output = 1
    for number in numbers:
        output *= number
    return output


print(multiply_passing_variable_arguments_and_coming_as_tuple_param(2, 3))  # passing variable number of arguments to a function


def save_user_passing_keyword_arguments_and_coming_as_dict(**user):
    print(f"save_user_passing_keyword_arguments_and_coming_as_dict {user}")
    print(f"UserID:{user.get('id')} UserName:{user.get('name')}")


save_user_passing_keyword_arguments_and_coming_as_dict(id=1, name="Karan")