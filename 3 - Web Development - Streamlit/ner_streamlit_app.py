import streamlit as st
import pandas as pd
import requests

DOCKER_CONTAINER_URL = "http://localhost:8000/ner"

# Align logo and user instructions using streamlit columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:  # center col
    st.image("sleek_logo.png", width=400)

    st.title("NER App")

    st.write("Welcome to Sleek's NER App!")
    st.write("")
    st.write("Upload a text file to extract named entities:")

    # File upload widget
    uploaded_file = st.file_uploader(label='Choose text file', type="txt")

if uploaded_file is not None:

    file_contents = uploaded_file.read().decode("utf-8")

    # Limiting display of the file contents
    max_display_length = 2000
    if len(file_contents) > max_display_length:
        st.write("File content (truncated for display):")
        st.write(file_contents[:max_display_length] + "...")
    else:
        st.write("File content:")
        st.write(file_contents)

    # Sending text to the NER service running in the Docker container
    try:
        response = requests.post(
            DOCKER_CONTAINER_URL,
            json={"text": file_contents}
        )
        # Raising error if the request unsuccessful
        response.raise_for_status()

        ner_results = response.json()

        # Checking if there are entities in the response
        if ner_results and "entities" in ner_results:
            data = {
                "Entity Class": [entity["entity_group"] for entity in ner_results["entities"]],
                "Entity": [entity["word"] for entity in ner_results["entities"]]
            }

            # Displaying as table
            df = pd.DataFrame(data)
            st.write("Entities Identified:")
            st.table(df)
        else:
            st.write("No entities found :(")

    except requests.exceptions.RequestException as e:
        st.error(f"Error during NER processing: {e}")

# Footer
st.write("---")
st.write("Made by Sergio Bank for Sleek")
