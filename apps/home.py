"""
Name- Rajat Gupta
Licensable
Contact- support@infojio.com
Batch-cs76
Roll-181429
"""
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

def app():
    #-----------------------------------------------------------------------------------
    def calling(df):
        
        ARIMA_DEPRECATION_ERROR = """
        statsmodels.tsa.arima_model.ARMA and statsmodels.tsa.arima_model.ARIMA have
        been removed in favor of statsmodels.tsa.arima.model.ARIMA (note the .
        between arima and model) and statsmodels.tsa.SARIMAX.
        statsmodels.tsa.arima.model.ARIMA makes use of the statespace framework and
        is both well tested and maintained. It also offers alternative specialized
        parameter estimators.
        """
        
        
        
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import warnings
        warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARMA',FutureWarning)
        warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARIMA',FutureWarning)
        warnings.warn(ARIMA_DEPRECATION_ERROR,FutureWarning)
        warnings.filterwarnings("ignore")
        
        # df=pd.read_csv('perrin-freres-monthly-champagne-.csv')
        # df.head()
        
        # df.tail()
        
        ## Cleaning up the data
        df.columns=["Month","Sales"]
        # df.head()
        
        ## Drop last 2 rows
        df.drop(106,axis=0,inplace=True)
        
        # df.tail()
        
        df.drop(105,axis=0,inplace=True)
        
        # df.tail()
        
        # Convert Month into Datetime
        df['Month']=pd.to_datetime(df['Month'])
        
        # df.head()
        
        df.set_index('Month',inplace=True)
        
        # df.head()
        
        # df.describe()
        
        """## Step 2: Visualize the Data"""
        
        df.plot()
        
        ### Testing For Stationarity
        
        from statsmodels.tsa.stattools import adfuller
        
        test_result=adfuller(df['Sales'])
        
        #Ho: It is non stationary
        #H1: It is stationary
        
        def adfuller_test(sales):
            result=adfuller(sales)
            labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
            for value,label in zip(result,labels):
                print(label+' : '+str(value) )
            if result[1] <= 0.05:
                print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is     stationary")
            else:
                print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")
        
        adfuller_test(df['Sales'])
        
        """## Differencing"""
        
        df['Sales First Difference'] = df['Sales'] - df['Sales'].shift(1)
        
        df['Sales'].shift(1)
        
        df['Seasonal First Difference']=df['Sales']-df['Sales'].shift(12)
        
        # df.head(14)
        
        ## Again test dickey fuller test
        adfuller_test(df['Seasonal First Difference'].dropna())
        
        df['Seasonal First Difference'].plot()
        
        """## Auto Regressive Model
        
        y t = c + ϕ 1 y t − 1 + ϕ 2 y t − 2 + ⋯ + ϕ p y t − p + ε t , where εt is white noise.
        """
        
        from pandas.plotting import autocorrelation_plot
        autocorrelation_plot(df['Sales'])
        #plt.show()
        
        """### Final Thoughts on Autocorrelation and Partial Autocorrelation
        
        * Identification of an AR model is often best done with the PACF.
            * For an AR model, the theoretical PACF “shuts off” past the order of the model.  The phrase “shuts off” means that in theory     the      partial autocorrelationsare equal to 0 beyond that point.
            
            
        * Identification of an MA model is often best done with the ACF rather than the PACF.
            * For an MA model, the theoretical PACF does not shut off, but instead tapers toward 0 in some manner.  
            
            p,d,q
            p AR model lags
            d differencing
            q MA lags
        """
        
        from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
        
        import statsmodels.api as sm
        
        fig = plt.figure(figsize=(12,8))
        ax1 = fig.add_subplot(211)
        fig = sm.graphics.tsa.plot_acf(df['Seasonal First Difference'].iloc[13:],lags=40,ax=ax1)
        ax2 = fig.add_subplot(212)
        fig = sm.graphics.tsa.plot_pacf(df['Seasonal First Difference'].iloc[13:],lags=40,ax=ax2)
        
        # For non-seasonal data
        #p=1, d=1, q=0 or 1
        # import statsmodels.tsa.arima_model as ARIMA
        # model=ARIMA(df['Sales'],order=(1,1,1))
        # model_fit=model.fit()
        
        # model_fit.summary()
        
        # df['forecast']=model_fit.predict(start=90,end=103,dynamic=True)
        # df[['Sales','forecast']].plot(figsize=(12,8))
        
        import statsmodels.api as sm
        
        model=sm.tsa.statespace.SARIMAX(df['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
        results=model.fit()
        
        df['forecast']=results.predict(start=90,end=103,dynamic=True)
        df[['Sales','forecast']].plot(figsize=(12,8))
        
        from pandas.tseries.offsets import DateOffset
        future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,24)]
        
        future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
        
        future_datest_df.tail()
        
        future_df=pd.concat([df,future_datest_df])
        
        future_df['forecast'] = results.predict(start = 104, end = 120, dynamic= True)  
        future_df[['Sales', 'forecast']].plot(figsize=(12, 8))
        st.write(future_df['forecast'].iloc[104:121])
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(plt.show())
        st.balloons()
    #------------------------------------------------
    
    
        
    st.set_option('deprecation.showfileUploaderEncoding',False)
    # file uploading attribute and prediction
    st.sidebar.title("Upload File For Prediction")
    uploaded_file=st.sidebar.file_uploader(label="Upload your Csv or Excel file.",type=['csv','xlsx'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        st.success("File Uploaded Successfully")
    st.sidebar.title("Press Below For Prediction")
    if st.sidebar.button('Predict'):
        calling(df)
    #-------------------------------------------------
    #file downloading structure

    Data_file=pd.read_csv('perrin-freres-monthly-champagne-.csv')
    @st.cache
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(Data_file)
    st.sidebar.title("Customize Your own Data")
    st.sidebar.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='perrin-freres-monthly-champagne-.csv',
        mime='text/csv',
        )

    #--------------------------------------------------