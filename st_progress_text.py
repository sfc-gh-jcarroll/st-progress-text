import streamlit as st

space = st.empty()

def st_progress(value, text=''):
    with space.container():
        if text:
            st.markdown(text.format(value=value))
        st.progress(value)

    return space
