# Name:         Ivana Pejicic
# Date:         04-08-2022
# Description:  This challenge reads from the text file that contains weekly average prices for a gallon
#               of gas in the United States from April 5th, 1993 through August 26, 2013 and displays menu with options
#               for calculating: average per year, average per month, highest and lowest for each year and also
#               sorting file by price from lowest to highest and then from highest to lowest...

# function that takes month number and returns month name...
def month_name(month_num):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[month_num-1]

# function that validates user's input...
def validate_user_input(prompt_msg, invalid_input_msg, out_of_range_msg):
    while True:
        try:
            value = int(input(prompt_msg))
        except ValueError:
            print(invalid_input_msg)
            continue
        else:
            if value < 1 or value > 6:
                print(out_of_range_msg)
                continue
            else:
                break
    return value

# function that displays menu options...
def display_menu():
    print("Welcome to COP 1047 Gas Prices Analyzer")
    print("Please choose from the following options:")
    print("1. Average Price Per Month")
    print("2. Average Price Per Year")
    print("3. Highest/Lowest Prices Per Year")
    print("4. List of Prices, from Low to High")
    print("5. List of Prices, from High to Low")
    print("6. Exit")

# function that reads file's contents and displays the right output based on user's choice...
def menu_options(users_input):
  infile = open('GasPrices.txt', 'r')
  file_list = infile.readlines()
  infile.close()
  for i in file_list:
    i = i.strip()
  if users_input == 1:
    average_per_month(file_list)
  elif users_input == 2:
    avg_per_year(file_list)
  elif users_input == 3:
    highest_and_lowest(file_list)
  elif users_input == 4:
    low_to_high(file_list)
  elif users_input == 5:
    high_to_low(file_list)
  display_menu()

# function that calculates and displays average for every month...
def average_per_month(file_list):
    previous_year = None
    previous_month = None
    i = 0
    list_of_months = []

    for data in file_list:
        price = float(data[11:])
        year = int(data[6:10])
        month = int(data[0:2])

        if previous_month is None:
            list_of_months.append([month, year, price, 1])
            previous_month = month
            previous_year = year
        elif previous_month == month and previous_year == year:
            list_of_months[i][2] += price
            list_of_months[i][3] += 1
        else:
            i += 1
            previous_month = None
            previous_year = None

    for month in list_of_months:
        avg = round(month[2] / month[3], 2)
        print(f"Average price for {month_name(month[0])}, {month[1]}: ${avg:.2f}")

# function that calculates and displays the average for each year ...
def avg_per_year(file_list):
    list_of_sums = [0] * 21
    list_of_counts = [0] * 21
    for data in file_list:
        price = float(data[11:])
        year = int(data[6:10])
        list_of_sums[year - 1993] += price
        list_of_counts[year - 1993] += 1
    for i in range(21):
        print(f"The average price in {i + 1993} was ${(list_of_sums[i] / list_of_counts[i]):.2f}")

# function that displays lowest and highest price for each year...
def highest_and_lowest(file_list):
    previous_year = None
    list_of_years = []
    for data in file_list:
        price = float(data[11:])
        year = int(data[6:10])

        if year == previous_year:
            list_of_years[year - 1993].append(price)
        else:
            list_of_years.append([year, price])
            previous_year = year

    for i in range(len(list_of_years)):
        year = list_of_years[i][0]
        prices = list_of_years[i][1:]
        highest = max(prices)
        print(f"Highest price for {year}: ${highest:.2f}")

    for i in range(len(list_of_years)):
        year = list_of_years[i][0]
        prices = list_of_years[i][1:]
        lowest = min(prices)
        print(f"Lowest price for {year}: ${lowest:.2f}")


def low_to_high(file_list):
    sorted_list = []
    output_file = open('low_to_high.txt', 'w')
    # building a 2D list ....
    for index in file_list:
        date = index[:10]
        price = float(index[11:])
        sorted_list.append([date,price])
    # using bubble sort for 2D list ...
    length = len(sorted_list)
    for i in range(length - 1):
      for j in range(0, length - i - 1):
        if sorted_list[j][1] > sorted_list[j+1][1]:
          sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    # writing sorted list to a file ...
    for i in sorted_list:
      output_file.write(str(i[0]) + ":" + str(i[1]) + "\n")
    output_file.close()
    print("Please see the low_to_high.txt file")


def high_to_low(file_list):
    sorted_list = []
    output_file = open('high_to_low.txt', 'w')
    # building a 2D list ....
    for index in file_list:
        date = index[:10]
        price = float(index[11:])
        sorted_list.append([date,price])
    # using bubble sort for 2D list ...
    length = len(sorted_list)
    for i in range(length - 1):
      for j in range(0, length - i - 1):
        if sorted_list[j][1] < sorted_list[j+1][1]:
          sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    # writing sorted list to a file ...
    for i in sorted_list:
      output_file.write(str(i[0]) + ":" + str(i[1]) + "\n")
    output_file.close()
    print("Please see the high_to_low.txt file")


def main():
  display_menu()
  prompt = 'Your choice: '
  invalid = 'Error. Please enter an integer'
  out_of_range = 'Error. Choice out of range.'
  user_choice = validate_user_input(prompt, invalid, out_of_range)
  keep_going = True
  while keep_going:
    if user_choice == 6:
      print("Thank you for using COP 1047 Gas Prices Analyzer\nHave a nice day!")
      keep_going = False
    else:
      menu_options(user_choice)
      user_choice = validate_user_input(prompt, invalid, out_of_range)


main()