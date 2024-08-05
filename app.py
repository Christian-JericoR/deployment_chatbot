import streamlit as st
from streamlit_chat import message
from streamlit_option_menu import option_menu
import pickle
import string
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random

st.set_page_config(
    page_title="ParuCekBot - 🫁",
    page_icon="👾"
)

# Navigasi
selected = option_menu(None, ["ParuCekBot", "Tentang"], 
                       icons=['house', "list-task"], 
                       menu_icon="cast", default_index=0, orientation="horizontal")

# Definisikan fungsi untuk logika chatbot
def input_data():
    st.write("Selamat datang di menu deteksi penyakit paru, mohon jawab list pertanyaan berikut:")
    jenisKelamin = st.text_input("Apa jenis kelamin anda (pria / wanita)?")
    usia = st.text_input("Berapa usia anda?")
    merokok = st.text_input("Apakah anda merokok?")
    jarikuning = st.text_input("Apakah jari anda berwarna kuning?")
    kecemasan = st.text_input("Apakah anda punya riwayat kecemasan?")
    kesehatanmental = st.text_input("Apakah anda punya riwayat kesehatan mental?")
    penyakitkronis = st.text_input("Apakah anda punya riwayat sakit kronis?")
    kelelahan = st.text_input("Apakah anda punya riwayat kelelahan?")
    alergi = st.text_input("Apakah anda punya riwayat sakit alergi?")
    mengi = st.text_input("Apakah anda punya riwayat mengi?")
    konsumsialkohol = st.text_input("Apakah anda konsumsi minuman mengandung alkohol?")
    batuk = st.text_input("Apakah anda mengalami batuk?")
    sesaknapas = st.text_input("Apakah anda mengalami sesak nafas?")
    kesulitanmenelan = st.text_input("Apakah anda mengalami kesulitan menelan?")
    nyeridada = st.text_input("Apakah anda mengalami nyeri pada dada?")
    
    return {
        "jenisKelamin": jenisKelamin,
        "usia": usia,
        "merokok": merokok,
        "jarikuning": jarikuning,
        "kecemasan": kecemasan,
        "kesehatanmental": kesehatanmental,
        "penyakitkronis": penyakitkronis,
        "kelelahan": kelelahan,
        "alergi": alergi,
        "mengi": mengi,
        "konsumsialkohol": konsumsialkohol,
        "batuk": batuk,
        "sesaknapas": sesaknapas,
        "kesulitanmenelan": kesulitanmenelan,
        "nyeridada": nyeridada
    }

def konfirmasi_data(data):
    st.write("Terima kasih telah mengisi survey. Apakah data kamu benar sebagai berikut:")
    for k, v in data.items():
        st.write(f"{k}: {v}")
    
    konfirmasi = st.text_input("Jika sudah sesuai input 1, jika tidak sesuai input 0:")
    return konfirmasi == "1"

def preprocess_data(data):
    # Konversi data kategori ke numerik
    processed_data = [
        1 if data['jenisKelamin'].lower() == 'pria' else 0,    # jenisKelamin
        int(data['usia']),                                     # usia
        2 if data['merokok'].lower() == 'ya' else 0,           # merokok
        2 if data['jarikuning'].lower() == 'ya' else 0,        # jarikuning
        2 if data['kecemasan'].lower() == 'ya' else 0,         # kecemasan
        2 if data['kesehatanmental'].lower() == 'ya' else 0,   # kesehatanmental
        2 if data['penyakitkronis'].lower() == 'ya' else 0,    # penyakitkronis
        2 if data['kelelahan'].lower() == 'ya' else 0,         # kelelahan
        2 if data['alergi'].lower() == 'ya' else 0,            # alergi
        2 if data['mengi'].lower() == 'ya' else 0,             # mengi
        2 if data['konsumsialkohol'].lower() == 'ya' else 0,   # konsumsialkohol
        2 if data['batuk'].lower() == 'ya' else 0,             # batuk
        2 if data['sesaknapas'].lower() == 'ya' else 0,        # sesaknapas
        2 if data['kesulitanmenelan'].lower() == 'ya' else 0,  # kesulitanmenelan
        2 if data['nyeridada'].lower() == 'ya' else 0          # nyeridada
    ]
    return processed_data

