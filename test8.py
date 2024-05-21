import streamlit as st
import pandas as pd
import base64
import requests

from streamlit_lottie import st_lottie


# Fungsi untuk mengatur warna background
def set_background_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    
def show_Home():
    st.title("Home")

    # Pemilihan warna background
    color = st.color_picker("Pilih warna untuk background:", "#FFFFFF")
    set_background_color(color)

    # file json format (File path)
    lottie_url = "https://lottie.host/8585b30c-3f7a-4730-a70f-f812b061be4c/m3HYoJH7FC.json"

    # Fungsi untuk memproses lottie url
    def load_lottie_url(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Memproses animasi lottie
    lottie_json = load_lottie_url(lottie_url)

    # Menampilkan animasi lottie
    if lottie_json is not None:
        st_lottie(lottie_json)
    else:
        st.write("Failed to load Lottie animation.")


def show_InformasitentangNormalitas():
    # Tabel informasi tambahan
    st.markdown("<h1 style='color:pink'>𓇼Informasi tentang Normalitas𓇼</h1>", unsafe_allow_html=True)
    st.write('Normalitas dapat diartikan sebagai jumlah mol ekuivalen dari suatu zat per liter larutan.')
    st.write('Normalitas adalah ukuran yang menunjukkan konsentrasi pada berat setara dalam gram per liter larutan. Berat ekivalen itu sendiri adalah ukuran kapasitas reaktif molekul yang dilarutkan dalam larutan. Dalam suatu reaksi, tugas zat terlarut adalah menentukan normalitas suatu larutan. Normalitas juga disebut satuan konsentrasi larutan ekivalen.')
    st.header('Jenis-jenis Normalitas dalam Kimia', divider='red')
    st.write(' normalitas sering digunakan dalam tiga jenis reaksi, yaitu reaksi asam basa, reaksi redoks, dan reaksi pengendapan. Berikut penjelasan mengenai penggunaan normalitas dalam ketiga reaksi tersebut. ')
    st.write('~ Dalam reaksi asam basa, normalitas digunakan untuk menunjukkan konsentrasi ion hidronium (H3O+) atau ion hidroksida (OH) dalam suatu larutan')
    st.write('~ Dalam reaksi reduksi oksidasi atau reaksi redoks, normalitas digunakan untuk menentukan jumlah elektron yang dapat diberikan atau diterima oleh zat pereduksi atau pengoksidasi. ')
    st.write('~ Dalam reaksi deposisi atau pengendapan, normalitas digunakan untuk mengukur jumlah ion yang dilepaskan dalam larutan oleh endapan yang terbentuk dari suatu proses pengendapan. ')
    st.header('Rumus Normalitas', divider='red')
    st.write('N= bobot baku primer/BE baku primer x V titrat ')


def calculated_KalkulatorPerhitunganNormalitas():
    st.header('Perhitungan Normalitas')
    massa = st.number_input('Masukkan nilai massa (mg):')
    volume = st.number_input('Masukkan nilai volume (mL):')
    BE1 = st.number_input('Masukkan nilai BE:')
    FP1 = st.number_input('Masukkan nilai Faktor Pengali/ jika tidak ada Faktor Pengali cukup menuliskan angka 1:')

    tombol = st.button('Hitung nilai normalitasnya')

    if tombol:
        nilai_normalitas1 = massa/(BE1*volume*FP1)
        st.success(f'nilai normalitas adalah {nilai_normalitas1}')

def show_Informasitentang_KadarLarutan():
    st.markdown("<h1 style='color:pink'>𐙚 Informasi Kadar Larutan 𐙚 </h1>", unsafe_allow_html=True)
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, indigo,violet);"/>',
                unsafe_allow_html=True)
    st.write('Larutan adalah campuran homogen (komposisinya sama), serba sama (ukuran partikelnya), tidak ada bidang batas antara zat pelarut dengan zat terlarut (tidak dapat dibedakan secara langsung antara zat pelarut dengan zat terlarut), partikel- partikel penyusunnya berukuran sama (baik ion, atom, maupun molekul) dari dua zat atau lebih. Dalam larutan fase cair, pelarutnya (solvent) adalah cairan, dan zat yang terlarut di dalamnya disebut zat terlarut (solute), bisa berwujud padat, cair, atau gas. Dengan demikian, larutan = pelarut (solvent) + zat terlarut (solute). Khusus untuk larutan cair, maka pelarutnya adalah volume terbesar.')
    st.header('informasi tentang Kadar%(b/v)', divider='grey')
    st.write('Persen berat volume %(b/v) menyatakan jumlah (gram) massa zat terlarut dalam 100(mL) larutan.')
    st.write('rumus kadar%(b/v)= (Vtitran x Ntitran x BE titrat)x10^-3 x 100% / Volume titran(mL).')
    st.header('informasi tentang Kadar%(b/b)', divider='grey')
    st.write('Persen berat volume %(b/v) menyatakan jumlah (gram) massa zat terlarut dalam 100(gram) larutan.')
    st.write('rumus kadar%(b/v)= (Vtitran x Ntitran x BE titrat)x10^-3 x 100% / Volume titran(mg).')
          
