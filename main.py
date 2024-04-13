import streamlit as st
import dotenv
from services.auth import auth_service

dotenv.load_dotenv()

# Define a function to handle the login process
def login_screen():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", disabled=(not username or not password)):
       if auth_service.authenticate(username, password):
           st.experimental_rerun()

# Main function to control the app's flow
def main():
    if auth_service.is_authenticated():
        st.title('Autenticado!')
    else:
        login_screen()

if __name__ == '__main__':
    main()
