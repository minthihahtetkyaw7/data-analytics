import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
# Load the dataset
df = pd.read_csv('cardio_data_processed.csv')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Cardiovascular Disease Dashboard')

# Sidebar for filters
st.sidebar.title('Filters')
selected_gender = st.sidebar.selectbox('Select Gender', ['All', 'Female', 'Male'])
selected_cardio = st.sidebar.selectbox('Select Cardio Presence', ['All', 'Yes', 'No'])
age_range = st.sidebar.slider('Select Age Range (Years)', min_value=df['age_years'].min(), max_value=df['age_years'].max(), value=(df['age_years'].min(), df['age_years'].max()))

if st.sidebar.button('Reset Filters'):
    selected_gender = 'All'
    selected_cardio = 'All'

# Apply filters
if selected_gender != 'All':
    df = df[df['gender'] == (1 if selected_gender == 'Female' else 2)]

if selected_cardio != 'All':
    df = df[df['cardio'] == (1 if selected_cardio == 'Yes' else 0)]

df = df[(df['age_years'] >= age_range[0]) & (df['age_years'] <= age_range[1])]

with st.spinner(text='In progress'):
    time.sleep(3)

col1, col2 = st.columns(2)


with col1:
    plt.figure(figsize=(10, 6))
    gender_counts = df['gender'].map({1: 'Female', 2: 'Male'})
    st.subheader('Cardiovascular Disease Presence by Gender')
    sns.countplot(x='cardio', hue=gender_counts, data=df)
    st.pyplot()

    plt.figure(figsize=(10, 6))
    cardio_counts = df['cardio'].map({1: 'Yes', 0: 'No'})
    st.subheader('Cardiovascular Disease by Blood Pressure Category')
    sns.countplot(x='bp_category', hue=cardio_counts, data=df, palette="Set2")
    st.pyplot()

    st.subheader('Cardiovascular Disease by Systolic & Diastolic Blood Pressure')
    sns.scatterplot(x='ap_hi', y='ap_lo', hue='cardio', data=df)
    plt.xlabel('Systolic Blood Pressure (ap_hi)')
    plt.ylabel('Diastolic Blood Pressure (ap_lo)')
    plt.title('Scatter Plot of Blood Pressure')
    st.pyplot()


with col2:
    plt.figure(figsize=(10, 6))
    st.subheader('Age vs. Cardio')
    sns.countplot(data=df, x='age_years', hue='cardio', palette="Set1")
    plt.xlabel('Age (years)')
    plt.ylabel('Count')
    plt.title('Age vs Cardiovascular Disease')
    st.pyplot()

    cholesterol_gluc_cardio = pd.crosstab([df['cholesterol'], df['gluc']], df['cardio'])
    st.subheader('Cholesterol & Glucose vs. Cardio')
    cholesterol_gluc_cardio.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Cholesterol and Glucose Levels by Cardiovascular Disease')
    plt.xlabel('Cholesterol and Glucose Levels')
    plt.ylabel('Count')
    plt.legend(title='Cardiovascular Disease')
    st.pyplot()







