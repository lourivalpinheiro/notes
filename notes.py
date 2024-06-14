import streamlit as st

st.set_page_config(page_title='NOTES')
st.title('WELCOME TO NOTES')
text = st.text_area('Create your note down below.')
st.download_button(
    'DOWNLOAD',
    data= text,
    file_name='note.md',
    mime='text/md',
)