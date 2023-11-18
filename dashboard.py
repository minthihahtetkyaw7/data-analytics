import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('cardio_data_processed.csv')

# Sidebar for filters
st.sidebar.title('Filters')
selected_gender = st.sidebar.selectbox('Select Gender', ['All', 'Female', 'Male'])

# Apply filters
if selected_gender != 'All':
    df = df[df['gender'] == (1 if selected_gender == 'Female' else 2)]

# Display the dataset
st.title('Cardiovascular Disease Dataset')
st.write(df)

# Statistics and visualizations
st.title('Data Statistics and Visualizations')

# Summary statistics
st.write(df.describe())

# Bar plot of cardiovascular disease presence by gender
gender_counts = df['gender'].map({1: 'Female', 2: 'Male'})
st.subheader('Cardiovascular Disease Presence by Gender')
sns.countplot(x='cardio', hue=gender_counts, data=df)
st.pyplot()

# Scatter plot of age vs. BMI
st.subheader('Age vs. Body Mass Index (BMI)')
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age_years', y='bmi', hue='cardio', data=df)
plt.xlabel('Age (years)')
plt.ylabel('BMI')
st.pyplot()

# Blood pressure categories pie chart
st.subheader('Blood Pressure Category Distribution')
bp_category_counts = df['bp_category'].value_counts()
st.write(bp_category_counts)
plt.figure(figsize=(6, 6))
bp_category_counts.plot(kind='pie', autopct='%1.1f%%')
plt.ylabel('')
st.pyplot()
