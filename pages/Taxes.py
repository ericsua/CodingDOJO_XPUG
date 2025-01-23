import streamlit as st
import pandas as pd


st.title('Taxes')

taxes_df = pd.read_csv('taxes.csv', index_col='state')


# Optionally, display the discount and tax tables
taxes_df["tax_rate"] = taxes_df["tax_rate"].apply(lambda x: f"{(x*100):.2f} %")

st.write(taxes_df)