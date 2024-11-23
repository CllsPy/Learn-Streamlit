import streamlit as st
from pgs.pag1 import title1
from pgs.pag2 import title2

def main():
    st.sidebar.header('Page Selection')
    page_selection = st.sidebar.selectbox(
        'Page', ['Main Page', 'Page 1', 'Page 2']
        )
    pages_main = {
        'Main Page': main_page_subpage,
        'Page 1': run_pg1,
        'Page 2': run_pg2,
    }

    pages_main[page_selection]()

def main_page_subpage():
    st.title('MAIN')

def run_pg1():
    title1()

def run_pg2():
    title2()

if __name__=='__main__':
    main()


