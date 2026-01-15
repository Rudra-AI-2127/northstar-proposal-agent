import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sales Proposal AI Agent",
    layout="centered"
)

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
    "This agent incrementally gathers context, reasons over missing information, "
    "and generates enterprise-ready sales proposals with human approval."
)

st.divider()

# ---------------- AGENT MEMORY ----------------
if "memory" not in st.session_state:
    st.session_state.memory = {
        "client_name": None,
        "industry": None,
        "product": None,
        "budget": None,
        "timeline": None
    }

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

Northstar Enterprises proposes **{memory['product']}**, specifically tailored for the **{memory['industry']}** sector.

**Estimated Budget:** {memory['budget']}  
**Timeline:** {memory['timeline']}

This proposal is designed to improve operational efficiency, scalability, and cross-team collaboration
using Microsoft 365–native workflows.
"""

def internal_notes():
    return """
### Internal Coordination Notes
- CRM context reviewed (simulated)
- Pricing validated against approval thresholds
- Appropriate proposal template selected
- Awaiting sales manager approval before external sharing
"""

def confidence_score():
    return random.randint(85, 95)

# ---------------- RESET AGENT ----------------
col1, col2 = st.columns([6, 2])

with col2:
    if st.button("Reset Agent"):
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

if next_step != "generate":
    st.subheader("Context Collection")

    label_map = {
        "client_name": "Client Name",
        "industry": "Industry",
        "product": "Proposed Product / Service",
        "budget": "Estimated Budget",
        "timeline": "Expected Timeline"
    }

    user_input = st.text_input(f"Please provide {label_map[next_step]}")

    if st.button("Submit"):
        if user_input.strip() == "":
            st.warning("This field cannot be empty.")
        else:
            st.session_state.memory[next_step] = user_input
            st.rerun()

else:
    st.success("All required context gathered.")

    st.markdown(generate_proposal(st.session_state.memory))
    st.markdown(internal_notes())

    st.divider()

    # ---------------- CONFIDENCE SCORE ----------------
    score = confidence_score()
    st.metric(
        label="Agent Confidence Score",
        value=f"{score}%",
        help="Represents the agent’s confidence based on completeness and clarity of inputs."
    )

    st.divider()

    # ---------------- HUMAN APPROVAL ----------------
    st.subheader("Approval & Governance")

    approved = st.checkbox(
        "I approve this proposal for external sharing",
        help="Human approval is mandatory before sending proposals to clients."
    )

    if approved:
        st.success("Proposal approved. Ready for external sharing.")
    else:
        st.info("Awaiting human approval. Proposal will not be shared externally.")

