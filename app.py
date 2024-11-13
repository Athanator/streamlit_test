import streamlit as st
import pandas as pd
from io import BytesIO

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

        # Step 3: Save the Transformed File to a BytesIO object
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            transformed_df.to_excel(writer, index=False)
        
        # Seek to the beginning of the stream
        output.seek(0)
        
        # Use Streamlit's download button to save the transformed data
        st.download_button(
            label="Download Transformed File",
            data=output,
            file_name="transformed_table.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
