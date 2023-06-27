import re
import time
import pathlib
import logging

import streamlit as st
from dotenv import load_dotenv

from bot import MidjourneyBot
from gallery import save_experiment

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if pathlib.Path(".env").exists():
    logging.info("Loading environment variables from file.")
    load_dotenv(".env")
else:
    logging.warning("No environment variables file found.")

st.set_page_config(page_title="Midjourney", page_icon=":art:")

if __name__ == "__main__":
    bot = MidjourneyBot()

    st.header("Midjourney Demo")

    prompt = st.text_area("Enter your prompt", max_chars=500)

    if prompt != "" and st.button("Submit"):
        st.subheader("Result")
        st.markdown(f"**Your prompt :** {prompt}")

        with st.spinner("Generating image"):
            bot.ask(prompt)

            progress_bar = st.progress(0, text="Starting generation")

            time.sleep(2)

            while True:
                message = bot.messages(1)[0]

                if bot.validate_image_url(message):
                    progress_bar.progress(100, "Generation finished")
                    break

                generation_status = re.search(r"\((.*?)\)", bot.content(message)).group(
                    1
                )

                try:
                    status = int(generation_status[:-1])
                    progress_bar.progress(status, f"Generation in progress")
                except ValueError:
                    progress_bar.progress(0, generation_status)

                time.sleep(3)

            message = bot.messages(1)[0]
            image_url = bot.get_image_url(message)

            save_experiment(prompt, bot.get_image(image_url))
            st.image(image_url)
