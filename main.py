import streamlit as st
import pandas as pd

st.title('Elefant Carpaccio')

# Input
price = st.number_input('Price', min_value=0.0, value=0.0)
n_items = st.number_input('Number of items', min_value=0, value=0)
country = st.text_input('Country', 'TX')

total_price = price * n_items
st.write(f'Price: {total_price:.2f} $')

# Read discount and tax CSVs
discount_df = pd.read_csv('discounts.csv', index_col='order_value')
taxes_df = pd.read_csv('taxes.csv', index_col='state')

# 1. Discount Calculation
# Check if total price is above the discount thresholds
discount_rate = 0  # Default no discount
for i in range(len(discount_df)):
    if total_price < discount_df.index[i]:
        # Apply discount from the previous row
        discount_rate = discount_df.iloc[i-1, 0] if i > 0 else 0
        break
    else:
        # Use the last available discount rate if price is above all thresholds
        discount_rate = discount_df.iloc[-1, 0]

# Apply discount to the total price
discount_value = total_price * discount_rate
total_after_discount = total_price - discount_value

st.write(f'Discount: {discount_rate:.2f} %')
st.write(f'Discount Value: {discount_value:.2f} $')
st.write(f'Total after Discount: {total_after_discount:.2f} $')

# 2. Taxes Calculation
# Check if country exists in the taxes DataFrame
if country in taxes_df.index:
    tax_rate = taxes_df.loc[country, "tax_rate"]
    tax_value = total_after_discount * tax_rate
    total_after_tax = total_after_discount + tax_value
    st.write(f'Tax: {tax_rate*100:.2f} %')
    st.write(f'Tax Value: {tax_value:.2f} $')
    st.write(f'Total after Tax: {total_after_tax:.2f} $')
else:
    st.write(f'No tax data available for country {country}')

# Optionally, display the discount and tax tables
discount_df["discount_rate"] = discount_df["discount_rate"].apply(lambda x: f"{(x*100):.2f} %")
taxes_df["tax_rate"] = taxes_df["tax_rate"].apply(lambda x: f"{(x*100):.2f} %")

st.write(discount_df)
st.write(taxes_df)
