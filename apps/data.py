import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def app():
    def calling_Auto(df):
        # import seaborn as sns
        # df=sns.load_dataset('planets')
        import dtale
        from dtale.views import startup
        from dtale.app import get_instance
        startup(data_id="1", data=df)
        df = get_instance("1").data
        components.html("<html><body><iframe src='/dtale/main/1' style='height:1000px;width:1000px;' /></body></html>")
        st.markdown("<a href=/dtale/main/1 class='btn btn-outline-success' target='_blank'>Exploratory Data Analysis</a>", unsafe_allow_html=True)
        #components.html("<a href=/dtale/main/1 class='btn btn-primary' target='_blank'>Exploratory Data Analysis</a>")

    st.set_option('deprecation.showfileUploaderEncoding',False)
    st.sidebar.title("Upload Any File To Do EDA")
    uploaded_file=st.sidebar.file_uploader(label="Upload your Csv or Excel file.",type=['csv','xlsx'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)  
        st.dataframe(df)

    
    if st.sidebar.button('Start The Operation'):
        calling_Auto(df)
