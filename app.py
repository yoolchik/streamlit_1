import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = st.cache_data(pd.read_csv)("data/salaries.csv")
df.work_year = df.work_year.astype('int')

## Sidebar filters
show_data = st.sidebar.checkbox('Show raw data', value=True)
st.sidebar.title("Filters")
experience_level = st.sidebar.multiselect(
    'Choose experience level',
    df['experience_level'].unique(),
    ['SE', 'EX']
)
st.sidebar.caption("EN = Entry-level / Junior  \n"
                   "MI = Mid-level / Intermediate  \n"
                   "SE Senior-level / Expert  \n"
                   "EX Executive-level / Director  \n")

job_title = st.sidebar.multiselect(
    'Choose job title',
    df['job_title'].unique(),
    ['Data Scientist', 'Machine Learning Engineer']
)

year_list = df.work_year.unique()
year_selection = st.sidebar.slider('Select year', 2020, 2024, (2020, 2024))
year_selection_list = list(np.arange(year_selection[0], year_selection[1] + 1))

## Main part
st.title("Data Science Job Salaries")
st.divider()
st.info(
    """
    Dataset could be found here: https://www.kaggle.com/datasets/abhinavshaw09/data-science-job-salaries-2024
    """
)

filtred = df[(df['experience_level'].isin(experience_level)) & (df['job_title'].isin(job_title)) & (
    df['work_year'].isin(year_selection_list))]

if show_data == True:
    st.subheader('Raw data')
    st.write(filtred)

# Plot
fig = px.scatter(filtred, x='employee_residence', y='salary_in_usd')
st.plotly_chart(fig)
