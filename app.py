# -*- coding: utf-8 -*-
"""
Created on 09 Juin 16:02

@author: Hajjar
"""
import seaborn as sns
from sklearn.utils import shuffle
import tornado.ioloop
import tornado.web
import tornado.options
import streamlit as st
import pymongo
from pymongo import MongoClient
import numpy as np
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title(' TRANSACTION FRAUD ANALYSE')

#client = pymongo.MongoClient("mongodb+srv://transac:Mhajjar3@cluster0.hskyz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#db = client.transaction
#col = db.collec1
#data = pd.DataFrame(list(col.find()))
#data = data.drop(columns=["_id"])
#print(data)

@st.cache
def load_data(nrows):
    client = pymongo.MongoClient("mongodb+srv://transac:Mhajjar3@cluster0.hskyz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.transaction
    col = db.collec1
    data = pd.DataFrame(list(col.find()))
    data = data.drop(columns=["_id"])
    data =  shuffle(data, random_state=42)
    data = data.iloc[0:1000]
    # Convert integer valued (numeric) columns to floating point
    numeric_columns = data.select_dtypes(["int64", "float64"]).columns
    data[numeric_columns] = data[numeric_columns].astype("float32")
    #data = pd.read_csv('transaction_simplon.csv', nrows=nrows)
    return data

#@st.cache
#def load_center_data(nrows):
    #data = pd.read_csv('fulfilment_center_info.csv',nrows=nrows)
    #return data

#@st.cache
#def load_meal_data(nrows):
    #data = pd.read_csv('meal_info.csv',nrows=nrows)
    #return data


transaction = load_data(1000)
#center_info_data = load_center_data(1000)
#meal_data = load_meal_data(1000)


#altaire

with st.echo(code_location='below'):
    import altair as alt

    st.write(alt.Chart(transaction).mark_point().encode(
        # The notation below is shorthand for:
        # x = alt.X("Acceleration", type="quantitative", title="Acceleration"),
        x="fraud",

        y=alt.Y("amount", type="quantitative", title="amount fraud quantitative"),
    ))












#WeeklyDemand Data
st.subheader('transactions')
st.write(transaction)
df = pd.DataFrame(transaction[:1000], columns = ['id'])
df.hist()
st.pyplot()






# Value count of target values
if st.checkbox("Show Pie Chart and Value Counts of Target Columns"):
  st.write(transaction.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
  st.pyplot()
  st.write(transaction.iloc[:,-1].value_counts())




    # Correlation plot of dataset
if st.checkbox("Show Correlation Plot"):
  st.write("### Heatmap")
  fig, ax = plt.subplots(figsize=(10,10))
  st.write(sns.heatmap(transaction.corr(), annot=True,linewidths=0.5))
  st.pyplot()






if st.checkbox("card type fraud "):
  st.write("###")
  fig, ax = plt.subplots(figsize=(10,10))
  st.write(sns.barplot(x='card_type', y='fraud', data=transaction))
  st.pyplot()



if st.checkbox("DISTRIBTION FRAUD EN LEGITIME"):
  st.write("### test")
  fig, ax = plt.subplots(figsize=(10,10))
  st.write(sns.stripplot(x=transaction["reference"], y=transaction['fraud'].astype('category'),
             palette=['#bcbddc','#756bb1']))
  st.pyplot()



if st.checkbox("DISTRIBTION TRANSACTION"):
  st.write("### Country distribution")
  fig, ax = plt.subplots(figsize=(10,10))
  st.write(sns.distplot(transaction.ip_country, color='#756bb1'))
  st.pyplot()



import streamlit.components.v1 as components
st.title('Streamlit Components')
components.html(
  """
     
    <div class="container">
  <h2>HackerShrine</h2>
 
    <div class="card" style="width:400px">
     
    <div class="card-body ">
      <form action="/upload" method="post" enctype="multipart/form-data">
      <p class="card-text">Custom HTML </p>
        <input type="file" name="file" value="file">
        <hr>
      <input type="submit" name="upload" value="Upload" class="btn btn-success">
      </form>
     
    </div>
  </div>
  <br>
</div>
 , """,
    height=600,
)





#st.bar_chart(data['checkout_price'])
#st.button('click')
#chart = st.line_chart(data['center_id'])
#
#hist_data = [data['checkout_price'], data['base_price'], data['num_orders']]
#group_labels = ['checkout_price', 'base_price', 'num_orders']
#fig = ff.create_distplot(hist_data,group_labels, bin_size=[.1, .25, .5])
#st.plotly_chart(fig, use_container_width=True)



#from PIL import Image
#image = Image.open('designflow.jpg')
#st.image(image, caption='Sunrise by the mountains', use_column_width=True)

#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)
#
## Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#
#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)