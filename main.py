import streamlit as st

st.title('Elefant carpaccio')

# Input
price = st.number_input('Price', min_value=0.0, value=0.0)

n_items = st.number_input('Number of items', min_value=0, value=0)

# Output
st.write(f'Price: {price*n_items} €')
