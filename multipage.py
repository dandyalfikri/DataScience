import streamlit as st

class MultiPage: 

    def __init__(self) -> None:
        self.pages = []
    
    def add_page(self, title, func) -> None: 

        self.pages.append({
          
                "title": title, 
                "function": func
            })

    def run(self):
        st.sidebar.header('Navigasi Halaman')
        page = st.sidebar.selectbox(
            'Halaman', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        page['function']()