import streamlit as st

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Manufacturing Manuals Chatbot",
    layout="wide"
)

# ---------- STYLES ----------
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f4f4f4;
    }
    .css-1cpxqw2 {
        display: none;
    }
    .chatbox {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .reference-box {
        font-size: 0.9em;
        background-color: #eee;
        padding: 10px;
        margin-top: 10px;
        border-left: 4px solid #666;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "login"  # default page

# ---------- LOGIN PAGE ----------
def login_page():
    st.title("Login into your account")
    st.write("Please enter your credentials")

    email = st.text_input("Email address", placeholder="alex@email.com")
    password = st.text_input("Password", placeholder="Enter your password", type="password")

    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Login now"):
            if email and password:
                st.session_state.page = "chat"  # ✅ switch page
            else:
                st.error("Please enter both email and password.")
    with col2:
        st.write("")

    st.markdown("[Forgot password?](#)")
    st.markdown("[Signup now](#)")
    st.markdown("---")
    st.markdown("OR")

# ---------- SIDEBAR DOCUMENT TREE ----------
def render_sidebar():
    st.sidebar.header("Documents")
    st.sidebar.markdown("**Factory X**")

    st.sidebar.markdown("""
    - Operations Manuals  
    - Maintenance Logs  
    - End of Shift Logs  
    - Corporate Instructions  
    - Global Policies  
    - Regional Policies  
    - Local Notes  
    - OEM Bulletins  
    - Other Documents  
    """)

# ---------- CHAT PAGE ----------
def show_chat_page():
    render_sidebar()

    st.title("How can I help today?")

    # Previous conversation (mock)
    with st.container():
        st.markdown("**Bob Smith**")
        st.markdown("What are the termination clauses for AWS contracts?")
        st.markdown("""
        <div class="chatbox">
        AWS allows termination for cause (e.g., breach, non-payment). After termination, clients have at least 30 days to retrieve data from the AWS environment.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="reference-box">
        📄 **UK Policy v2.doc**  •  Word Doc • Uploaded by Steve Smith on 23/01/2021
        </div>
        """, unsafe_allow_html=True)

        st.markdown("👍  👎  Give feedback on this answer")

    st.markdown("---")

    # Chat input
    prompt = st.text_input("Ask your question about the manuals...")
    if prompt:
        st.markdown("Searching knowledge base... (mock)")
        st.markdown("🔍 Response will appear here from AWS Bedrock...")

# ---------- MAIN ROUTING ----------
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "chat":
    show_chat_page()
