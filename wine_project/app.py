import streamlit as st
import pandas as pd
import plotly.express as px

# Judul aplikasi
st.title("Eksplorasi Data Kualitas Anggur")

# Langkah 1: Upload dataset
uploaded_file = st.file_uploader("Upload file dataset Anda (CSV)", type=["csv"])
if uploaded_file is not None:
    # Baca dataset
    data = pd.read_csv(uploaded_file)

    # Tampilkan data awal
    st.write("Berikut adalah beberapa baris dari dataset Anda:")
    st.write(data.head())

    # Langkah 2: Pilih kolom untuk visualisasi
    st.sidebar.header("Pengaturan Visualisasi")
    x_axis = st.sidebar.selectbox("Pilih kolom untuk X-Axis", options=data.columns)
    y_axis = st.sidebar.selectbox("Pilih kolom untuk Y-Axis", options=data.columns)

    # Langkah 3: Buat scatter plot dengan tema yang lebih keren
    st.subheader("Scatter Plot")
    scatter_plot = px.scatter(
        data, 
        x=x_axis, 
        y=y_axis, 
        title="Scatter Plot Interaktif", 
        color=data.columns[0],  # Misalnya menggunakan kolom pertama sebagai warna
        hover_data=data.columns.tolist(),  # Menambahkan data yang lebih detail saat hover
        template='plotly_dark'  # Tema yang lebih modern
    )
    scatter_plot.update_layout(
        title_font=dict(size=20, family='Verdana'),
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0.1)',
        font=dict(color="white")  # Mengubah warna teks agar kontras dengan tema gelap
    )
    st.plotly_chart(scatter_plot)

    # Langkah 4: Filter data berdasarkan nilai (opsional)
    st.subheader("Filter Data (Opsional)")
    filter_column = st.selectbox("Pilih kolom untuk filter", options=data.columns)
    unique_values = data[filter_column].unique()
    selected_value = st.selectbox("Pilih nilai untuk filter", unique_values)
    filtered_data = data[data[filter_column] == selected_value]

    st.write(f"Data yang difilter berdasarkan {filter_column} = {selected_value}:")
    st.write(filtered_data)

    # Scatter plot dari data yang difilter
    st.subheader("Scatter Plot (Data Terseleksi)")
    filtered_plot = px.scatter(
        filtered_data, 
        x=x_axis, 
        y=y_axis, 
        title="Scatter Plot dari Data yang Difilter", 
        color=filter_column,  # Memilih warna berdasarkan kolom filter
        hover_data=filtered_data.columns.tolist(),
        template='plotly_dark'
    )
    filtered_plot.update_layout(
        title_font=dict(size=20, family='Verdana'),
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0.1)',
        font=dict(color="white")
    )
    st.plotly_chart(filtered_plot)
else:
    st.write("Silakan upload dataset untuk memulai.")
