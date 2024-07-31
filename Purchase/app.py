import openai
import pandas as pd
import streamlit as st    # Open-source Python Library framework to deliver dynamic data apps
import os

# Set your OpenAI API key here
client=openai.OpenAI(api_key="sk-None-DuOtAWoH3laz6yJtDaHpT3BlbkFJNyAM7dptZMZg8D22bUSH")

# Function to generate technical requirements from business requirements
def generate_technical_requirements(business_requirements):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in transforming business requirements into detailed technical specifications."},
            {"role": "user", "content": f"Transform the following business requirements into measurable technical specifications :\n\n{business_requirements}"}
        ],
        temperature=0.0, #To control variability in the output
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

# Streamlit app setup
st.title("LLM-Based Assistant for Technical Requirements Definition")
st.header("Input Business Requirements")

# Input form
with st.form(key='requirements_form'):
    business_requirements = st.text_area("Enter the business requirements :")
    submit_button = st.form_submit_button(label='Generate Technical Requirements')

# Process input and display output
if submit_button:
    technical_requirements = generate_technical_requirements(business_requirements)
    st.header("Generated Technical Requirements")
    st.text(technical_requirements)

###########################################################

# Function to generate tender from technical requirements

def generate_tender(technical_requirements):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the purchase manager of a large business. It is your responsiblity to create a tender document out of the technical reqirements."},
            {"role": "user", "content": f"Transform the technical requirements into comprehensive tender document:\n\n{technical_requirements}"}
        ],
        temperature=0.1, #To reduce variability in the output
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

# Process input and display output
# if submit_button:

if True:
   tender = generate_tender(technical_requirements)
   st.header("Tender")
   st.text(tender)

##################################################################

# Vendor evaluation

# load vendor performance history file

uploaded_file = st.file_uploader("D://UAE//vendor_history.csv")
vendor_hist = pd.read_csv(uploaded_file)

# Evaluate vendors 

def vendor_evaluation(vendor_hist):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the purchase manager of a large business. It is your responsiblity to select potential suppliers from a list of potential vendors based on their past performance."},
            {"role": "user", "content": f"Evaluate the vendors based on past performance:\n\n{vendor_hist}"}
        ],
        temperature=0.1, #To reduce variability in the output
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

# Generate the vendor evaluation report based on vendor history

if True:
   vendor_evaluation_report = vendor_evaluation(vendor_hist)
   st.header("Vendor evaluation report")
   st.text(vendor_evaluation_report)
