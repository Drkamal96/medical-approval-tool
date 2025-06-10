import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="Medical Approval Assistant", page_icon="🩺", layout="wide")

# الشريط الجانبي
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=120)
    st.title("🔍 Menu")
    st.markdown("Use the dropdown below to choose a procedure.")
    
# العنوان الرئيسي
st.title("🩺 Medical Approval Assistant")
st.markdown("Helping insurance doctors verify the required documents for each medical procedure.")
st.markdown("---")

# تحميل ملف الإكسل
@st.cache_data
def load_data():
    return pd.read_excel("Medical_Approvals_Tool_With_Search.xlsx")

df = load_data()

# اختيار الإجراء الطبي
procedure_list = df['Procedure'].dropna().unique().tolist()
selected_procedure = st.selectbox("Select a medical procedure:", procedure_list)

# البحث وعرض النتائج
if selected_procedure:
    result_df = df[df['Procedure'] == selected_procedure]

    # عرض النتائج داخل بطاقات
    for index, row in result_df.iterrows():
        with st.expander(f"📄 {row['Procedure']} - Details"):
            st.write(f"**Required Questions:**\n{row['Required Questions']}")
            st.write(f"**Expected Findings:**\n{row['Expected Findings']}")
            st.write(f"**Notes:**\n{row['Notes'] if pd.notna(row['Notes']) else 'No additional notes.'}")
            st.markdown("---")

# تذييل
st.markdown("----")
st.caption("Built with ❤️ by Dr. Kamal | Powered by Streamlit")
