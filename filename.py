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
