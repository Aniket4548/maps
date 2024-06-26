import streamlit as st
import prettymaps

try:
  st.pyplot = prettymaps.plot('Delhi, India')
except Exception as e:
  st.error(f"Error generating map: {e}")
