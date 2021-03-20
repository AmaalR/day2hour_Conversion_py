

#Function section

def day_to_units(user_in_num):

    Calculation_of_units =  24
    return (f'{user_in_num} days are {user_in_num * Calculation_of_units} Hours ') 
        


def validate_and_execute():
    if user_in.isdigit():
        user_in_num = int(user_in)
        if user_in_num > 0:
            calculation = day_to_units(int(user_in_num))
            print(calculation)
        elif user_in_num == 0:
            print("You entered a 0, enter correct value...")
    else:
        print("\nNot Valid Input")


user_in = ""

while user_in != "exit":
    user_in = (input ("\n\nHey user !!! \nEnter the number of days : "))
    validate_and_execute()



