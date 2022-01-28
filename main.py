import streamlit as st

if __name__ == '__main__': 

    st.sidebar.title('Read Me')
    st.sidebar.header('How to Use')
    st.sidebar.write('[description]')

    st.header('Inputs')  
    uploaded_file = st.file_uploader("Choose a file")

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

    st.header('Inputs Summary')  
    st.write('Max Nested Loops =', number_nested_loops)
    if number_nested_loops > 0:
        st.write('ExpectedRunCount =', ExpectedRunCount_Dict)

    st.write('Return Parameter Type =', return_type)
