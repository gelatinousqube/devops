import names

input_gender = input('Enter m for male or f for female:\n')

if input_gender != 'm' and input_gender != 'f':
    raise Exception("Please enter a valide value.")

if input_gender == 'm':
    print(names.get_full_name(gender='male'))
else:
    print(names.get_full_name(gender='female'))