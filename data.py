import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns




def app(df):
	st.subheader('Visualise Data')
	st.set_option('deprecation.showPyplotGlobalUse', False)
	
	st.subheader('Visualisation Selector')
	plots = st.multiselect('Select plot',('pie chart','count plot','boxplot'))
	if 'pie chart' in plots:
		st.subheader('Pie chart')
		pieselect = st.selectbox('Income or Gender?',('Income','Gender'))
		if pieselect == 'Income':
			plt.figure(figsize=(20,5))
			piedata = df['income'].value_counts()
			plt.pie(piedata,labels=piedata.index,autopct='%1.2f%%')
			st.pyplot()
		else:
			plt.figure(figsize=(20,5))
			piedata = df['gender'].value_counts()
			plt.pie(piedata,labels=piedata.index,autopct='%1.2f%%')
			st.pyplot()			

	if 'boxplot' in plots:
		st.subheader('Box plot')
		boxselect = st.selectbox('Income or Gender',('Income','Gender'))
		if boxselect == 'Income':
			plt.figure(figsize=(20,5))
			sns.boxplot(df['hours-per-week'],df['income'])
			st.pyplot()	
		else:
			plt.figure(figsize=(20,5))
			sns.boxplot(df['hours-per-week'],df['gender'])
			st.pyplot()	


	if 'count plot' in plots:
		st.subheader('Count plot for work classes')
		plt.figure(figsize=(20,5))
		sns.countplot(df['workclass'])
		st.pyplot()