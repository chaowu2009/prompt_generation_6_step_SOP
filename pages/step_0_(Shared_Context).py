import streamlit as st

from sop_core import render_step_page

st.set_page_config(page_title="SOP step_0 (Shared Context)", layout="wide")
render_step_page("step_0")
