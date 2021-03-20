
#Function section

def day_to_units(user_in_num):
    Calculation_of_units =  24
    if user_in_num> 0:
        return (f'{user_in_num} days are {user_in_num * Calculation_of_units} Hours ') 
    elif user_in_num == 0:
        return("You entered a 0, enter correct value...")


def validate_and_execute():
    if user_in.isdigit():
    # user_in_num = int(user_in)
        calculation = day_to_units(int(user_in))
        print(calculation)
    else:
        print("\nYour Input is not a number")


user_in = input ("Hey user !!! \nEnter the number of days : ")
validate_and_execute()



# print(user_input)



# unit = input("Choose the unit which you want (seconds, hours, minutes : ")

# print(unit)



# day_to_units(user_input)