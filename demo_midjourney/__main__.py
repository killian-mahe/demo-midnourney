import re
import time

import streamlit as st

from bot import MidjourneyBot

if __name__ == '__main__':
    bot = MidjourneyBot()

    st.header("Midjourney Demo")

    prompt = st.text_area("Enter your prompt", max_chars=500)

    st.subheader("Result")
    st.write(prompt)

    if prompt != "":
        bot.ask(prompt)

        with st.spinner("Generating image"):

            progress_bar = st.progress(0, text="Starting generation")

            time.sleep(2)

            while True:
                message = bot.messages(1)[0]
                if bot.validate_image_url(message):
                    progress_bar.progress(100, "Generation finished")
                    break

                generation_status = re.search(r'\((.*?)\)', bot.content(message)).group(1)

                try:
                    status = int(generation_status)
                    progress_bar.progress(status, f"Generation in progress")
                except ValueError:
                    progress_bar.progress(0, generation_status)

                time.sleep(3)

            message = bot.messages(1)[0]
            image_url = bot.get_image_url(message)
            st.image(image_url)