import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

streamlit.title('🍌🥭 Build Your Own Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# put a picklist here for customers to choose their smoothie ingredients
fruits_selected = streamlit.multiselect("Pick your fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#create a function
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  sreamlit.error()
  
streamlit.write('The user entered', fruit_choice)

streamlit.header("View Our Fruit List - Add Your Favorites!")
#function
def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
            my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
            return my_cur.fetchall()

#add button to load the fruit
if streamlit.button('Get Fruit Load List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_Load_list()
      my_cnx.close()
      streamlit.dataframe(my_data_rows)

#allow end user to add fruit to the list
def insert_row_snowflake(new_fruit):
      with my_cnx.cursor() as my_cur:
            my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')")
            return "Thanks for adding " + new-fruit

#my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
