import streamlit as st
import pandas as pd

st.title('Analisis Bike Sharing Dataset')

# Upload file
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())

    # Analisis sederhana
    st.subheader('Statistik Deskriptif')
    st.write(data.describe())

    st.subheader('Jumlah Sepeda Berdasarkan Hari')
    daily_counts = data.groupby('dteday')['cnt'].sum().reset_index()
    st.line_chart(daily_counts.set_index('dteday'))
