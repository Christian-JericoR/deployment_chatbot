import streamlit as st
from streamlit_chat import message
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="ParuCekBot - 🫁",
    page_icon="👾"
)

# Navigasi
selected = option_menu(None, ["ParuCekBot", "About"], 
        icons=['house', "list-task"], 
        menu_icon="cast", default_index=0, orientation="horizontal",)

# Awal Content Chatbot

# Untuk Codingan model LSTM
# Isi Codingan algoritma
# jeda 1 line utuk isi dari codingan model chatbot

# View ( "Tampilan Chatbot")
if selected == "ParuCekBot":
    st.markdown(
        """
        <style>
        .center-text {
            text-align: center;
        }
        </style>
        <h1 class="center-text">🤖 ParuCekBot - 🫁</h1>
        """,
        unsafe_allow_html=True
    )
if selected == "ParuCekBot":
 st.markdown(""" Tanya ParuCekBot

Hai, aku ParuCekBot👋. Mulai dengan menyapa aku untuk memulai chat :smile:
""", True)
 
 # input pengguna
 def get_text():
    input_text = st.text_input("Mulai Pertanyaan: ","Hai?", key="input")
    return input_text 
 
 # Respone Chatbot
 user_input = get_text()
 
# Akhir Content Chatbot

# Awal Content About
if selected == "About":
    st.markdown("""# 🤖 ParuCekBot - 🫁
### Hallo Sahabat 👋

🤖 Aku ParuCekBot👋

Aku adalah asisten virtual yang dibuat menggunakan model algoritma Long Short Term-Memory (LSTM).

ParuCekBot mempunyai 2 fitur yaitu:
1. Media informasi untuk penyakit kanker paru
2. Prediksi Kanker paru
""", True)
    st.write("---")
    st.markdown("""
    ### Teknologi Yang Ada di ParuCekBot 🤖
    Seperti yang telah disebutkan,**ParuCekBot** merupakan chatbot yang dapat berkomunikasi dalam format percakapan dan dirancang untuk bisa berinteraksi. Pondasi dibalik teknologi chatbot sendiri adalah teknologi Artificial Intelligence (AI), 
    cabang ilmu komputer yang berkaitan dengan pemecahan masalah-masalah selayaknya manusia seperti berbicara, 
    memahami, ataupun berpikir🥳.
    
    Salah satu bidang dalam AI yang membuat chatbot dapat memproses bahasa alami manusia adalah Natural Language Processing (NLP).

    **Model ChatBot** ini masih memiliki batasan-batasan. **Model ChatBot** tidak selalu dapat memberikan jawaban yang benar untuk pertanyaan yang bersifat subjektif, atau yang memerlukan pengetahuan yang spesifik dan up-to-date. 
    **Model ChatBot** juga belum mampu memberikan informasi yang sangat detail.
    Selain itu, **Model ChatBot** ini juga membutuhkan data latih yang cukup banyak untuk dapat berfungsi dengan baik dan akurat.
    
    """, True)
    st.write("---")

    st.markdown("""
    ### 📑Proses Pembuatan ParuCekbot
    Dalam proses pembuatan ParuCekBot,
    
    """, True)

    st.write("---")
# Akhir Content About

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)