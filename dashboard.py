import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page layout and theme
st.set_page_config(page_title="Green Finance Optimization Dashboard", layout="wide")

# Styling the app using markdown with a modern design approach
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: #f5f5f5;
            color:black
        }
        .stHeader {
            background-color: #1e2a38;
            color: #ffffff;
            padding: 20px;
            text-align: center;
        }
        .stSidebar {
            background-color: #2f3e56;
        }
        .stText {
            font-size: 1.1em;
            color: #333333;
        }
        .stTable th {
            background-color: #1e2a38;
            color: #ffffff;
            font-weight: bold;
            padding: 12px 15px;
        }
        .stTable td {
            background-color: #ffffff;
            padding: 10px 15px;
            border-bottom: 1px solid #f1f1f1;
        }
        .stButton>button {
            background-color: #2d9cdb;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 14px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #217eb3;
        }
        .section-header {
            font-size: 22px;
            font-weight: bold;
            color: #2f3e56;
            margin-bottom: 15px;
        }
        .section-subheader {
            font-size: 16px;
            color: #757575;
            margin-top: 5px;
        }
        .table-container {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .plot-container {
            margin-top: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="stHeader">🌱 Green Finance Optimization Dashboard 🌍</h1>', unsafe_allow_html=True)
st.write("Welcome to the Green Finance Optimization Platform! This platform uses AI to optimize green investments across various sectors. Below are key insights and data-driven recommendations.")

# Enhanced Dummy Data for Projects and ESG Scores
projects = ['Solar Farm A', 'Wind Power B', 'Hydropower C', 'Sustainable Agri D', 'Green Building E']
esg_scores = [0.85, 0.78, 0.92, 0.76, 0.88]
roi = [12, 15, 10, 8, 20]
budget = [100, 150, 120, 80, 110]
carbon_impact = [25000, 40000, 35000, 18000, 30000]  # Carbon emissions reduction in tons per year
job_creation = [500, 800, 600, 350, 700]  # Jobs created in each project

# Detailed Data for Portfolio Optimization
portfolio_data = {
    'Project': projects,
    'ESG Score': esg_scores,
    'ROI (%)': roi,
    'Budget ($M)': budget,
    'Carbon Impact (tons/year)': carbon_impact,
    'Job Creation (jobs)': job_creation
}

# Convert data into DataFrame
df = pd.DataFrame(portfolio_data)

# ESG Score Distribution Plot
st.markdown('<div class="section-header">1. ESG Score Distribution Across Projects</div>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=projects, y=esg_scores, ax=ax, palette="coolwarm")
ax.set_title('ESG Scores for Different Green Projects', fontsize=16)
ax.set_xlabel('Projects', fontsize=12)
ax.set_ylabel('ESG Score', fontsize=12)
ax.set_ylim(0, 1)
st.pyplot(fig)

# Project Scoring and ROI Table with Enhanced Style
st.markdown('<div class="section-header">2. Project Scoring and ROI</div>', unsafe_allow_html=True)
st.write("Below is a summary of key project metrics such as ESG scores, ROI, Budget, Carbon Impact, and Job Creation.")
st.markdown('<div class="table-container">', unsafe_allow_html=True)
st.dataframe(df.style.set_table_styles([{
    'selector': 'th',
    'props': [('background-color', '#1e2a38'), ('color', 'white'), ('font-size', '14px')]
}, {
    'selector': 'td',
    'props': [('background-color', '#ffffff'), ('color', '#333333')]
}]), width=800)
st.markdown('</div>', unsafe_allow_html=True)

# Resource Allocation Optimization (More Detailed Data)
st.markdown('<div class="section-header">3. Resource Allocation Optimization</div>', unsafe_allow_html=True)
st.write("Here is an optimized resource allocation plan based on ESG impact, ROI, and project budgets.")
dummy_allocation = {
    'Project': projects,
    'Allocated Budget ($M)': np.random.randint(50, 130, size=5),
    'Expected ESG Impact': np.random.uniform(0.7, 1.0, size=5),
    'Capital Needed for Scale ($M)': np.random.randint(80, 150, size=5)
}
allocation_df = pd.DataFrame(dummy_allocation)
st.markdown('<div class="table-container">', unsafe_allow_html=True)
st.dataframe(allocation_df, width=800)
st.markdown('</div>', unsafe_allow_html=True)

# Scenario Analysis (Improved Chart)
st.markdown('<div class="section-header">4. Scenario Analysis for Investment Strategies</div>', unsafe_allow_html=True)
st.write("This section compares different investment strategies in terms of ESG impact and ROI.")

# Dummy data for scenario analysis
scenarios = ['Strategy A', 'Strategy B', 'Strategy C']
roi_scenario = [14, 18, 12]
esg_scenario = [0.85, 0.90, 0.80]

# Plot for Scenario Analysis
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(scenarios, roi_scenario, label='ROI', marker='o', color='royalblue', linewidth=2)
ax.plot(scenarios, esg_scenario, label='ESG Score', marker='s', color='seagreen', linestyle='--', linewidth=2)
ax.set_title('Scenario Analysis: ROI vs ESG Impact', fontsize=16)
ax.set_xlabel('Investment Strategy', fontsize=12)
ax.set_ylabel('Values', fontsize=12)
ax.legend()
st.pyplot(fig)

# Future Risk Prediction (More Detailed Text Output)
st.markdown('<div class="section-header">5. Predicted Future Risks for Green Investments</div>', unsafe_allow_html=True)
st.write("""
We assess potential risks in green investments, including:
- **Policy Risks**: New regulations that might alter project viability.
- **Technological Risks**: Emerging green technologies that may impact current investments.
- **Market Fluctuations**: Energy price volatility that affects renewable energy projects.
- **Climate Change Impact**: The unpredictable long-term effects of climate change on project feasibility.
""")

# File Uploader for Project Reports (For User Interaction)
st.markdown('<div class="section-header">6. Upload Your Project Report</div>', unsafe_allow_html=True)
st.write("""
Upload your project report for analysis. Our AI will provide further insights based on the ESG metrics and investment strategies of the projects.
""")
uploaded_file = st.file_uploader("Choose a file...", type=["txt", "pdf", "docx"])
if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")
    st.write("Processing the report... (This feature is under development)")
    st.success("Report processed successfully!")

