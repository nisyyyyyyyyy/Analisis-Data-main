import streamlit as st
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

st.title(" Dashboard Proyek Analisis Data")  
st.header('Bike Sharing Dataset')  
st.subheader('Tingkat  antusiasme  pelanggan dalam meminjam sepeda ')
def plot_antusiasme_chart():       
    antusiasme_pelanggan = {
        'Hari': ['Minggu','Senin', 'Selasa','Rabu', 'Kamis','Jumat','Sabtu' ],
        'Jumlah': [105, 105,104,104,104,104,105]  # Jumlah pelanggan untuk setiap hari
    }

     # Membuat DataFrame dari data dummy diatas
    df = pd.DataFrame(antusiasme_pelanggan)

    # Mengurutkan DataFrame berdasarkan kolom 'Hari'
    df_sorted = df.sort_values(by='Hari')

    # Menampilkan chart menggunakan Matplotlib
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Hari'], df_sorted['Jumlah'], color='pink')  

    # Menambahkan caption jumlah data di atas setiap bar
    for i, v in enumerate(df_sorted['Jumlah']):
        ax.text(i + 1, v + 10, str(v), ha='center', va='bottom')
    ax.set_xlabel('Hari')
    ax.set_ylabel('Jumlah')
    ax.set_title('Tingkat Antisiasme Pelanggan dalam Meminjam Sepeda')
    
    # Menampilkan chart menggunakan st.pyplot()
    st.pyplot(fig)

plot_antusiasme_chart()
# Memanggil fungsi untuk menampilkan chart


with st.expander("See explanation"):
    st.write(
        """Berdasarkan grafik diatas menunjukkan bahwa pelanggan lebih banyak meminjam sepeda pada hari minggu dan senin. Namun grafik inj cenderung konstan sehingga dapat dikatakan bahwa jumlah pelanggan yang meminjam sepeda relatif konstan.
        """
    )

st.subheader("Persebaran Pelanggan Berdasarkan Jenis Hari")
def plot_jenis_distribution():  
    Jenis_Hari   = {
        'Jenis_Hari': ['Holiday','Workingday'],   
        'Jumlah': [231,500]  # Jumlah pelanggan untuk workingday dan holiday
    }
    df = pd.DataFrame(Jenis_Hari)
    df_sorted = df.sort_values(by='Jumlah', ascending=False)
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Jenis_Hari'], df_sorted['Jumlah'], color='skyblue')
    for i, v in enumerate(df_sorted['Jumlah']):
        ax.text(i, v + 10, str(v), ha='center', va='bottom')

    ax.set_xlabel('Jenis Hari')  
    ax.set_ylabel('Jumlah pelanggan')  
    ax.set_title('Persebaran Pelanggan Berdasarkan Jenis Hari')  
    st.pyplot(fig)
plot_jenis_distribution()   
with st.expander("See explanation"):
    st.write(
        """Berdasarkan grafik diatas dapat disimpulkan bahwa  pada workingday jumlah pelanggan lebih banyak dibandingkan dengan jumlah pelanggan diluar workingday.

"""
    )
 
st.subheader('Kesimpulan')
st.write(
        """Dengan demikian dapat disimpulkan bahwa jumlah pelanggan setiap harinya konstan dan lebih banyak di workingday daripada diluar workingday(holiday)."""
)  