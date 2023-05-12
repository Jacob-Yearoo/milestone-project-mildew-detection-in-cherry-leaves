import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect mildew-infected leaves have clear differences that visually set them apart, "
        f"typically with an infected leaf, you will see a white powdery fungus. \n\n"
        f"* An Image Montage shows that typically an infected leaf has white fungus on the surface layer. "
        f" Average Image and Difference between Averages studies did reveal "
        f"that healthy cherry leaves are a more vibrant colour and infected ones are more withered and dull."

    )
