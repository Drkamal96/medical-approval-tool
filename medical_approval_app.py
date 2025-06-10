
import streamlit as st
import pandas as pd

# Load the data
@st.cache_data
def load_data():
    df = pd.read_excel("Medical_Approvals_Tool_With_Search.xlsx", sheet_name="Procedure Database")
    return df

df = load_data()

# App title
st.title("Medical Approval Support Tool")

# Dropdown to select procedure
procedure = st.selectbox("Select a Medical Procedure", df["Procedure Name"])

# Filter data for the selected procedure
selected = df[df["Procedure Name"] == procedure].iloc[0]

# Display the information
st.subheader("Procedure Information")
st.markdown(f"**Diagnosis:** {selected['Diagnosis']}")
st.markdown(f"**Key Questions to Ask:** {selected['Key Questions to Ask']}")
st.markdown(f"**Required Investigations:** {selected['Required Investigations']}")
st.markdown(f"**Acceptance Criteria:** {selected['Acceptance Criteria']}")
st.markdown(f"**Notes:** {selected['Notes']}")
st.markdown(f"**Covered by Insurance?:** {selected['Covered by Insurance?']}")
