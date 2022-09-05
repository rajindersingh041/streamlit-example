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

st.area_chart(chart_data, color = 'green')
