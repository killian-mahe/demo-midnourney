import logging

import streamlit as st

from gallery import load_experiments

logger = logging.getLogger(__name__)

st.set_page_config(page_title="Gallery", page_icon=":art:")

experiments = load_experiments()

for experiment in experiments:
    logger.debug("Displaying gallery")
    st.image(experiment["image_path"], caption=experiment["prompt"])
    st.divider()