def calculated_Kalkulator1PerhitunganKadar():
    st.header('Perhitungan Kadar %(b/v)')
    st.write('Jika sampel titratnya dipipet maka menggunakan Volume titrat (mL)')
    Vtitran = st.number_input('Masukkan nilai volume titran (mL)')
    Ntitran = st.number_input('Masukkan nilai normalitas titran (N):')
    BE2 = st.number_input('Masukkan nilai BEnya:')
    FP2 = st.number_input('Masukkan nilai Faktor Pengalinya/jika tidak ada Faktor Pengali cukup menuliskan angka 1:')
    Vtitrat = st.number_input('Masukkan nilai volume titrat (mL):')

    tombol = st.button('Hitung nilai kadarnya')

    if tombol:
        nilai_kadar = (Vtitran*Ntitran*BE2*10**-3*FP2*100)/Vtitrat 
        st.success(f'Persentase kadarnya adalah {nilai_kadar}')


def calculated_Kalkulator2PerhitunganKadar():
    st.header('Perhitungan Kadar %(b/b)')
    st.write('Jika sampel titratnya dipipet maka menggunakan Volume titrat (mL)')
    Vtitran = st.number_input('Masukkan nilai volume titran (mL)')
    Ntitran = st.number_input('Masukkan nilai normalitas titran (N):')
    BE2 = st.number_input('Masukkan nilai BEnya:')
    FP2 = st.number_input('Masukkan nilai Faktor Pengalinya/jika tidak ada Faktor Pengali cukup menuliskan angka 1:')
    Vtitrat = st.number_input('Masukkan nilai bobot titrat (mg):')

    tombol = st.button('Hitung nilai kadarnya')

    if tombol:
        nilai_kadar = (Vtitran*Ntitran*BE2*10**-3*FP2*100)/Vtitrat 
        st.success(f'Persentase kadarnya adalah {nilai_kadar}')

def Our_Team () :
    st.header("_Meet The Team_")

    # Team Members
    team_data = [
        {"name": "Aufa azhzhahra dalillh HFB ","NIM": "2360079", "image_url": "imgs/aufa.png"},
        {"name": "Amanda Adistya Pasya ", "NIM": "2360067", "image_url": "imgs/amanda.png"},
        {"name": "Nayla Putri Dwinta ", "NIM": "2360209", "image_url": "imgs/nayla.png"},
        {"name": "Rizky Amelia Putri ", "NIM": "2360247", "image_url": "imgs/el.png"},
        {"name": "Zahra Yasmin Zafira ", "NIM": "2360296", "image_url": "imgs/zahra.png"}
    ]

    # Display Team Members
    col1, col2, col3, col4, col5 = st.columns(5)

    for i, member in enumerate(team_data):
        with locals()[f"col{i % 5 + 1}"]:
            st.image(member["image_url"], use_column_width='auto', output_format='png', caption=f"{member['name']} {member['NIM']}")


    st.header(" ", divider="gray")
    st.caption('<div style="text-align: center; transform: skewX(-20deg);">Powered by Politeknik AKA BOGOR</div>', unsafe_allow_html=True)


def main():
    st.sidebar.header("MENU")
    selected = st.sidebar.selectbox("Pilih menu:", ["📂 Home", "1️⃣ Informasi tentang Normalitas", "2️⃣ Kalkulator Perhitungan Normalitas", "3️⃣ Informasi tentang Kadar Larutan","4️⃣ Kalkulator Perhitungan Kadar %(b/v)", "5️⃣ Kalkulator Perhitungan Kadar %(b/b)", "👥 Our Team"])

    if selected == "📂 Home":
        show_Home()
    elif selected == "1️⃣ Informasi tentang Normalitas":
        show_InformasitentangNormalitas()
    elif selected == "2️⃣ Kalkulator Perhitungan Normalitas":
        calculated_KalkulatorPerhitunganNormalitas()
    elif selected == "3️⃣ Informasi tentang Kadar Larutan":
        show_Informasitentang_KadarLarutan()
    elif selected == "4️⃣ Kalkulator Perhitungan Kadar %(b/v)":  
        calculated_Kalkulator1PerhitunganKadar()   
    elif selected == "5️⃣ Kalkulator Perhitungan Kadar %(b/b)":
        calculated_Kalkulator2PerhitunganKadar()
    elif selected == "👥 Our Team":
        Our_Team()

if __name__ == '__main__':
    main()

def img_to_base64(image_path):
    """Convert image to base64"""
    with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    
    # Import gambar & konversi ke base64
img_path = "imgs/icon aka.png"  
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto;">',
    unsafe_allow_html=True,
)