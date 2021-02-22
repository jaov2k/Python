if __name__ == "__main__":

    #Prompt user for their hours; need to convert from str to int
    number_of_hours = input("Please Eneter the number of hours that you worked: ")
    number_of_hours = int(number_of_hours)

    #Assuming 24 hours in a day
    #TODO: #1 handle situation when hours is negative
    percentage_of_day = number_of_hours / 24 * 100

    print(f"The percentage of the day you worked is {percentage_of_day}%")