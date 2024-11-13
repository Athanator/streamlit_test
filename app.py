import streamlit as st
import pandas as pd

st.title("Excel Transformation App")

# Step 1: Upload Excel file
file = st.file_uploader("Upload an Excel file", type="xlsx")

if file:
    # Load and display the file content
    df = pd.read_excel(file)
    st.write("Original Table:", df)

    # Step 2: Transform the Table
    if st.button("Transform Table"):
        # Example transformation: Adding a new column with a simple calculation
        transformed_df = df.copy()  # Placeholder for actual transformation logic
        transformed_df["New Column"] = transformed_df.iloc[:, 0] * 2  # Example transformation
        st.write("Transformed Table:", transformed_df)

        # Step 3: Download the Transformed File
        # Use Streamlit's download button to save the transformed data as an Excel file
        st.download_button(
            label="Download Transformed File",
            data=transformed_df.to_excel(index=False),
            file_name="transformed_table.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
