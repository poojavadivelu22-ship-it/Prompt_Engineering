import streamlit as st
from llm import generate_response
from prompt_templates import build_prompt


# Page Configuration
st.set_page_config(
    page_title="Qwen Prompt Dashboard",
    page_icon="",
    layout="wide"
)


# Title
st.title(" Qwen Prompt Dashboard")

st.write(
    "Explore different prompting techniques and "
    "generate responses using Qwen LLM."
)


# Sidebar
st.sidebar.header(" Prompt Settings")

technique = st.sidebar.selectbox(
    "Choose Prompting Technique",
    [
        "Zero-Shot",
        "One-Shot",
        "Few-Shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    1.0,
    0.2,
    0.1
)

max_tokens = st.sidebar.slider(
    "Maximum Tokens",
    100,
    1000,
    500,
    100
)


# User Input
st.subheader(" Enter Your Task")

task = st.text_area(
    "Question / Task",
    height=150,
    placeholder="Example: Explain Artificial Intelligence in simple words."
)


# Generate Button
if st.button(" Generate Response"):

    if task.strip() == "":
        st.warning("Please enter a task.")

    else:

        try:

            # Build prompt
            prompt = build_prompt(
                technique,
                task
            )

            # Display selected technique
            st.info(
                f"Selected Technique: {technique}"
            )

            # Display generated prompt
            st.subheader(" Generated Prompt")

            with st.expander("View Prompt"):
                st.code(
                    prompt,
                    language="text"
                )

            # Generate response
            with st.spinner(
                " Qwen is generating the response..."
            ):

                answer = generate_response(
                    prompt,
                    temperature,
                    max_tokens
                )

            # Display answer
            st.subheader(" Generated Answer")

            st.success(answer)

        except Exception as e:

            st.error(
                f"Error while generating response: {e}"
            )


# Information Section
st.divider()

st.subheader(" Prompting Techniques")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Zero-Shot")
    st.write(
        "Answer the task without giving examples."
    )

with col2:
    st.markdown("### One-Shot")
    st.write(
        "Give one example before asking the task."
    )

with col3:
    st.markdown("### Few-Shot")
    st.write(
        "Give multiple examples before the task."
    )


col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("### CoT")
    st.write(
        "Uses structured reasoning to solve a task."
    )

with col5:
    st.markdown("### Manual CoT")
    st.write(
        "Manually provides reasoning instructions."
    )

with col6:
    st.markdown("### ToT")
    st.write(
        "Explores multiple possible solution paths."
    )

