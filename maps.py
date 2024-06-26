import streamlit as st
import prettymaps


plot = prettymaps.plot(
    'Stad van de Zon, Heerhugowaard, Netherlands',
    preset = 'minimal'
)

st.pyplot(plot)
