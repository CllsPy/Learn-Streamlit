import streamlit as st

def main():
    st.sidebar.header('Page Selection')
    page_selection = st.sidebar.selectbox(
        'Page', ['Main Page', 'Page 1', 'Page 2', 'Home']
        )
    pages_main = {
        'Main Page': main_page,
        'Page 1': run_page_1,
        'Page 2': run_page_2,
        'Home': home
    }

    pages_main[page_selection]()


def func_page_1():
    st.title('Page 1')

def func_page_2():
    st.title('Page 2')
    st.markdown('Texto Aleatório...')

def func_page_home():
    st.title('HOME')
    st.markdown('Texto Aleatório...')
 

def main_page():
    st.title('Main Page')
    st.markdown('[Using st.pages](https://discuss.streamlit.io/t/using-st-pages-st-navigation-to-create-selectbox-selector/81682/2)')

def run_page_1():
    func_page_1()

def run_page_2():
    func_page_2()

def home():
    func_page_home()

if __name__=='__main__':
    main()


