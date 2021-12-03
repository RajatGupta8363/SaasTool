# Import all the necessary libraries
from matplotlib import pyplot
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

# Include important bootstrap cdn meta library
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# Navbar using bootstrap
st.markdown("""

<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="#" target="_blank">Saas Tool</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_blank">File Sharing</a>
      </li>
    </ul>
  </div>
</nav>

""", unsafe_allow_html=True)


app = MultiApp()

st.markdown("""
<html>
<body>
<h1 style='color:Red;font-size:30px;'><b>📊Visualization And Prediction Become Easy<b></h1>
<pre>This Web app allows you to do Exploratory data analysis.💹
This Web app helps user to predict his sales.📈
It turns your excel sheet into a intercative dashboard.💻
Sharing any files/data become easy with this app.🗂️
</pre>
</body>
</html>
""",unsafe_allow_html=True)


# Add all your application here
app.add_app("Sales Prediction", home.app)
app.add_app("Perform EDA", data.app)
app.add_app("Excel to Intercative Dashboard", model.app)


# The main app
app.run()
