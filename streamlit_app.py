from time import sleep
import streamlit as st
import pandas as pd
import numpy as np
import datetime
st.title('My Strategy')

col1, col2, col3 = st.columns(3)
with col1:
	entry = st.time_input('Entry time', datetime.time(9, 25))
with col2:
	exit = st.time_input('exit time', datetime.time(15, 0))
with col3:
	capital = st.number_input('Enter capital', min_value = 100, value = 100000, step = 100)

paper = st.checkbox('Paper trading', True, help = 'Turn on paper trading')

col4, col5, col6, col7 = st.columns(4)

with col4:
	s1 = st.selectbox("Symbol1 select OHLC", options = ('Open', 'High', 'Low', 'Close'))
with col5:
	s2 = st.selectbox("Symbol2 select OHLC", options = ('Open', 'High', 'Low', 'Close'))
with col6:
	s3 = st.selectbox("Symbol3 select OHLC", options = ('Open', 'High', 'Low', 'Close'))
with col7:
	candle_length = st.number_input("Enter candle length", min_value = 1, value = 5, step = 1)


uploaded_file = st.file_uploader("Upload symbol combination")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


run = st.button("Click me to run the strategy")

if run:
	total_pnl = 0
	n = [np.random.randint(-1000,1000) for x in range(1000)]
	dt  = datetime.datetime.now()
	# dt = pd.date_range(start = dt, freq = '1min', period = 1000)
	dt = pd.date_range(start = dt, periods = 1000, freq = '1min')
	# st.text(n)
	# st.text(dt)
	df = pd.DataFrame({'dt':dt, 'pnl':n})
	# for i in range(1000):
	# 	total_pnl += n[i]
	# 	# st.line_chart(total_pnl)
	# 	# slee(1)
	# st.text(total_pnl)
	# st.line_chart(x = dt, y = n)
	# st.table(df)
	st.line_chart(df, x = 'dt', y = 'pnl')
# if agree:
#     st.write('Great!')
# # st.write('Alarm is set for', t)

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
