import streamlit as st
from utils.io import load_data
from utils.prep import make_tables
from sections import intro, overview, deep_dives, conclusions

st.set_page_config(page_title="Cost of Living Dashboard", layout="wide")

@st.cache_data
def get_data():
    df = load_data("data/cost-of-living.csv")
    tables = make_tables(df)
    return df, tables


st.markdown("""
<h1 style='text-align: center; font-size: 96px; color: #27BEF5;'>
Cost of Living Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stTabs [data-baseweb="tab"] {
        font-size: 20px;
        padding: 12px 24px;
    }
            
    .stTabs [aria-selected="true"] {
    background-color: #27BEF5;
    color: white;
    font-weight: bold;
    }

    </style>
""", unsafe_allow_html=True)


st.markdown("""
**Source** : [Numbeo](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living)
""")

df, tables = get_data()

import streamlit as st
from sections import intro, overview, deep_dives, conclusions

st.set_page_config(page_title="Cost of Living Dashboard", layout="wide")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Intro", "Overview", "Deep Dives", "Conclusions"])

if page == "Intro":
    intro.show()
elif page == "Overview":
    overview.show(tables)
elif page == "Deep Dives":
    deep_dives.show(tables)
elif page == "Conclusions":
    conclusions.show()