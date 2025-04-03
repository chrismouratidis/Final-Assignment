# Final-Assignment
This project is designed to simulate a full workflow of a Data Analyst from getting data off the Database to manipulate it with the use of Python and Pandas module to present it through matplotlib module or Tableau.


The concept is that we are given a dataset that contains Liquor Sales in the state of Iowa in USA between 2012-2020 and we are asked to find the most popular item per zipcode and the percentage of sales per store in the period between 2016-2019.

We are also asked to visualize the Data and present them in either a matplotlib format or in Tableau Public.

Every calculation and transformation of Data has to happen through a Python Script. 

## Final Assignment by Christos Mouratidis


- ###### Step 1.

I used  the command 'select * from   `finance_liquor_sales`  where   YEAR(`date`) BETWEEN 2016 AND 2019;' in MySQL to choose all the elements of the table from 2016-2019 

- ###### Step 2.

I exported them to a csv file data_assignment2.csv

- ###### Step 3.
I grouped the data using pandas in the python file  calculating the total bottled sold by zip code and used scatter plot to visualize them (matplotlib.pyplot). I changed the colour of the plot after every 100 zip codes (bottles_sold_per_zipcode.png).

- ###### Step 4.

I calculated the total sales of all stored and then the total sales by each store.Then I found the % of total sales by each store 

'total_sales = data['sale_dollars'].sum()
store_sales = data.groupby([ 'store_name'])['sale_dollars'].sum().reset_index()
store_sales['sales_percentage'] = (store_sales['sale_dollars'] / total_sales) * 100'

- ###### Step 5.
Finally i visualise the %sales per store with a simple bar plot (percentage_of_totsales_per_store.png)


