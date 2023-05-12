import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* powdery mildew, plant disease of worldwide occurrence that causes a  "
        f"powdery growth on the surface of leaves, buds, young shoots, fruits, and flowers.\n"
        f"* The white powdery appearance is due to large numbers of microscopic spores borne in chains.  "
        f"These wind-borne spores uniquely do not require free water for germination and infection.\n"
        f"* If the disease is severe, the mildewed plant parts may be stunted and distorted.  "
        f"Leaves commonly turn yellow and wither, flowers are distorted or fewer in number,  "
        f"and fruit yield and quality are reduced.\n\n "

        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 images containing "
        f"cherry leaves in varying shapes and sizes, half of these are "
        f"mildew-parasitised and the other half are healthy.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Code-Institute-Solutions/WalkthroughProject01/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to  "
        f"visually differentiate a healthy cherry leaf from one with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
    )
