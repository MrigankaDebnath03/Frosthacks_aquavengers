# import pandas as pd
# import plotly.express as px

# df = pd.read_csv('predictions Andhra Pradesh.csv')

# # Assuming 'YEAR' is a column in your DataFrame
# df_filtered = df[(df['YEAR'] >= 2024) & (df['YEAR'] <= 2100)]

# fig = px.line(df_filtered, x='YEAR', y='ANNUAL', title='Rainfall predictions from 2024 to 2100')
# fig.show()

import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
df = pd.read_csv('predictions Arunachal Pradesh.csv')

# Filter data
df_filtered = df[(df['YEAR'] >= 2024) & (df['YEAR'] <= 2100)]

# Streamlit app
st.title('Rainfall Predictions from 2024 to 2100')

# Display the data table (optional)
st.dataframe(df_filtered)

# Create a Plotly Express line chart
fig = px.line(df_filtered, x='YEAR', y='ANNUAL', title='Rainfall predictions from 2024 to 2100')

# Display the chart using Streamlit's Plotly chart support
st.plotly_chart(fig)