def prediction(data):
    with open('model.pickle', 'rb') as file:
        model2 = pickle.load(file)
    prediction = model2.predict([data])
    st.write("Hasil prediksi:", prediction)

def chatbot_response(prediction_input):
    # Muat model dan tokenizer
    with open('tokenizers.pkl', 'rb') as handle:
        tokenizer = pickle.load(handle)
    with open('le.pkl', 'rb') as handle:
        le = pickle.load(handle)
    
    model = pickle.load(open('model.h5', 'rb'))
    
    texts_p = []
    
    # Bersihkan dan preprocess input
    prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
    prediction_input = ''.join(prediction_input)
    texts_p.append(prediction_input)
    
    # Tokenisasi dan padding
    prediction_input = tokenizer.texts_to_sequences(texts_p)
    prediction_input = np.array(prediction_input).reshape(-1)
    prediction_input = pad_sequences([prediction_input], maxlen=20)
    
    # Dapatkan output model
    output = model.predict(prediction_input)
    output = output.argmax()
    
    # Dapatkan respon berdasarkan tag output
    response_tag = le.inverse_transform([output])[0]
    responses = {
        "greeting": ["Hello!", "Hi there!", "Greetings!"],
        "goodbye": ["Goodbye!", "See you later!", "Take care!"],
        # Tambahkan lebih banyak respon sesuai kebutuhan
    }
    jawaban = random.choice(responses.get(response_tag, ["Saya tidak mengerti."]))
    st.write("🤖 ParuCekBot: ", jawaban)
    
    return response_tag

# Tampilan untuk antarmuka Chatbot
if selected == "ParuCekBot":
    st.markdown(
        """
        <style>
        .center-text {
            text-align: center;
        </style>
        <h1 class="center-text">🤖 ParuCekBot - 🫁</h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown(""" Tanya ParuCekBot

Hai, aku ParuCekBot👋. Mulai dengan menyapa aku untuk memulai chat :smile:
""", True)
    
    # Input pengguna
    def get_text():
        input_text = st.text_input("Mulai Pertanyaan: ", "Hai?", key="input")
        return input_text

    user_input = get_text()
    
    if user_input:
        response_tag = chatbot_response(user_input)
        
        if response_tag == "goodbye":
            data = input_data()
            if konfirmasi_data(data):
                processed_data = preprocess_data(data)
                prediction(processed_data)
            else:
                st.write("Silakan isi data kembali.")
                data = input_data()
                processed_data = preprocess_data(data)
                prediction(processed_data)

# Tampilan untuk bagian Tentang
if selected == "Tentang":
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
    Seperti yang telah disebutkan, **ParuCekBot** merupakan chatbot yang dapat berkomunikasi dalam format percakapan dan dirancang untuk bisa berinteraksi. Pondasi dibalik teknologi chatbot sendiri adalah teknologi Artificial Intelligence (AI), 
    cabang ilmu komputer yang berkaitan dengan pemecahan masalah-masalah selayaknya manusia seperti berbicara, 
    memahami, ataupun berpikir🥳.
    
    Salah satu bidang dalam AI yang membuat chatbot dapat memproses bahasa alami manusia adalah Natural Language Processing (NLP).

    **Model ChatBot** ini masih memiliki batasan-batasan. **Model ChatBot** tidak selalu dapat memberikan jawaban yang benar untuk pertanyaan yang bersifat subjektif, atau yang memerlukan pengetahuan yang spesifik dan up-to-date. 
    **Model ChatBot** ini juga membutuhkan data latih yang cukup banyak untuk dapat berfungsi dengan baik dan akurat.
    """, True)
    st.write("---")
    st.markdown("""
    ### 📑Proses Pembuatan ParuCekbot
    Dalam proses pembuatan ParuCekBot,
    """, True)
    st.write("---")

# Sembunyikan menu Streamlit default
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
