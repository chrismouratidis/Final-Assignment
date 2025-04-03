
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the URL
url = r'C:\Users\chris\OneDrive\Έγγραφα\data_assignment2.csv'  # Make sure to use raw string notation for Windows file paths

# Load the data
data = pd.read_csv(url)

# Calculate total bottles sold per zip code
tot_bottles_per_zip = data.groupby('zip_code')['bottles_sold'].sum().reset_index()
# Print the total bottles sold per zip code
print("\nTotal Bottles Sold per Zip Code:")
print(tot_bottles_per_zip)
# Create a scatter plot with different colors for each zip code
plt.figure(figsize=(10, 6))
plt.scatter(tot_bottles_per_zip['zip_code'], tot_bottles_per_zip['bottles_sold'],
            c=tot_bottles_per_zip['zip_code'], cmap='tab20', edgecolors='k', s=100)

# Adding labels and title
plt.xlabel('Zip Code')
plt.ylabel('Total Bottles Sold')
plt.title('Total Bottles Sold per Zip Code')
plt.colorbar(label='Zip Code')

# Show the plot
plt.xticks(rotation=45)  # Rotate zip codes if necessary for readability
plt.tight_layout()
plt.show()



# Calculate total sales for all stores
total_sales = data['sale_dollars'].sum()

# Group by store and calculate their individual sales
store_sales = data.groupby([ 'store_name'])['sale_dollars'].sum().reset_index()

# Calculate sales percentage  of each store
store_sales['sales_percentage'] = (store_sales['sale_dollars'] / total_sales) * 100

# Displaying the result
print("\nSales Percentage per Store:")
print(store_sales.sort_values(by='sales_percentage', ascending=False))
# Sorting the data
store_sales = store_sales.sort_values(by='sales_percentage', ascending=False).head(15)

plt.figure(figsize=(12, 8))

# Plotting a horizontal bar chart
bars = plt.barh(store_sales['store_name'], store_sales['sales_percentage'], color='steelblue')
plt.xlabel('%Sales', fontsize=14)
plt.title('%Sales by Store', fontsize=18)
plt.gca().invert_yaxis()

# Adding text labels to each bar
for bar in bars:
    plt.text(
        bar.get_width() + 0.5,  # Position of text slightly to the right of the bar
        bar.get_y() + bar.get_height() / 2,  # Centering the text vertically
        f'{bar.get_width():.1f}%',  # Formatting the percentage with one decimal place
        va='center',  # Vertical alignment
        fontsize=12
    )

plt.show()