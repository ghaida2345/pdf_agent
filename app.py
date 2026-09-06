import streamlit as st
import requests

st.title("PDF AI Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"File selected: {uploaded_file.name}")

    if st.button("Send PDF to n8n"):

        webhook_url = "https://ghaida1122.app.n8n.cloud/webhook-test/pdf-Agent"

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        response = requests.post(
            webhook_url,
            files=files
        )

        st.write("Status Code:", response.status_code)

        try:
            data = response.json()

            answer = data.get("answer", {})

            st.subheader(answer.get("title", "نتيجة تحليل الملف"))

            st.write(answer.get("summary", ""))

            st.subheader("أهم النقاط")

            for point in answer.get("key_points", []):
                st.write(f"• {point}")

        except:
            st.error("تعذر قراءة الرد من n8n")
            st.write(response.text)
