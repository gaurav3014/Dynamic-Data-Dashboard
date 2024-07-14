# Dynamic-Data-Dashboard


## Overview
The **Dynamic Data Dashboard** is a Streamlit-based web application designed to visualize and analyze data from CSV or Excel files. Users can upload their datasets, apply filters, and generate various plots to gain insights into their data.

## Features
- **File Upload**: Supports CSV and Excel file formats for data upload.
- **Data Filtering**: Provides multi-select filters for all columns in the dataset.
- **Data Statistics**: Displays statistical summaries of the filtered data.
- **Data Visualization**:
  - Scatter plots
  - Histograms
  - Bar charts
  - Line charts

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/dynamic-data-dashboard.git
    cd dynamic-data-dashboard
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501` to access the dashboard.
3. Use the sidebar to upload your CSV or Excel file.
4. Apply filters to the dataset using the sidebar filter options.
5. View the filtered data and statistical summaries.
6. Generate and explore various plots using the provided visualization options.

## File Structure
- `app.py`: The main application file containing the Streamlit code.
- `requirements.txt`: A list of Python dependencies required to run the application.


## Dependencies
- `streamlit`
- `pandas`
- `plotly`



## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)

---

**Note**: Replace the placeholder URLs and image paths with actual links and paths relevant to your project.
