import streamlit as st
import prettymaps

st.write('This code is working')

try:
    plot = prettymaps.plot()
    plot.draw('Delhi, India')
    st.pyplot(plot.fig)
except Exception as e:
    st.error(f"Error generating map: {e}")
