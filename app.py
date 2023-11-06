import streamlit as st
import pandas as pd
import plotly.express as px

unsorted = {
    'selection': [62669.5, 2402.3, 1366.35, 603.364, 25.039, 6.283, 0.289],
    'insertion': [31214.4, 1196.06, 681.529, 298.537, 12.049, 3.204, 0.223],
    'merge': [122.313, 24.616, 17.971, 12.134, 2.276, 1.156, 0.367],
    'quick': [37.851, 6.519, 4.91, 3.17, 0.535, 0.257, 0.044],
    'hybrid': [36.701, 6.289, 4.85, 3.211, 0.52, 0.273, 0.043]
}

sortedTime = {
    'selection': [64685, 2387.21, 1345.63, 605.049, 24.201, 5.835, 0.254],
    'insertion': [0.671, 0.132, 0.099, 0.067, 0.03, 0.006, 0.001],
    'merge': [90.621, 18.436, 13.906, 9.587, 1.787, 0.855, 0.168],
    'quick': [124209, 4932.01, 2778.25, 1231.34, 50.051, 12.349, 0.525],
    'hybrid': [19.352, 2.859, 2.097, 1.382, 0.24, 0.122, 0.023]
}

unsorted_df = pd.DataFrame(unsorted, index=[500000, 100000, 50000, 5000, 1000, 500, 100])
unsorted_df = unsorted_df[::-1]

sorted_df = pd.DataFrame(sortedTime, index=[500000, 100000, 50000, 5000, 1000, 500, 100])
sorted_df = sorted_df[::-1]

st.title('Sorting Assignment')
page = st.sidebar.radio('Select page', ['Statistics', 'Plots'])

if page == 'Statistics':
    st.write('# Statistics')
    sel_col = st.selectbox('Select Type', ['Unsorted', 'Sorted'])
    if sel_col == 'Sorted':
        st.table(sorted_df)
    else:
        st.table(unsorted_df)
elif page == 'Plots':
    st.write('# Plots')
    sel_col = st.selectbox('Select Type', ['Unsorted', 'Sorted'])
    if sel_col == 'Unsorted':
        unsorted_fig = px.line(unsorted_df, x=unsorted_df.index, y=unsorted_df.columns, markers=True,
                               title='Unsorted Algorithms Performance')
        unsorted_fig.update_xaxes(title_text='Size', range=[0, 5000])
        unsorted_fig.update_yaxes(title_text='Time', range=[0, 10])
        st.plotly_chart(unsorted_fig)
    else:
        sorted_fig = px.line(sorted_df, x=sorted_df.index, y=sorted_df.columns,
                             markers=True, title='Sorted Algorithms Performance')
        sorted_fig.update_xaxes(title_text='Size', range=[0, 5000])
        sorted_fig.update_yaxes(title_text='Time', range=[0, 10])
        st.plotly_chart(sorted_fig)
