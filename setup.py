from setuptools import find_packages, setup

setup(
    name='MCQGenerator',
    version='1.0.1',
    description='Generates multiple-choice questions for educational purposes',
    author='Prince Lakhani',
    author_email='princeal3855@gmail.com',
    url='https://github.com/Prince3855',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages(),
),
