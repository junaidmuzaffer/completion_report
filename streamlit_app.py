import streamlit as st
import pandas as pd

# 1. Upload File
st.title("Sugar Mill Roller Completion Report Generator")
uploaded_file = st.file_uploader("Upload your Word file", type=["docx", "csv"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Data Preview:", df.head())

    # 2. Select a row/job
    selected_index = st.number_input("Enter Row Number (0-based):", min_value=0, max_value=len(df)-1, step=1)
    selected_data = df.iloc[selected_index]

    # 3. Generate Report Text
    report_text = f"""
    Roller Completion Report

    Roller ID: {selected_data['Roller_ID']}
    Date: {selected_data['Date']}
    Technician: {selected_data['Technician']}
    Material Used: {selected_data['Material']}
    Comments: {selected_data['Comments']}
    """

    st.text_area("Generated Report", report_text, height=300)

    # 4. Export as PDF
    if st.button("Download Report as PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in report_text.split('\n'):
            pdf.cell(200, 10, txt=line, ln=True)
        pdf.output("completion_report.pdf")
        st.success("PDF created! Check your download folder.")
