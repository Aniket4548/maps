import streamlit as st
import prettymaps


st.pyplot = prettymaps.plot(
    'Stad van de Zon, Heerhugowaard, Netherlands',
    preset = 'minimal'
)

