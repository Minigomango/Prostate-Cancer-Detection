"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd

# Import necessary functions from web_functions
from web_functions import predict

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prostate Cancer Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    rad = st.slider("Radius", int(df["radius"].min()), int(df["radius"].max()))
    tex = st.slider("Texture", int(df["texture"].min()), int(df["texture"].max()))
    per = st.slider("Perimeter", int(df["perimeter"].min()), int(df["perimeter"].max()))
    are = st.slider("Area", float(df["area"].min()), float(df["area"].max()))
    smo = st.slider("Smoothness", float(df["smoothness"].min()), float(df["smoothness"].max()))
    com = st.slider("Compactness", float(df["compactness"].min()), float(df["compactness"].max()))
    sym = st.slider("Symmetry", float(df["symmetry"].min()), float(df["symmetry"].max()))
    fad = st.slider("Fractal Dimension", float(df["fractal_dimension"].min()), float(df["fractal_dimension"].max()))
       


    # Create a list to store all the features
    features = [rad,tex,per,are,smo,com,sym,fad]

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=['radius','texture','perimeter','area','smoothness','compactness','symmetry','fractal_dimension']
    st.dataframe(df3)

    
    # Create a button to predict
    if st.button("Detect"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        

        # Print the output according to the prediction
        if (prediction == 1):
            st.sidebar.info("Major parameters affecting Prostate Cancer are its Compactness and Area / Perimeter")
            st.warning("The person has Prostate Cancer!!")
            if (com > 0.09):
                st.write("Cause: Compactness Tumour is High",com)
            elif(are > 550):
                st.write("Cause: Area of Tumour is High",are)
            elif(per > 88):
                st.write("Cause: Perimeter of Tumour is High",per)
        else:
            st.success("The person is safe from Prostate Cancer")

        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
