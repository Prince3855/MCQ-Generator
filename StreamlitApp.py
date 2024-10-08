import json
import traceback
import pandas as pd
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain_community.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain


# load json file
with open('Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

# app titile
st.title("MCQ Creator Application with Langchain")

# create from using st.form
with st.form('user_inputs'):
    # file upload
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    # input fields
    # mcq count
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)

    # subject
    subject = st.text_input("Insert a Subject", max_chars=20)

    # Quiz Tone
    tone = st.text_input("Complexity Level of Question", max_chars=20, placeholder='Simple')

    # Add button
    button = st.form_submit_button("Create MCQs")

    # Validate data on submit
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner('Loading...'):
            try:
                text = read_file(uploaded_file)

                # count tokens and API cost
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject":subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("An error occurred while processing your request.")
            
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")

                if isinstance(response, dict):
                    # extract quiz data from response
                    quiz = response.get('quiz', None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)

                            st.text_area(label="Review", value=response['review'])
                        else:
                            st.error("No MCQs generated.")
                else:
                    st.write(response)

