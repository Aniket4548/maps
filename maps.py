import streamlit as st
import prettymaps

# Error handling for a more robust app
try:
  # Improved map generation with potential customization
  map = prettymaps.plot( 'Delhi, India',  # Location to center the map
      style='stamen.terrain',  # Optional: Choose a map style (see prettymaps docs)
      # Optional: Set zoom level for closer view (1-18)
  )
  st.pyplot(map)  # Display the map

except Exception as e:
  st.error(f"Error generating map: {e}")
  st.info("Here are some tips for troubleshooting map generation:")
  st.write("- Ensure you have a stable internet connection.")
  st.write("- Verify that the `prettymaps` library is installed correctly.")
  st.write("- Check for any errors or warnings in the console output.")
