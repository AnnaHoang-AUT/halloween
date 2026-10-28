from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='Witch Flight | Halloween 30-Second Challenge', page_icon='🧙‍♀️', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>header[data-testid="stHeader"]{background:transparent} .block-container{padding-top:1rem;max-width:1050px} #MainMenu,footer{visibility:hidden} body{background:#090719}</style>''', unsafe_allow_html=True)
html = (Path(__file__).parent / 'game.html').read_text(encoding='utf-8')
components.html(html, height=820, scrolling=False)
