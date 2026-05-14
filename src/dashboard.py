import streamlit as st
from main import randompass_generator, memorablepass_generator, pin_generator


st.image('data:image/png;base64,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', width=120)
st.title('Password Generator')


option = st.radio(
    'select a password generator:',
    ('Randompassword', 'Memorablepassword', 'PINcode')
)

if option == 'PINcode':
    length = st.slider('length of PIN:', 4, 32, 8)
    password = pin_generator(length)

    st.write(f'**New PINcode is:** ```{password}```')

elif option == 'Randompassword':
    length = st.slider('length of Password:', 4, 70, 8)
    numbers = st.toggle('Includ Numbers')
    symbols = st.toggle('Includ Symbols')
    password = randompass_generator(length=length, numbers=numbers, symbols=symbols )

    st.write(f'**New Randompass is:** ``` {password} ```')

elif option == 'Memorablepassword':
    num_of_words = st.slider('num of words:', 2, 20, 4)
    separator = st.text_input('Separator:', '-')
    capitalize = st.toggle('Capitalize')
    password = memorablepass_generator(num_of_words=num_of_words, capitalize=capitalize, separator=separator)    
    
    st.markdown(f'**New Memorablepass is**: ``` {password} ```')
