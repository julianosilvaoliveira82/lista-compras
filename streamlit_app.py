import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Lista de Compras", layout="wide")

# Esconde a "moldura" do Streamlit para ficar o mais parecido possível com o HTML standalone
st.markdown(
    """
    <style>
      .block-container { padding-top: 0rem; padding-bottom: 0rem; }
      header[data-testid="stHeader"] { display: none; }
      footer { display: none; }
      [data-testid="stToolbar"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("index.html")

if not html_path.exists():
    st.error("Arquivo index.html não encontrado ao lado do streamlit_app.py. Coloque o index.html na raiz do repositório.")
    st.stop()

html = html_path.read_text(encoding="utf-8")

# Renderiza o HTML dentro de um iframe.
# Dica: aumente o height se sua lista ficar muito longa.
components.html(html, height=2200, scrolling=True)
