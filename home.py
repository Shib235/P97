import streamlit as st
import numpy as np
import pandas as pd


def app(df):

	st.header('Census visualisation app')
	st.text('''
		This app allows u to visualise census income''')

	st.subheader('View data')
	with st.beta_expander('View dataset'):
		st.table(df.head(300))
	st.subheader('Column description')
	if st.checkbox('Show summary'):
		st.table(df.describe())


	beta_col1,beta_col2,beta_col3 = st.beta_columns(3)
	with beta_col1:
		if st.checkbox('Show column names'):
			st.table(df.columns)
	with beta_col2:
		if st.checkbox('Show column datatypes'):
			st.table(df.dtypes)
	with beta_col3:
		if st.checkbox('View column data'):
			cols = st.selectbox('Select column',(df.columns))
			st.table(df[cols])	