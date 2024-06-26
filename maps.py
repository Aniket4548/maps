import streamlit as st
import prettymaps

st.write('This code is working')

try:
    st.pyplot = prettymaps.plot('Delhi, India', preset='default')

except Exception as e:
    st.error(f"Error generating map: {e}")
