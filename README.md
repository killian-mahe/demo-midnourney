
# Midjourney demonstration Web app

A tiny Midjourney web demonstrator for Brest AI Days 2023.


# [AI Days](https://www.ai-days.bzh/page-daccueil)

Join us at AI Days Brest, a premier event dedicated to Artificial Intelligence.
Discover the latest advancements in generative AI and attend over 15 panel discussions, demos, and technical sessions.
This free event, organized by French Tech Brest Bretagne Ouest, is open to professionals and curious individuals.
Immerse yourself in the world of AI with real-time demos of autonomous vehicles, ChatGPT/Midjourney, and more.
Don't miss the chance to visit the European Center for Virtual Reality or WINN,
the innovation center of Brest University Hospital. Experience the future of technology at AI Days Brest!

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`USER_TOKEN` : Discord user token

`SERVER_ID` : ID of the server where Midjourney is located

`CHANNEL_ID` : ID of the channel where the messages will be sent

## Installation

Install the project

```bash
  python -m venv env
  source env/bin/activate
  pip install -r requirements.txt
```

## Run Locally

```bash
  streamlit demo_midjourney/__main__.py
```

## Authors

- [@Killian Mahé](https://github.com/killian-mahe)
