import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

all_df = pd.read_csv('all_data.csv')

st.title("Bike Sharing Data Analysis")
st.markdown("### Questions")
st.markdown("- Which season has the highest bike rental count?")
st.markdown("- Which month has the highest bike rental count?")

t1, t2 = st.tabs(["Question 1", "Question 2"])

with t1:
    st.subheader("Which season has the highest bike rental count?")
    season_df = all_df.groupby('season')['cnt'].max().reset_index()
    formatted_season = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    season_df['season'] = season_df['season'].map(formatted_season)
    
    fig = plt.figure(figsize=(12,6))
    sns.barplot(x='season', y='cnt', data=season_df)
    plt.title('Highest Bike Rental Count per Season (2011 & 2012)')
    plt.xlabel('Season')
    plt.ylabel('Max Rental Count')
    st.pyplot(fig) 
    
    st.markdown("### Answer")
    st.markdown("- Fall season has the highest bike rental count, so focusing on trying to rent bikes in the fall season might be a good strategy to gain more profits.")

with t2:
    st.subheader("Which month has the highest bike rental count?")
    month_df = all_df.groupby('mnth')['cnt'].max().reset_index()
    formatted_month = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    month_df['mnth'] = month_df['mnth'].map(formatted_month)
    
    fig = plt.figure(figsize=(12,6))
    sns.barplot(x='mnth', y='cnt', data=month_df)
    plt.title('Highest Bike Rental Count per Month (2011 & 2012)')
    plt.xlabel('Month')
    plt.ylabel('Max Rental Count')
    st.pyplot(fig)

    st.markdown("### Answer")
    st.markdown("- September has the highest bike rental count, so focusing on trying to rent bikes in September might be a good strategy to gain more profits as well.")