import streamlit as st
import prettymaps

st.write('This code is working')

try:
    # Create a PrettyMap object
    m = prettymaps.PrettyMap()
    m.add_annotation('Delhi, India', coords=[28.6139, 77.2090])  # Add a annotation at Delhi, India
    fig, ax = m.draw()  # Draw the map
    st.pyplot(fig)  # Display the map
except Exception as e:
    st.error(f"Error generating map: {e}")
