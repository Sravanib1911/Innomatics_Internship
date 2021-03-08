import streamlit as st
from pickle import load
st.markdown('<style>body{background-color: lightgoldenrodyellow;}</style>',unsafe_allow_html=True)

pickle_in = open('svmc.pkl', 'rb')
classifier =load(pickle_in)


def prediction(col1,col2):
    prediction = classifier.predict([[col1,col2]])
    if prediction == 1:
        pred = "Yes"
    else:
        pred = "No"
    return pred


def main():
    st.title('HEROKU DEPLOYMENT')
    col1 = st.number_input('enter a value')
    col2 = st.number_input('enter another value')
    if st.button('Predict'):
        output=prediction(col1,col2)
        st.info(output)



if __name__=='__main__':
    main()
