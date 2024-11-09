# app.py
import streamlit as st

def main():
    st.title("Local (Confidential) LLM Letter Writer")

    # Form box for letter type/template
    letter_type = st.text_input("Enter letter type/template")

    # Background info section
    st.header("Background Info")
    docket_info = st.text_input("Docket Info")
    cms_info = st.text_input("CMS Info")
    client_goals = st.text_area("Client Goals")
    client_issues = st.text_area("Client Issues Discussed")
    advice_given = st.text_area("Advice Given to Client")
    procedural_posture = st.text_area("Current Procedural Posture / Next Court Event")

    # Create prompt button
    if st.button("Create Prompt"):
        prompt = (
            f"Letter Type/Template: {letter_type}\n\n"
            f"Background Info:\n"
            f"Docket Info: {docket_info}\n"
            f"CMS Info: {cms_info}\n"
            f"Client Goals: {client_goals}\n"
            f"Client Issues Discussed: {client_issues}\n"
            f"Advice Given to Client: {advice_given}\n"
            f"Current Procedural Posture / Next Court Event: {procedural_posture}\n"
        )
        st.text_area("Generated Prompt", prompt, height=300)

if __name__ == "__main__":
    main()