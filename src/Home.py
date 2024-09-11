import streamlit as st
from assistant import Create

st.session_state.assistants = Create().run()
st.session_state.thread = {}

st.title("AI Tutor - Pre-Master: Computer Programming")
st.subheader("Author: Matias Tolppanen")
st.subheader("Date: 9.9.2024")
st.write("Testing Partner: Robin Manz")

st.markdown("## Welcome to the AI Tutor Project")

st.write("""
This AI Tutor project focuses on helping students with computer programming through three core modules. 
These modules are designed to promote learning without giving direct answers, encouraging students to develop problem-solving skills.
""")

st.markdown("## Core Modules")

st.markdown("### 1. Socratic with Hints")
st.write("""
- **Objective:** Guide students to the correct solution through progressive hints.
- **Features:**
  - Progressive hints become more detailed step-by-step.
  - Hints are designed to guide the student to the right angle without directly providing the answer.
- **Testing:** Ensure the tutor provides hints without giving direct answers, especially for common Python beginner mistakes.
""")

st.markdown("### 2. Debugging Helper Module")
st.write("""
- **Objective:** Help students debug their code by explaining errors and offering tips.
- **Features:**
  - Identifies common beginner coding errors such as syntax and logical mistakes.
  - Offers suggestions on how to fix errors without giving away the complete solution.
  - Provides tips to improve coding style.
- **Testing:** Validate the tutor’s ability to guide students through debugging without solving the problem entirely.
""")

st.markdown("### 3. Feedback Bot")
st.write("""
- **Objective:** Provide constructive feedback on student submissions.
- **Features:**
  - Explains why an answer is right or wrong and why it is wrong etc.
- **Testing:** Ensure feedback is clear, concise, and scalable for different student levels.
""")

st.markdown("## Technical Development Overview")
st.write("""
This project is built using a low-code approach and leverages UvA AI API and Streamlit for the front-end. 
The system focuses on ethical considerations such as fairness, transparency, and non-judgmental feedback. 
Development is ongoing, with future plans to integrate advanced features like difficulty adjustment and feedback scaling.
""")


