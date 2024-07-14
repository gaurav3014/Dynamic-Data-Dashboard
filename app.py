import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Streamlit Dashboard Example 📊")

# Sidebar for file upload
st.sidebar.header("Upload your CSV or Excel file")
uploaded_file = st.sidebar.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Determine file type and read the file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    
    st.sidebar.header("Filter Data")
    # Add sidebar filters
    unique_values = {col: df[col].unique() for col in df.columns}
    selected_values = {col: st.sidebar.multiselect(f"Filter by {col}", options=values, default=values) for col, values in unique_values.items()}
    
    # Filter the dataframe based on selected values
    filtered_df = df.copy()
    for col, values in selected_values.items():
        filtered_df = filtered_df[filtered_df[col].isin(values)]
    
    st.header("Filtered Data")
    st.write(filtered_df)

    # Show dataframe statistics
    st.header("Data Statistics")
    st.write(filtered_df.describe())

    # Plotting
    st.header("Data Visualization")

    # Column selection for plotting
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis", options=columns)
    y_axis = st.selectbox("Select Y-axis", options=columns)

    fig = px.scatter(filtered_df, x=x_axis, y=y_axis, title=f"Scatter plot of {x_axis} vs {y_axis}")
    st.plotly_chart(fig)

    # Additional plots
    st.header("Additional Plots")

    st.subheader("Histogram")
    hist_column = st.selectbox("Select column for histogram", options=columns)
    hist_fig = px.histogram(filtered_df, x=hist_column, title=f"Histogram of {hist_column}")
    st.plotly_chart(hist_fig)

    st.subheader("Bar Chart")
    bar_column = st.selectbox("Select column for bar chart", options=columns)
    bar_fig = px.bar(filtered_df, x=bar_column, title=f"Bar chart of {bar_column}")
    st.plotly_chart(bar_fig)

    st.subheader("Line Chart")
    line_x = st.selectbox("Select X-axis for line chart", options=columns, key="line_x")
    line_y = st.selectbox("Select Y-axis for line chart", options=columns, key="line_y")
    line_fig = px.line(filtered_df, x=line_x, y=line_y, title=f"Line chart of {line_x} vs {line_y}")
    st.plotly_chart(line_fig)
else:
    st.write("Please upload a CSV or Excel file to see the dashboard.")
