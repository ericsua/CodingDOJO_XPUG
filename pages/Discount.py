import streamlit as st
import pandas as pd


st.title('Discounts')

discount_df = pd.read_csv('discounts.csv', index_col='order_value')


# Optionally, display the discount and tax tables
discount_df["discount_rate"] = discount_df["discount_rate"].apply(lambda x: f"{(x*100):.2f} %")

st.write(discount_df)
