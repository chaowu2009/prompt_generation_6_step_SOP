import streamlit as st

from sop_core import STEP_CONFIG, apply_global_styles, ensure_state

st.set_page_config(page_title="AI Enabled Java Test Framework SOP", layout="wide")

apply_global_styles()
ensure_state()

st.title("Java Test Framework SOP Prompt Generator")
st.caption("Open any workflow step or the standalone SKILL.md prompt page from here, or use the left Pages menu.")

st.markdown("### Open a Page")

step_columns = st.columns(4)
for index, (step_key, config) in enumerate(STEP_CONFIG.items()):
    step_num = step_key.split("_")[-1]
    page_path = f"pages/step_{step_num}_({config['name'].replace(' ', '_')}).py"
    with step_columns[index % len(step_columns)]:
        st.page_link(
            page=page_path,
            label=f"Step {step_num} - {config['name']}",
        )

st.page_link(
    page="pages/generate_SKILL_file.py",
    label="Generate SKILL.md Prompt",
)

st.markdown("### Overall Progress")
for step_key, config in STEP_CONFIG.items():
    step_num = step_key.split("_")[-1]
    is_done = st.session_state.done_flags.get(step_key, False)
    status = "Done" if is_done else "Pending"
    st.write(f"- Step {step_num} ({config['name']}): {status}")
