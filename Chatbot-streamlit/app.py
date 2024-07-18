import streamlit as st
from streamlit_chat import message

import os
import tempfile
import requests
from base64 import b64encode
from pydantic import BaseModel
from src.utils.logutils import Logger
from src.api import advance_rag_chatbot

from langchain_core.messages import HumanMessage, AIMessage

logger = Logger()

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state["history"] = []

    if "generated" not in st.session_state:
        st.session_state["generated"] = [] #["Hello! Ask me anything about 🤗"]

    if "past" not in st.session_state:
        st.session_state["past"] = [] #["Hi! How can I assist you👋"]
    
    if "df" not in st.session_state:
        st.session_state["df"] = []

def message_func(text, is_user=False):
    """
    This function is used to display the messages in the chatbot UI.

    Parameters:
    text (str): The text to be displayed.
    is_user (bool): Whether the message is from the user or the chatbot.
    """
    question_bg_color = "#f0f0f0"  # Faint grey color
    response_bg_color = "#f0f0f0"  # Faint grey color

    if is_user:
        avatar_url = "https://media.istockphoto.com/id/1184817738/vector/men-profile-icon-simple-design.jpg?s=612x612&w=0&k=20&c=d-mrLCbWvVYEbNNMN6jR_yhl_QBoqMd8j7obUsKjwIM="
        bg_color = question_bg_color
    else:
        avatar_url = "🤖"  # Provided logo link
        bg_color = response_bg_color
            # <div style="display: flex; align-items: center; margin-bottom: 20px;">
    st.write(
        f"""
        <div style=""background: #ffffff;height: 800px;border-radius: 0.75rem;padding: 10px; width:101% !important; overflow-y: scroll;"">
            <img src="{avatar_url}" class="avatar" alt="avatar" style="width: 40px; height: 40px; border-radius: 50%; margin-right: 10px;" />
            <div style="background: {bg_color}; color: black; border-radius: 20px; padding: 10px; max-width: 75%;">
                {text}
            </div>
        </div>
        """,
        unsafe_allow_html=True)

def conversation_chat(query, history):
    logger.info(f"Query {query}")
    logger.info(f"History {history}")
    result = advance_rag_chatbot(query['query'], history, logger)
    # history.append((query, result[0][0])) #history.append(HumanMessage(content=query)), history.append(AIMessage(content=result))
    return result

def main():
    st.set_page_config(
        page_title="Nvidia-CUDA-Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            "About": """This is a Streamlit Chatbot Application designed to solve queries regarding Cuda trained over nividia Cuda docs.
                """
        },
    )

    initialize_session_state()
    st.markdown("""
        <style>
            .top-bar {
                background-color: #f0f0f0;
                color: #5C31FF;
                padding: 10px;
                font-size: 10px;
                text-align: left;
                border-radius: 5px;
            }
            button {
                width: 80px;
                height: 40px;
                content: "Send url('{svg_base64}')";
                padding: 10px;
                background-color: white;
                color: black;
                border: 2px solid black;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                position: fixed;
                bottom: 3rem;
            }
            .stTextInput>div>div>input {
                width: 85% !important;
                padding: 10px;
                background: white;
                border: 1px solid #ccc;
                border-radius: 5px;
                position: fixed;
                bottom: 3rem;
                height: 40px;
            }
            
            section > div.block-container > div {
                background: #ffffff;
                height: 780px;
                border-radius: 0.75rem;
                padding: 10px;
                width:101% !important;
                overflow-y: scroll;
            }
            
            section {
                background: #eeeeee;
            }
            .st-b7 {
                background-color: rgb(255 255 255 / 0%);
            }

            .st-b6 {
                border-bottom-color: rgb(255 255 255 / 0%);
            }

            .st-b5 {
                border-top-color: rgb(255 255 255 / 0%);
            }

            .st-b4 {
                border-right-color: rgb(255 255 255 / 0%);
            }

            .st-b3 {
                border-left-color: rgb(255 255 255 / 0%);
            }
            
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="top-bar">
            <img src="https://w7.pngwing.com/pngs/728/156/png-transparent-nvidia-flat-brand-logo-icon-thumbnail.png" class="logo-img">
        </div>
        """, unsafe_allow_html=True
    )

    container = st.container()
    col1, col2 = st.columns([14, 1])
    with col1:
        user_input = st.text_input(
            "Question: ",
            placeholder="Enter the prompt here...",
            key="input",
            value=st.session_state.get("input", ""),
            label_visibility="hidden",
        )

    with col2:
        st.write("")
        st.write("")
        svg_image = """
        <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 1 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-send"><path d="M10 14l11 -11"></path><path d="M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5"></path></svg>
        """
        svg_base64 = "data:image/svg+xml;base64," + b64encode(svg_image.encode()).decode()

        # Check if the hidden button is clicked
        if st.button("Send", on_click=None):
            data = {
                'query': user_input
            }
            output  = conversation_chat(
                data, st.session_state["history"]
            )
            st.session_state["history"].append((user_input, output[0][0]))
            st.session_state["df"].append({"Question":user_input, "Answer":output[0][0], "Latency":output[1], "Total_Cost($)":output[0][1]})  #we can store this data to mongo or s3 for qa fine-tuning.
            st.session_state["past"].append(user_input)
            st.session_state["generated"].append(output[0][0])

    if st.session_state["generated"]:
        print(st.session_state["generated"])
        with container:
            for i in range(len(st.session_state["generated"])):
                with st.container():
                    message_func(st.session_state["past"][i], is_user=True)
                    message_func(f"{st.session_state["generated"][i]}\n\nLatency:{output[1]} , Total_Cost: ${output[0][1]}")

if __name__ == "__main__":
    main()