import streamlit as st
from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaf_visualization import page_leaf_visualization_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Cherry Leaves & Powder Mildew")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Leaf Visualisation", page_leaf_visualization_body)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()  # Run the app
