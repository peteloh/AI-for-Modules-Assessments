import streamlit as st
import io

#custom imports
import sca

st.set_page_config(
    page_title="Code Marker",
    layout='wide'
    )

if __name__ == '__main__': 

    col1, col2 = st.sidebar.columns((2,1))
    col1.image("./images/imperial_logo.png")

    st.sidebar.header("AI for Modules Assessment")
    st.sidebar.text("""Developed by Patapee Lohprasert""")
    st.sidebar.markdown("#")


    st.title('Code Marking Assistant')

    # Input Codes and Store Them in class "code"
    with st.container():
        col1, col2 = st.columns((1,1))
        upload1 = col1.file_uploader("Upload Solution Code")
        upload2 = col2.file_uploader("Upload Student Codes", accept_multiple_files=True)

        if upload1 != None:
            upload1_code_strings = io.StringIO(upload1.getvalue().decode("utf-8")).read()
            MODEL_CODE = sca.analyse(upload1_code_strings)

        if upload2 != None:
            STUDENT_CODE = {}
            for upload in upload2:
                code_string = io.StringIO(upload.getvalue().decode("utf-8")).read()
                STUDENT_CODE[upload.name] = sca.analyse(code_string)

    # Store what SCA Tests have to be done on student codes (do we also want to do on model code?)
    with st.container():
        sca_tests = {
            "Count Nested Loops": False
        }

        col1, col2 = st.columns((1,1))

        col1.subheader("Static Code Analysis")
        col2.subheader("Test Cases")

        if col1.checkbox('Count Nested Loops'):
            loop_to_check = col1.multiselect('Pick Either or Both',['For Loop', 'While Loop'])
            sca_tests['Count Nested Loops'] = True

    st.markdown('#')   
    if st.button('Start'):

        st.header('Student Results')

        if upload1 != None:
            st.sidebar.header("**MarkScheme**")
            # with st.sidebar.expander('Model Code', expanded=True):
            st.sidebar.markdown("**Model Code**")
            st.sidebar.code(MODEL_CODE.long_string_with_comments)
        
        if upload2 != None:
            with st.container():
                for key in STUDENT_CODE.keys():
                    with st.expander(str(key)):
                        col1, col2 = st.columns((1,1))
                        col1.markdown("**Input Code**")
                        col1.code(STUDENT_CODE[key].long_string_with_comments)

                        col2.markdown("**Analysis**")
                        if sca_tests['Count Nested Loops'] == True: 
                            col2.text("Number of Nested Loop = " + str(sca.find_nested_loops(STUDENT_CODE[key], loop_to_check)))
        
                    






    
    