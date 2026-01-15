import streamlit as st

st.set_page_config(page_title="Northstar Proposal Agent", layout="centered")

st.info("Simulated Microsoft 365 Copilot Agent for Northstar Enterprises")

st.title("🤖 Sales Proposal AI Agent")

# -------- AGENT MEMORY --------
if "memory" not in st.session_state:
    st.session_state.memory = {
        "client_name": None,
        "industry": None,
        "product": None,
        "budget": None,
        "timeline": None
    }

# -------- AGENT REASONING --------
def decide_next_step(memory):
    for key, value in memory.items():
        if value is None:
            return key
    return "generate"

# -------- AGENT TOOLS --------
def generate_proposal(memory):
    return f"""
### 📄 Sales Proposal Draft

**Client:** {memory['client_name']}  
**Industry:** {memory['industry']}  

Northstar Enterprises proposes **{memory['product']}** tailored for the {memory['industry']} sector.

**Estimated Budget:** {memory['budget']}  
**Timeline:** {memory['timeline']}  

This proposal is designed to improve efficiency, scalability, and collaboration using Microsoft 365 workflows.
"""

def internal_notes():
    return """
### 🧠 Internal Coordination Notes
- CRM context reviewed (simulated)
- Pricing checked against approval rules
- Proposal template selected automatically
- Awaiting sales manager approval before external sharing
"""

# -------- AGENT LOOP --------
next_step = decide_next_step(st.session_state.memory)

if next_step != "generate":
    user_input = st.text_input(f"Please provide {next_step.replace('_',' ').title()}")

    if st.button("Submit"):
        st.session_state.memory[next_step] = user_input
        st.experimental_rerun()
else:
    st.success("All required context gathered.")
    st.markdown(generate_proposal(st.session_state.memory))
    st.markdown(internal_notes())
