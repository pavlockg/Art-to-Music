import streamlit as st

def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def about():
    st.title("About Page")
    st.write("This is the about page.")

def contact():
    st.title("Contact Page")
    st.write("You can contact us here.")

# Dictionary mapping page names to their respective functions
pages = {
    "Home": home,
    "About": about,
    "Contact": contact
}

# Streamlit app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", tuple(pages.keys()))

    # Invoke the function based on the selected page
    pages[page]()

if __name__ == "__main__":
    main()
