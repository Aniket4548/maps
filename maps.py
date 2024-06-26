import streamlit as st
import prettymaps

st.write('This code is working')

try:
  # Improved map generation with potential customization
  map = prettymaps.plot( 'Delhi, India',  # Location to center the map
      style='stamen.terrain')
  st.pyplot(map)  # Display the map

except Exception as e:
  st.error(f"Error generating map: {e}")
  
