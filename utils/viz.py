import streamlit as st

def show_chart(fig):
    st.plotly_chart(fig, use_container_width=True)
