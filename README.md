# Grammar_checker

##SETUP
pip install gingerit

this package in python is used for Correcting spelling and grammar mistakes based on the context of complete sentences. Wrapper around the gingersoftware.com API

pip install streamlit 

Streamlit is an open-source app framework in python language. It helps us create beautiful web apps for data science and machine learning in a little time.

Once this is done we are good to go

###CODE

from gingerit.gingerit import GingerIt
import streamlit as st
st.title("Grammar Checker")
text=st.text_area("Enter text:",
                  value='',
                  height=None,
                  max_chars=None,
                  key=None)
parser=GingerIt()

if st.button("Correct Sentence="):
    if text== '':
        st.write("Please enter the text for checking")
    else:
        result_dict=parser.parse(text)
        st.markdown("** Corrected Senttence = " + str(result_dict["result"]))
else:
    pass


TO RUN THIS CODE 
GO TO THE TERMINAL AND WRITE THIS COMMAND 
streamlit run filename.py

THIS WILL DIRECT YOU TO A PAGE AS BELLOW 
