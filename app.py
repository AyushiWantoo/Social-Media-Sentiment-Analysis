# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
file_path = 'Time-Wasters on Social Media.csv'  # Adjust path as needed
data = pd.read_csv(file_path)

# Set up Streamlit page configuration
st.set_page_config(page_title="Company Insights Dashboard", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page:", ["Operations Insights", "Sales Insights", "Marketing Insights"])

# Display title and description based on selected page
if page == "Operations Insights":
    st.title("Operations Team Insights")
    st.write("Explore KPIs and insights for the Operations team.")

    # User Distribution by Location
    st.subheader("User Distribution by Location")
    location_data = data['Location'].value_counts()
    st.bar_chart(location_data)

    # Average Income by Location
    st.subheader("Average Income by Location")
    income_location = data.groupby('Location')['Income'].mean()
    st.bar_chart(income_location)

    # Platform Popularity by Location
    st.subheader("Platform Popularity by Location")
    location = st.selectbox("Select a location:", data['Location'].unique())
    platform_data = data[data['Location'] == location]['Platform'].value_counts()
    st.bar_chart(platform_data)

    # Device Type and Connection Type by Location
    st.subheader("Device Type and Connection Type Popularity by Location")
    device_type = data[data['Location'] == location]['DeviceType'].value_counts()
    connection_type = data[data['Location'] == location]['ConnectionType'].value_counts()
    st.write("Device Type Popularity")
    st.bar_chart(device_type)
    st.write("Connection Type Popularity")
    st.bar_chart(connection_type)

elif page == "Sales Insights":
    st.title("Sales Team Insights")
    st.write("View KPIs and insights for optimizing vendor offers on Flipkart.")

    # User Engagement by Platform
    st.subheader("User Engagement by Platform")
    engagement_platform = data.groupby('Platform')['Engagement'].mean()
    st.bar_chart(engagement_platform)

    # Engagement by Video Category
    st.subheader("Engagement by Video Category")
    engagement_category = data.groupby('Video Category')['Engagement'].mean()
    st.bar_chart(engagement_category)

    # Total Time Spent and Session Frequency
    st.subheader("Total Time Spent and Session Frequency")
    total_time_spent = data['Total Time Spent'].sum()
    session_frequency = data['Number of Sessions'].mean()
    st.write(f"Total Time Spent: {total_time_spent}")
    st.write(f"Average Session Frequency: {session_frequency}")

    # Income Segmentation for Targeting
    st.subheader("Income Segmentation for Targeting")
    income_segment = pd.cut(data['Income'], bins=[0, 30000, 60000, 100000, data['Income'].max()],
                            labels=['Low Income', 'Mid Income', 'High Income', 'Very High Income'])
    segment_data = income_segment.value_counts()
    st.bar_chart(segment_data)

elif page == "Marketing Insights":
    st.title("Marketing Team Insights")
    st.write("Analyze user segments and create personalized marketing campaigns.")

    # User Count by Age Group
    st.subheader("User Count by Age Group")
    age_group = pd.cut(data['Age'], bins=[18, 30, 45, 60, 100], labels=['18-30', '30-45', '45-60', '60+'])
    age_data = age_group.value_counts()
    st.bar_chart(age_data)

    # Engagement by Device Type
    st.subheader("Engagement by Device Type")
    device_engagement = data.groupby('DeviceType')['Engagement'].mean()
    st.bar_chart(device_engagement)

    # Addiction Level and Self-Control by Age Group
    st.subheader("Addiction Level and Self-Control by Age Group")
    addiction_by_age = data.groupby(age_group)['Addiction Level'].mean()
    self_control_by_age = data.groupby(age_group)['Self Control'].mean()
    st.write("Average Addiction Level by Age Group")
    st.bar_chart(addiction_by_age)
    st.write("Average Self Control by Age Group")
    st.bar_chart(self_control_by_age)

    # Engagement by Watch Time
    st.subheader("Engagement by Watch Time")
    watch_time_engagement = data.groupby('Watch Time')['Engagement'].mean()
    st.line_chart(watch_time_engagement)
