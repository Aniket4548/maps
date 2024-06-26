import streamlit as st
import prettymaps

st.write('This code is working')

try:
    plot = prettymaps.plot('Delhi, India', preset='default')
    st.pyplot(plot)
except Exception as e:
    st.error(f"Error generating map: {e}")
