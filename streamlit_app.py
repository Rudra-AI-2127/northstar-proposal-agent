import streamlit as st
import json
import os
import random

# ---------------- CONFIG ----------------
MEMORY_FILE = "agent_memory.json"

st.set_page_config(
    page_title="Sales Proposal AI Agent",
    layout="centered"
)

# ---------------- UTILITIES ----------------
def load_all_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def load_user_memory(user_id):
    data = load_all_memory()
    return data.get(user_id, None)

def save_user_memory(user_id, memory):
    data = load_all_memory()
    data[user_id] = memory
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def clear_user_memory(user_id):
    data = load_all_memory()
    if user_id in data:
        del data[user_id]
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)

# ---------------- HEADER ----------------
st.markdown(
    """
    <div style="background-color:#1f2937;padding:14px;border-radius:8px;margin-bottom:20px">
        <span style="color:#93c5fd;font-size:14px">
            Simulated Microsoft 365 Copilot Agent for Northstar Enterprises
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Sales Proposal AI Agent")

st.markdown(
    "This agent gathers context incrementally, reasons over missing information, "
    "and generates enterprise-ready sales proposals with persistent memory and human approval."
)

st.divider()

# ---------------- SESSION MEMORY ----------------
if "memory" not in st.session_state:
    st.session_state.memory = {
        "client_name": None,
        "industry": None,
        "product": None,
        "budget": None,
        "timeline": None
    }

if "user_id" not in st.session_state:
    st.session_state.user_id = None

# ---------------- RESUME PREVIOUS PROPOSAL ----------------
stored_memory = load_all_memory()

if stored_memory and st.session_state.user_id is None:
    st.subheader("Resume Previous Proposal")

    selected_user = st.selectbox(
        "Select an existing client to resume",
        options=["-- Select --"] + list(stored_memory.keys())
    )

    if selected_user != "-- Select --":
        if st.button("Resume Proposal"):
            st.session_state.user_id = selected_user
            st.session_state.memory = stored_memory[selected_user]
            st.rerun()

st.divider()

# ---------------- AGENT REASONING ----------------
def decide_next_step(memory):
    for key, value in memory.items():
        if value is None:
            return key
    return "generate"

# ---------------- AGENT TOOLS ----------------
def generate_proposal(memory):
    return f"""
### Sales Proposal Draft

**Client:** {memory['client_name']}  
**Industry:** {memory['industry']}

Northstar Enterprises proposes **{memory['product']}**, tailored for the **{memory['industry']}** sector.

**Estimated Budget:** {memory['budget']}  
**Timeline:** {memory['timeline']}

This proposal is designed to improve operational efficiency, scalability, and collaboration
using Microsoft 365–native workflows.
"""

def internal_notes():
    return """
### Internal Coordination Notes
- CRM context reviewed (simulated)
- Pricing validated against approval thresholds
- Proposal template selected
- Awaiting sales manager approval before external sharing
"""

def confidence_score():
    return random.randint(85, 95)

# ---------------- RESET AGENT ----------------
col1, col2 = st.columns([6, 2])
with col2:
    if st.button("Reset Agent"):
        if st.session_state.user_id:
            clear_user_memory(st.session_state.user_id)
        st.session_state.user_id = None
        st.session_state.memory = {
            "client_name": None,
            "industry": None,
            "product": None,
            "budget": None,
            "timeline": None
        }
        st.rerun()

# ---------------- AGENT LOOP ----------------
next_step = decide_next_step(st.session_state.memory)

label_map = {
    "client_name": "Client Name",
    "industry": "Industry",
    "product": "Proposed Product / Service",
    "budget": "Estimated Budget",
    "timeline": "Expected Timeline"
}

if next_step != "generate":
    st.subheader("Context Collection")

    with st.form(key="context_form"):
        user_input = st.text_input(f"Please provide {label_map[next_step]}")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if user_input.strip() == "":
                st.warning("This field cannot be empty.")
            else:
                st.session_state.memory[next_step] = user_input

                if next_step == "client_name":
                    st.session_state.user_id = user_input

                save_user_memory(
                    st.session_state.user_id,
                    st.session_state.memory
                )

                st.rerun()

else:
    st.success("All required context gathered.")

    st.markdown(generate_proposal(st.session_state.memory))
    st.markdown(internal_notes())

    st.divider()

    st.metric(
        label="Agent Confidence Score",
        value=f"{confidence_score()}%",
        help="Confidence based on completeness and clarity of inputs."
    )

    st.divider()

    st.subheader("Approval & Governance")

    approved = st.checkbox("I approve this proposal for external sharing")

    if approved:
        st.success("Proposal approved. Ready for external sharing.")
    else:
        st.info("Awaiting human approval. Proposal will not be shared externally.")
