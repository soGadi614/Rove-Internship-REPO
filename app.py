import sys
import os

# Force Python to find modules inside the code folder
sys.path.append(os.path.abspath("code"))

import streamlit as st

# Define your individual tools as sub-pages
copilot_page = st.Page("code/combined_copilot.py", title="Combined Copilot", icon=":material/smart_toy:")
refund_page = st.Page("code/Refund_Calculator.py", title="Refund Calculator", icon=":material/calculate:")
sop_page = st.Page("code/SOP_match.py", title="SOP Match", icon=":material/assignment:")

# Bundle them into a sidebar navigation menu
pg = st.navigation([copilot_page, refund_page, sop_page])

# Run the app configuration
st.set_page_config(page_title="Rove Internship Workspace", layout="wide")
pg.run()
