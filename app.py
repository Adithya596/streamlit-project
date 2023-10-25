import streamlit as st
import requests
import streamlit_lottie as sl
from PIL import Image

st.set_page_config(page_title="IPS tech community", page_icon="♾",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

with st.container():
    st.subheader("Hello there! :wave:")
    st.title("Welcome to our IPS Tech community!")
    st.write("[our webpage!](https://google.com)")



lottie_link = load_lottieurl("https://lottie.host/54366d44-4fef-49b9-91e5-77a8f1683767/s1oTaMP8D9.json")
img_contact = Image.open("streamlit\images\download.png")
form = """
<form action="https://formsubmit.co/adithya14255@gmail.com" method="POST">
     <input type="your name" name="name" placeholder ="enter your name" required>
     <input type="your email" name="email" placeholder ="enter your email" required>
     <textarea name="message" placeholder="enter your feedback or questions!"></textarea>
     <button type="submit">Send</button>
</form>"""


with st.container():
    st.write("---")
    st.write("Here are some of our projects - ")
    left,right = st.columns((1,2))
    with left:
        st.subheader("PyExpo!")
        st.write("##")
        st.write("Conducted in KITE coimbatore!")
        st.write("completely planned and organized by the students!")
        st.write("A melting pot of learning and tech culture")
        st.write("[check it out -!](https://youtu.be/dQw4w9WgXcQ)")
    with right:
        sl.st_lottie(lottie_link,height=320)

with st.container():
    st.write("---")
    st.write("here is the logo for pyexpo - ")
    st.image(img_contact,width=150)


with st.container():
    st.write("---")
    st.write("send me a message!")
    right,left = st.columns((1,2))
    with right:
        st.markdown(form,unsafe_allow_html=True)
        css("streamlit\style\style.css")
