import streamlit as st
import pandas as pd

st.set_page_config(page_title="Opportunities < KIIT TNP", page_icon='assets/logo.png', layout='wide')

st.title('Open Opportunity Lookup')
# Load data from CSV file
data = pd.read_csv('assets/jobs.csv')

# Get column names
column_names = data.columns.tolist()

# Add search functionality
search_term = st.text_input('Search')
search_column = st.selectbox('Search in column', column_names)
data[search_column] = data[search_column].astype(str)  # Convert column to string type
filtered_data = data[data[search_column].str.contains(search_term, case=False)]

# Add sort functionality
sort_column = st.selectbox('Sort by', column_names)
sort_order = st.radio('Sort order', ('Ascending', 'Descending'))

if sort_order == 'Ascending':
    sorted_data = filtered_data.sort_values(sort_column, ascending=True)
else:
    sorted_data = filtered_data.sort_values(sort_column, ascending=False)

# Add pagination
page_size = st.slider('Rows per page', min_value=1, max_value=len(sorted_data), value=10)
page_number = st.number_input('Page number', min_value=1, max_value=len(sorted_data) // page_size + 1, value=1)

start_index = (page_number - 1) * page_size
end_index = start_index + page_size
paginated_data = sorted_data.iloc[start_index:end_index]

# Display the table
st.dataframe(paginated_data)

# Add load more functionality
if end_index < len(sorted_data):
    if st.button('Load More'):
        page_number += 1

# Hide Streamlit menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
