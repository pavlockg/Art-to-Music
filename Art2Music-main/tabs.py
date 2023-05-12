import streamlit as st
import pandas as pd
import numpy as np

def foo():
	print('bar')


st.set_page_config(layout='wide')
st.title('Streamlit Tab Test with Custom Colors')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab2", "Tab3"])

with tab1:
	st.subheader('Widgets')
	st.button('Click me')
	st.checkbox('I agree')

with tab2:
	st.radio('Pick one', ['cats', 'dogs'])
	st.selectbox('Pick one', ['cats', 'dogs'])
	st.multiselect('Buy', ['milk', 'apples', 'potatoes'])

with tab3:
	st.slider('Pick a number', 0, 100,50)
	st.select_slider('Pick a size', ['S', 'M', 'L'])
	st.text_input('First name')