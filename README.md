# Pelicia-Mikhail-Anthony-Bennet-D.R.--PA_3
### This is my submission for the third programming assignment

## Problem 1
#### For section a.), the instruction was to read the "cars.csv" file and display its contents. To do this, I first imported the pandas library. I then used pd.read_csv() to load the CSV file into a DataFrame called "cars". Then I printed it by calling "cars".
#### Here's the code that was used
````
cars = pd.read_csv('cars.csv')
cars
````
#### For section b.), the instructions were to display the first and last five rows of the resulting cars. To do this, I used the cars.head and cars.tail which automatically returns the first and last five, respectively.
#### Here's the code that was used
````
cars.head()

cars.tail()
````
## Problem 2
#### For section a.), the instructions were to display the first five rows of odd-numbered columns. The instruction was to print the first five rows of all odd-numbered columns. I used iloc[] with slicing [:, ::2] to select every other column starting from the first column (index 0).
#### Here's the code that was used
````
odd_columns = cars.iloc[:, ::2]
print(odd_columns.head())
````
#### For section b.) Display the row that contains the ‘Model’ of ‘Mazda RX4’. To do this, I used boolean indexing with cars['Model'] == 'Mazda RX4' to search for that specific row.
#### Here's the code that was used
````
mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']
print(mazda_rx4_row)
````
#### For section c.), the instructions were to display the cylinders (cyl) that 'CamaroZ28' has. For this, I used loc[] with a condition to find the specific model and then accessed the 'cyl' column value.
#### Here's the code that was used
````
camaro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print(f"\nCamaro Z28 has {camaro_cyl} cylinders")
````
#### For section d.), the instructions were to determine the cylinders, gear type, and model of the ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’. For this, I first created a list with the models. I then used the .isin() method on the 'Model' column to search for the rows where the models match. and .loc[] was used to search based on the list, and it selected the 'Model', 'cyl', and 'gear' columns.
#### Here's the code that was used
````
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
result = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
print(result)
````

