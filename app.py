import streamlit as st
import sca

if __name__ == '__main__': 

    st.sidebar.title('Read Me')
    st.sidebar.header('How to Use')
    st.sidebar.write('This user interface is still under development')

    st.title('ME1 Code Marking Assistant')
    st.header('Input Parameters')  
    st.subheader('Python Codes')  
    teacher_code = st.file_uploader("Upload Solution Code")
    student_code = st.file_uploader("Upload Student Codes (Multiple Upload)", accept_multiple_files=True)

    st.subheader('Checking Rules')  
    number_nested_loops = int(st.select_slider(
        'Select the maximum number of nested loop',
        options=['0', '1', '2', '3', '4', '5']))
    
    if number_nested_loops > 0:
        ExpectedRunCount_Dict = {} # dict
        for i in range(1,number_nested_loops+1):
            ExpectedRunCount_Dict["Loop"+str(i)] = st.text_input('Loop {i} ExpectedRunCount'.format(i=i),value ="any")
    
    return_type = st.multiselect(
        'Choose the type of the return parameter, if not a function please choose None',
        options=['None','String', 'Int', 'Float', 'List', 'Array'])
    
    st.sidebar.write("other checking rules once developed will be shown here")

    st.subheader('Checklist Summary')  
    st.write('Max Nested Loops =', number_nested_loops)
    if number_nested_loops > 0:
        st.write('ExpectedRunCount =', ExpectedRunCount_Dict)

    st.write('Return Parameter Type =', return_type)

    st.header('Results')  
    st.write('This section will show the results of each student code and allow export as csv')
    st.write('This section is underdevelopment')