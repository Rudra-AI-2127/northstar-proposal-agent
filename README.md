Sales Proposal AI Agent

Vibe-Coded Working Experience

A stateful AI agent prototype that demonstrates how enterprise sales proposal workflows can be supported using an agent-based approach inspired by Microsoft 365 Copilot.

🔗 Live Demo:
https://northstar-proposal-agent.streamlit.app/

Overview

This project simulates an AI agent operating inside an enterprise productivity environment (Microsoft 365 Copilot–like experience).
The agent assists sales teams by incrementally gathering context, maintaining proposal state across sessions, and generating enterprise-ready sales proposals with mandatory human approval.

The focus of this prototype is agent behavior, reasoning, and workflow orchestration, not production-grade integrations.

Key Capabilities

Incremental context collection (client, timeline, scope, etc.)

Stateful proposal workflows with resume support

Persistent memory using file-based storage

Proposal draft generation aligned to enterprise workflows

Internal coordination notes generation

Mandatory human approval before proposal completion

Reset and recovery controls for safety and predictability

Why an Agent-Based Approach

Traditional automation or single-prompt copilots are insufficient for proposal workflows because:

Required context is often incomplete at the start

Workflows span multiple steps and sessions

Decisions depend on previous inputs

Human review and approval are mandatory

This agent reasons across time, context, and workflow state, advancing only when sufficient information is available.

Agent Responsibilities & Boundaries
What the Agent Owns

Tracking proposal state

Identifying missing context

Generating drafts and internal notes

Enforcing approval gates

What Remains Human-Driven

Providing business context

Reviewing proposal drafts

Approving before external sharing

Final decision-making

The agent is assistive, not autonomous.

Architecture (Conceptual)
User
  ↓
Copilot-like UI (Streamlit)
  ↓
Agent Reasoning Layer
  ↓
Session Memory + Persistent Memory
  ↓
Proposal Generator
  ↓
Human Approval Gate


Session memory handles active interactions

Persistent memory enables resuming previous proposals

Approval gate prevents autonomous external actions

Safety, Trust & Governance

No automated external communication

Mandatory human approval before completion

Predictable, step-by-step progression

Reset functionality to recover from errors

Clear separation between internal notes and external content

Safety is enforced by design.

Intentional Trade-offs

Streamlit used for rapid prototyping

Microsoft 365 APIs are simulated conceptually

File-based memory used instead of databases

Single-proposal-per-client workflow

These choices prioritize clarity of agent behavior over platform plumbing.

What This Demonstrates

Platform-level thinking across workflows and data

Clear understanding of agent responsibility and limits

Comfort operating in ambiguous, multi-stakeholder environments

Ability to translate abstract agent concepts into a working experience

Disclaimer

This is a prototype intended to demonstrate agent reasoning and workflow orchestration.
It is not production-ready and does not connect to live enterprise systems.

Author

Rudra Pratap Singh Rathore
