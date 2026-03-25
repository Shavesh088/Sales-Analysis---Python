import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("sales_data_500_rows.csv")

# 2. View first rows
print(df.head())

# 3. Check shape
print(df.shape)

# 4. Column names
print(df.columns)

# 5. Data types
print(df.dtypes)

# 6. Check null values
print(df.isnull().sum())

# 7. Drop nulls
df.dropna(inplace=True)

# 8. Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# 9. Create Revenue column
df['Revenue'] = df['Price'] * df['Quantity']

# 10. Total revenue
print("Total Revenue:", df['Revenue'].sum())

# 11. Average revenue
print("Average Revenue:", df['Revenue'].mean())

# 12. Max revenue
print("Max Revenue:", df['Revenue'].max())

# 13. Min revenue
print("Min Revenue:", df['Revenue'].min())

# 14. Unique products
print(df['Product'].nunique())

# 15. Top selling product
print(df.groupby('Product')['Quantity'].sum().idxmax())

# 16. Least selling product
print(df.groupby('Product')['Quantity'].sum().idxmin())

# 17. Sales by category
print(df.groupby('Category')['Revenue'].sum())

# 18. Sales by city
print(df.groupby('City')['Revenue'].sum())

# 19. Sales by payment mode
print(df.groupby('Payment')['Revenue'].sum())

# 20. Average rating
print(df['Rating'].mean())

# 21. Best rated product
print(df.groupby('Product')['Rating'].mean().idxmax())

# 22. Add Month column
df['Month'] = df['Date'].dt.month

# 23. Monthly revenue
monthly = df.groupby('Month')['Revenue'].sum()
print(monthly)

# 24. Highest sales month
print(monthly.idxmax())

# 25. Lowest sales month
print(monthly.idxmin())

# 26. Sort by revenue
print(df.sort_values(by='Revenue', ascending=False).head())

# 27. Filter high revenue (>50000)
high_sales = df[df['Revenue'] > 50000]
print(high_sales.head())

# 28. Discount impact
df['Discounted_Price'] = df['Price'] - (df['Price'] * df['Discount']/100)

# 29. Correlation
print(df[['Price', 'Quantity', 'Revenue']].corr())

# 30. Revenue by product (bar chart)
df.groupby('Product')['Revenue'].sum().plot(kind='bar')
plt.title("Revenue by Product")
plt.show()

# 31. City sales (pie chart)
df.groupby('City')['Revenue'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("City Sales Distribution")
plt.show()

# 32. Monthly trend (line chart)
monthly.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.show()

# 33. Top 5 transactions
print(df.nlargest(5, 'Revenue'))

# 34. Bottom 5 transactions
print(df.nsmallest(5, 'Revenue'))

# 35. Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("Analysis Completed by SHARVESH")
