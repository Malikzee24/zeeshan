print("How many rows you want?")
rows = int(input())
print("Choose any single option: 1 = True or 0 = False")
stars = int(input())

# Creating Boolean Function:

numbers_of_stars = bool(stars)

if numbers_of_stars == True:
  for numbers_of_rows in range(1, rows + 1):                # Taking numbers of rows
    for numbers_of_star in  range(1, numbers_of_rows + 1):  # Taking numbers of stars
      print("*", end = " ")
     print()
    
elif number_of_stars == False:
  for numbers_of_rows in range(rows, 0, -1):               # Taking numbers of rows
    for numbers_of_star in range(1, numbers_of_rows + 1):  # Taking numbers of stars
      print("*", end = " ")
     print()
