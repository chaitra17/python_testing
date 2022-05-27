# Sign_up form for a play which involves 4 different roles.
# This is for limited number of participants (here limit is 5) on 1st come 1st serve basis

# Nested dictionary to store responses

auditions = {
    "Principal": {
        },
    "Teacher": {
        },
    "Troublemaker": {
        },
    "Student": {
        }
    }


#  Ask for input, adding response to the nested dictionary and looping signup form
def sign_up():
    # Ask for input

    name = input("what is your name? ").capitalize()

    grade = input('''what is your grade(please respond with a number)''')

    role = input('''what is your preferred role? please select a number from the following options:
                    [1] Principal
                    [2] Teacher
                    [3] Troublemaker
                    [4] Student''')

    if role == '1':
        auditions["Principal"][name] = [grade]
    elif role == '2':
        auditions["Teacher"][name] = [grade]
    elif role == '3':
        auditions["Troublemaker"][name] = [grade]
    else:
        auditions["Student"][name] = [grade]


# For-loop that calls sign_up function
for i in range(5):
    sign_up()

# Print the list of students signed up for audition
print("sign_up for the play is closed")

print("Role : Student")
for i, j in auditions["Principal"].items():
    print(i, j)
print("Role : Student")
for i, j in auditions["Teacher"].items():
    print(i, j)
print("Role : Student")
for i, j in auditions["Troublemaker"].items():
    print(i, j)
print("Role : Student")
for i, j in auditions["Student"].items():
    print(i, j)
