import streamlit as st
import dotenv
from services.auth import auth_service
dotenv.load_dotenv()


# Login screen
def login_screen():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
       auth_service.authenticate(username, password)
       
# Conditional rendering based on authentication status
if auth_service.is_authenticated():
    st.title('Autenticado!')
else:
    login_screen()