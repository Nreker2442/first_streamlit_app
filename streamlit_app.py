import streamlit

streamlit.title('Our New Coffee Shop')

streamlit.header('Drink Menu')
streamlit.text('Pourover')
streamlit.text('Drip')
streamlit.text('Americano')
streamlit.text('Cortado')


streamlit.header('Food Menu')
streamlit.text('🐔 Blueberry Scone')
streamlit.text('🥑 Chocolate Chip Cookie')
streamlit.text('🥗 Banana Bread')
streamlit.text('🥣 Granola Bar')

streamlit.title('🍌🥭 Build Your Own Smoothie Bowl 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# put a picklist here for customers to choose their smoothie ingredients
streamlit.multiselect("Pick your fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

streamlit.dataframe(my_fruit_list)


