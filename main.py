import streamlit as st
import pandas as pd

st.title('Elefant carpaccio')

# Input
price = st.number_input('Price', min_value=0.0, value=0.0)

n_items = st.number_input('Number of items', min_value=0, value=0)

# insert country
country = st.text_input('Country', 'TX')

discount_df = pd.read_csv('discounts.csv', index_col='order_value')

taxes_df = pd.read_csv('taxes.csv', index_col='state')

discount_df["discount_rate"] = discount_df["discount_rate"].apply(lambda x: f"{(x*100):.2f} %")
taxes_df["tax_rate"] = taxes_df["tax_rate"].apply(lambda x: f"{(x*100):.2f} %")


st.write(discount_df)
st.write(taxes_df)


# Output
st.write(f'Price: {(price*n_items):.2f} $')
