import streamlit as st
from pathlib import Path

st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)


def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'lebenslauf.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right = st.columns(2)

left.image("profile-pic.png", width=250)

right.markdown("""<h3>Joel Jashari<h3>
               <p>Ich glaube, dass KI jeden Job übernehmen wird.""", unsafe_allow_html=True)
st.download_button(
        label="📄 Download CV",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
    )
st.write("📩", "lisa.bauer@gmx.at")

st.header ("IT-Kompetenzen", anchor=False,  divider="blue")

st.markdown("""
           -Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
           - Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            -Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            -Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            -Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
          
            
            
            
            
            """)

st.header("Arbeitserfahrung",anchor=False,divider="blue")
st.markdown ("""
        - Berufspraktische Tage 1: Bei XYZ von 18. bis 22. Nov. 2024
        - Berufspraktische Tage 2: Bei XYZ von 24. bis 28. Feb. 2025
           """)
