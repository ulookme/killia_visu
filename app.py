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
import streamlit as st
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
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












#WeeklyDemand Data
#st.subheader('transactions')
#st.write(transaction)
#df = pd.DataFrame(transaction[:1000], columns = ['amount'])
#df.hist()
#st.pyplot()






# Value count of target values
if st.checkbox("Show Pie Chart and Value Counts of Target fraud"):
  st.write(transaction.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
  st.pyplot()
  st.write(transaction.iloc[:,-1].value_counts())



#st.subheader('transactions')
#fig1 = px.pie(transaction, values=transaction.fraud, names=transaction.ip_country, color=transaction.ip_country,
#color_discrete_map={'Sendo':'cyan', 'Tiki':'royalblue','Shopee':'darkblue'})
#fig1.update_layout(
#title="<b>Pourcentage de revenus entre les pays concernés </b>")
#st.plotly_chart(fig1)



fig = px.histogram(transaction, x="amount")
fig.update_layout(
title="<b>Distribution des sommes de transactions</b>")
st.plotly_chart(fig)


fig4 = px.histogram(transaction, x="site_name")
fig4.update_layout(
title="<b>Pourcentage les site internets avec le plus de transactions </b>")
st.plotly_chart(fig4)

# Here we use a column with categorical data
fig2 = px.histogram(transaction, x="site_name", y= "fraud")
fig2.update_layout(
title="<b>Les sites internet les plus fraudés </b>")
st.plotly_chart(fig2)

fig5 = px.histogram(transaction, x="amount", color="ip_country")
fig5.update_layout(
title="<b>Les pays qui font le plus de transactions </b>")
st.plotly_chart(fig5)



fig6 = px.scatter_matrix(transaction)
fig6.update_layout(
title="<b> Observation de la matrice des transactions </b>")
st.plotly_chart(fig6)


fig7 = px.scatter_matrix(transaction,
    dimensions=["client_id", "site_name", "card_type", "reference","ip_country","amount"],
    color="fraud")
st.plotly_chart(fig7)

fig8 = px.density_contour(transaction, x="amount", y="fraud")
fig8.update_traces(contours_coloring="fill", contours_showlabels = True)
fig8.update_layout(
title="<b> Densité contours  </b>")
st.plotly_chart(fig8)






import streamlit.components.v1 as components
#st.title('Streamlit Components')
#components.html(
  #"""
     
    #<div class="container">
  #<h2>HackerShrine</h2>
 
   # <div class="card" style="width:400px">
     
    #<div class="card-body ">
      #<form action="/upload" method="post" enctype="multipart/form-data">
      #<p class="card-text">Custom HTML </p>
      #  <input type="file" name="file" value="file">
      #  <hr>
      #<input type="submit" name="upload" value="Upload" class="btn btn-success">
      #</form>
     
    #</div>
  #</div>
  #<br>
#</div>
 #, #""",
    #height=600,
##)





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
