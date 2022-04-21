import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App

This app predicts the **Iris flower** type!
""")

# *User Input parameters is added as a heading to the sidebar and the website page.
st.sidebar.header('User Input Parameters')


"""  
#TODO:  user_input_features is a function that will be used to
* create slider(label,min,max,default)  """

# https://docs.streamlit.io/library/api-reference/widgets/st.slider.


def user_input_features():
    # *  st.sidebar.slider('label', min_value, max_value, default value on start)
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)

    # TODO  create a dictionary named 'data' that stores the users selected slider value into the dictionary Key.
    # *data = {'Key': value (slider_value)}

    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}

    # * create pandas DataFrame from the dictionary named 'data'.
    #! pd.DataFrame(dictionary ='data', index[0] = start at column 0 and row 0)
    features = pd.DataFrame(data, index=[0])

    # * return the slider values stored in 'data' to the user_input_features fuction.
    return features


# * assign the user_input_features function to df
df = user_input_features()

st.subheader('User Input parameters')

# * st.write(df)= display the user_input_function
st.write(df)

# * the sklearn.datasets is a module that allows us to load the data set ".load_iris()"
iris = datasets.load_iris()

X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
# st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
