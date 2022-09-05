from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
## Welcome to Rajinder Singh Algo engine tool!

"""
chart_data = pd.DataFrame(
     np.random.randn(20, 1),
     columns=['a'])

series = pd.DataFrame({
  'year': ['2010', '2011', '2012', '2013','2010', '2011', '2012', '2013'],
  'animal': ['antelope', 'antelope', 'antelope', 'antelope', 'velociraptor', 'velociraptor', 'velociraptor', 'velociraptor',],
  'count': [8, 6, 3, 1, 2, 4, 5, 5]
})

# Basic Altair line chart where it picks automatically the colors for the lines
basic_chart = alt.Chart(series).mark_line().encode(
    x='year',
    y='count',
    color='animal',
    # legend=alt.Legend(title='Animals by year')
)

# Custom Altair line chart where you set color and specify dimensions
custom_chart = alt.Chart(series).mark_line().encode(
    x='year',
    y='count',
    color=alt.Color('animal',
            scale=alt.Scale(
                domain=['antelope', 'velociraptor'],
                range=['blue', 'red'])
                )
).properties(
    width=900,
    height=500
)

st.altair_chart(basic_chart)
st.altair_chart(custom_chart)

import altair as alt
import pandas as pd
import numpy as np

x = np.linspace(0, 100, 1000)
y = np.sin(x)
df = pd.DataFrame({'x': x, 'y': y})

t = alt.Chart(df).transform_calculate(
    negative='df.y < 0'
).mark_area().encode(
    x='x',
    y=alt.Y('y', impute={'value': 0}),
    color='negative:N'
)

st.dataframe(df)
st.altair_chart(t)
