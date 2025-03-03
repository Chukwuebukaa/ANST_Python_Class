f_name = input('Enter your first name: ')
l_name = input('Enter your last name: ')
age_input = input('Enter your age: ')

# Convert age to integer for numerical comparison
try:
    age = int(age_input)
    if age <= 30:
        print('Hello Young Star!')
    else:
        print('welcome ' + f_name)
except ValueError:
    print('Please enter a valid age as a number')