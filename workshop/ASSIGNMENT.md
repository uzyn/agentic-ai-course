# Multi-Agent AI System Assignment

## Overview

Design and implement a multi-agent AI system that demonstrates your understanding of agentic AI architecture and coordination. Your system should solve a real-world problem or simulate a meaningful scenario using multiple AI agents working together.

## Learning Objectives

1. **Demonstrate understanding of agentic AI architecture** - Show how multiple AI agents can be structured and organized to work together
2. **Build a functional multi-agent system** - Implement a working system with at least 3 distinct agents that collaborate to achieve a common goal

## Project Requirements

### Core Technical Requirements

1. **Multiple Agents (Minimum 3)**
   - Each agent must have a distinct role/persona
   - Agents should have different capabilities or specializations

2. **Agent Coordination**
   - Implement a coordination mechanism (router, orchestrator, or peer-to-peer)
   - Handle agent communication/message passing

3. **Tool Integration**
   - Implement at least 1 tool/function that agents can call
   - Demonstrate tool access control (different agents have different tool permissions)

4. **State Management**
   - Maintain shared or individual agent states
   - Show how information flows between agents
   - Handle conversation/task history appropriately

### Framework Options

You may use any frameworks of your choice. I would recommend LangGraph or CrewAI.

You may use Python or JavaScript/TypeScript for implementation.

### LLM API

- You are recommended to use OpenAI API with the following models for cost management:
  - `gpt-5-mini` (requires `temperature: 1`)
  - `gpt-5-nano` (requires `temperature: 1`)
  - `gpt-4o-mini` (supports variable `temperature`)
- Load API key from `OPENAI_API_KEY` environment variable
- If using other APIs, provide clear instructions for obtaining access. I may reach out to you if I am unable to access the API.

## Deliverables

2 key deliverables are expected:
1. Project code with README.md
2. Project demo log

### Project Code
Your project MUST include a README.md that highlights the following:
1. Overview of your solution or simulation. What is it that you are trying to achieve or solve.
2. Clear set up instructions so that your instructor (me) knows how to set it up and run it.
3. Zip your package (remember to exclude external package folders such as `node_modules/*`), include README.md as well.

### Project Demo Log
1. A text log or screenshots of a demo run of your system.
2. Highlight key interactions _(you can include comments)_ between agents, tool usage, and the final outcome.


## Example Project Ideas

To inspire your creativity, here are some example multi-agent systems you could build:

1. Smart triage for customer support ticketing system.
2. Research assistant team that collaborates to gather, analyze, and summarize information on a given topic.
3. Travel planning committee that organizes a trip based on user preferences and budget.
4. Code review system where different agents check for style, security, performance, and documentation.


**Good luck! Show us your creativity in designing intelligent multi-agent systems!**
