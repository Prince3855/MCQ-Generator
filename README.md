﻿# MCQ-Generator
A web application that generates multiple-choice questions (MCQs) based on a given text or PDF file.

## Description

This application uses the following dependencies:

- [LangChain](https://github.com/hwchase17/langchain): A framework for building applications with LLMs.
- [Streamlit](https://streamlit.io/): A fast, easy-to-use, and powerful web application framework for creating data apps.

The app generates MCQs based on the number of required MCQs and complexity. To create MCQs, you need to provide a text or PDF file containing the content you want to use for generating questions. The app extracts text from the provided file and uses LangChain to generate questions and answers.

The generated MCQs are displayed in a user-friendly interface, allowing users to select their answers and view the correct answers.

Feel free to customize the app according to your specific requirements.


## Local setup

1. Cloan repository
    ```
    git clone https://github.com/Prince3855/MCQ-Generator.git
    ```

2. Move inside the repository
    ```
    cd MCQ-Generator
    ```

3. Create a virtual environment
    For example if you are using `conda` then try this command
    ```
    conda create -p venv python=3.8 -y
    ```

4. Activate the virtual environment
    ```
    source activate ./venv
    ```

5. Install dependencies
    ```
    pip install -r requirements.txt
    ```

6. Create `.env` file using `.example.env` file and update values of variables

7. To run the application execute the following command
    ```
    streamlit run StreamlitAPP.py
    ```

## Demo

[streamlit-StreamlitApp-2024-08-24-11-08-74.webm](https://github.com/user-attachments/assets/72bb2a36-3d35-43a0-81b1-b4c82155d111)
