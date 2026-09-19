import pandas as pd
import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Portal Kelas R7B", page_icon="📑", layout="wide")

# --- CSS CUSTOM BUAT TEMA CLASSIC COLLEGIATE ---
st.markdown(
    """
    <style>
    /* Background base dari warna Dark Navy */
    .stApp { background-color: #151B3D; color: #F5E6CC; }
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', 'Inter', sans-serif; }
    
    /* Judul Utama gradasi Deep Red ke Salmon ke Cream */
    .main-title { 
        background: linear-gradient(135deg, #B92B27 0%, #D68A82 50%, #F5E6CC 100%); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        font-weight: 800; font-size: 1.8rem; text-align: center; 
        margin-bottom: 0.5rem; padding-top: 1rem; 
    }
    
    /* --- CUSTOM UKURAN JUDUL SUB-HALAMAN YANG RESPONSIF --- */
    .section-title {
        font-size: 1.5rem !important; /* Ukuran pas untuk desktop & HP */
        font-weight: 700 !important;
        color: #F5E6CC !important;
        margin-bottom: 1rem !important;
    }
    
    .sub-title { 
        text-align: center; color: #D68A82; font-size: 1.05rem; 
        margin-bottom: 2.5rem; font-weight: 400; 
    }
    
    /* Kotak Card - Lighter Navy */
    .group-card { 
        background: linear-gradient(145deg, #1D2B64, #151B3D); 
        border: 1px solid #B92B27; padding: 1.5rem; border-radius: 16px; 
        margin-bottom: 1.5rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4); 
        transition: all 0.3s ease; 
    }
    .group-card:hover { 
        transform: translateY(-5px); border-color: #D68A82; 
        box-shadow: 0 20px 25px -5px rgba(214, 138, 130, 0.2); 
    }
    
    h3 { color: #D68A82 !important; font-weight: 600; font-size: 1.3rem; margin-bottom: 0.5rem; }
    
    /* Badge styling */
    .custom-badge { 
        display: inline-block; background: #151B3D; color: #D68A82; 
        padding: 4px 12px; border-radius: 6px; font-size: 0.85rem; 
        border: 1px solid #B92B27; font-family: monospace; font-weight: 600; 
    }
    
    /* Jadwal Harian */
    .schedule-day { 
        color: #B92B27; font-weight: 800; font-size: 1.3rem; 
        margin-top: 1.5rem; margin-bottom: 0.8rem; 
        border-bottom: 2px solid #B92B27; padding-bottom: 0.4rem; 
    }
    .schedule-card { 
        background: #1D2B64; border-left: 4px solid #B92B27; padding: 1.2rem; 
        border-radius: 8px 12px 12px 8px; margin-bottom: 1rem; 
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3); 
    }
    .schedule-time { color: #D68A82; font-weight: 700; font-size: 1rem; }
    .schedule-title { color: #F5E6CC; font-weight: 600; font-size: 1.05rem; margin-top: 0.2rem; }
    .schedule-dosen { color: #D68A82; font-size: 0.9rem; opacity: 0.9; }
    
    /* Selectbox Styling Override */
    div[data-baseweb="select"] > div {
        background-color: #1D2B64;
        border-color: #B92B27;
        color: #F5E6CC;
    }
    
    /* --- CUSTOM FONT LABEL SELECTBOX (Pilih Mata Kuliah) --- */
    div[data-testid="stSelectbox"] label p {
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        color: #D68A82 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Estetik
st.markdown(
    "<h1 class='main-title'>📚 Portal Kelas R7B</h1>", unsafe_allow_html=True
)
st.markdown(
    "<h6 class='sub-title'>Ruang informasi terpadu kelompok, tugas, dan jadwal"
    " kuliah Mahasigma R7B</h6>",
    unsafe_allow_html=True,
)

# Menu Navigasi Tab
tab1, tab2, tab3, tab4 = st.tabs(
    ["Info Kelompok", "Daftar Tugas", "Jadwal Kuliah", "Jadwal Lab"]
)

# --- TAB 1: INFO KELOMPOK ---
with tab1:
  st.markdown(
      "<p class='section-title'>✨ Daftar Kelompok Mata Kuliah</p>",
      unsafe_allow_html=True,
  )

  url_kelompok = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSgbDqQLSS7nEzsiKQgyOUmVPOdzJHLKrUCSCOcdf5paWbQmsPyB_agZQHiEhpyh8Vb-NlSLwUoDoGp/pub?output=csv"
  try:
    df_kel = pd.read_csv(url_kelompok, on_bad_lines="skip", dtype=str)
    kolom_mk = df_kel.columns[0]
    pilih_mk = st.selectbox(
        "Pilih Mata Kuliah:", df_kel[kolom_mk].unique(), key="mk_kelompok"
    )
    df_filtered_kel = df_kel[df_kel[kolom_mk] == pilih_mk]
    kolom_kelompok = df_kel.columns[1]

    st.markdown("<br>", unsafe_allow_html=True)

    for kel in df_filtered_kel[kolom_kelompok].unique():
      df_anggota = df_filtered_kel[df_filtered_kel[kolom_kelompok] == kel]

      card_html = (
          "<div class='group-card'>"
          f"<h3>📌 {kel}</h3>"
          "<hr style='border-color: #B92B27; margin: 0.5rem 0 1rem 0;'>"
          "<div style='display: flex; flex-direction: column; gap: 8px;'>"
      )

      for index, row in df_anggota.reset_index(drop=True).iterrows():
        npm = row.iloc[2]
        nama = row.iloc[3]
        card_html += (
            "<div style='display: flex; justify-content: space-between;"
            " align-items: center; padding-bottom: 8px; border-bottom: 1px"
            f" dashed #B92B27;'><span style='color: #F5E6CC; font-size:"
            f" 0.95rem;'><b>{index + 1}.</b> {nama}</span><span"
            f" class='custom-badge'>{npm}</span></div>"
        )

      card_html += "</div></div>"
      st.markdown(card_html, unsafe_allow_html=True)

  except Exception as e:
    st.error(f"Gagal memuat data kelompok: {e}")

# --- TAB 2: DAFTAR TUGAS ---
with tab2:
  st.markdown(
      "<p class='section-title'>📋 List Tugas & Deadline</p>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<p style='color: #D68A82; font-size: 0.85rem; margin-bottom:"
      " 1.5rem;'>Semua tugas terangkum di sini. Pantau terus deadline-nya dan"
      " jangan lupa dikerjain!!</p>",
      unsafe_allow_html=True,
  )

  url_tugas = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSgC5RjwOh9nMltAblQw8KVMeXx4U4GYua-pNZgNmRRjXDflowoykbz2ToCtCvROP4j2naXPahoW96v/pub?output=csv"
  try:
    df_tugas = pd.read_csv(url_tugas, on_bad_lines="skip", dtype=str).fillna(
        "-"
    )

    for index, row in df_tugas.iterrows():
      matkul = row.iloc[1]
      jenis = row.iloc[2]
      nama_tugas = row.iloc[3]
      pertemuan = row.iloc[4]
      tanggal = row.iloc[5]
      deadline = row.iloc[6]
      tempat = row.iloc[7]
      bentuk = row.iloc[8]

      jenis_bg = "#B92B27" if "kelompok" in str(jenis).lower() else "#151B3D"
      jenis_border = (
          "#D68A82" if "kelompok" in str(jenis).lower() else "#B92B27"
      )
      jenis_color = "#F5E6CC" if "kelompok" in str(jenis).lower() else "#D68A82"

      tugas_html = (
          "<div class='group-card' style='padding: 1.2rem 1.5rem;'>"
          "<div style='display: flex; justify-content: space-between;"
          " align-items: flex-start; margin-bottom: 10px;'><div><h3"
          " style='margin: 0; color: #F5E6CC !important; font-size:"
          f" 1.25rem;'>{nama_tugas}</h3><span style='color: #D68A82; font-weight:"
          f" 600; font-size: 0.95rem;'> Mata Kuliah :"
          f" {matkul}</span></div><div style='text-align: right;'><span"
          " class='custom-badge'"
          f" style='background: {jenis_bg}; color:"
          f" {jenis_color}; border-color: {jenis_border}; margin-bottom:"
          f" 5px;'>{jenis}</span><br><span class='custom-badge'"
          " style='background: #1D2B64; color: #D68A82; border-color:"
          f" #B92B27;'>📄 {bentuk}</span></div></div><hr"
          " style='border-color: #B92B27; margin: 0.8rem 0;'><div"
          " style='display: grid; grid-template-columns: 1fr 1fr; gap: 12px;"
          " font-size: 0.9rem; color: #D68A82;'><div><span style='color:"
          " #D68A82; font-size: 0.85rem;'>Pertemuan /"
          " Tanggal:</span><br><b style='color:"
          f" #F5E6CC;'>{pertemuan} — {tanggal}</b></div><div><span"
          " style='color: #D68A82; font-size: 0.85rem;'>Tempat"
          " Pengumpul:</span><br><b style='color:"
          f" #F5E6CC;'>{tempat}</b></div><div style='grid-column: span 2;"
          " background: rgba(185, 43, 39, 0.15); padding: 8px 12px;"
          " border-radius: 8px; border-left: 3px solid #B92B27;'><span"
          " style='color: #B92B27; font-size: 0.85rem; font-weight:"
          " 700;'>⏳ DEADLINE:</span><br><b style='color: #F5E6CC; font-size:"
          f" 1rem;'>{deadline}</b></div></div></div>"
      )
      st.markdown(tugas_html, unsafe_allow_html=True)

  except Exception as e:
    st.error(f"Gagal memuat data tugas: {e}")

# --- TAB 3: JADWAL KULIAH ---
with tab3:
  st.markdown(
      "<p class='section-title'>📅 Jadwal Kuliah Semester 7</p>",
      unsafe_allow_html=True,
  )

  st.markdown("<div class='schedule-day'>Senin</div>", unsafe_allow_html=True)
  senin_html = (
      "<div class='schedule-card'>"
      "<span class='schedule-time'>07:30 - 09:10</span> <span"
      " class='custom-badge' style='float: right;'>R.5.3-2</span>"
      "<div class='schedule-title'>Sistem Berbasis Pengetahuan (+)</div>"
      "<div class='schedule-dosen'>Dr. Alusyanti Primawati M.Kom.</div>"
      "<hr style='border-color: #B92B27; margin: 0.8rem 0;'>"
      "<span class='schedule-time'>09:10 - 10:50</span> <span"
      " class='custom-badge' style='float: right;'>R.5.3-2</span>"
      "<div class='schedule-title'>Keamanan Komputer</div>"
      "<div class='schedule-dosen'>Arif Pirman M.Kom.</div>"
      "</div>"
  )
  st.markdown(senin_html, unsafe_allow_html=True)

  st.markdown("<div class='schedule-day'>Selasa</div>", unsafe_allow_html=True)
  selasa_html = (
      "<div class='schedule-card'>"
      "<span class='schedule-time'>10:50 - 12:30</span> <span"
      " class='custom-badge' style='float: right;'>R.5.3-2</span>"
      "<div class='schedule-title'>E-Commerce (+) #)</div>"
      "<div class='schedule-dosen'>Rahmadanil M.Kom.</div>"
      "<hr style='border-color: #B92B27; margin: 0.8rem 0;'>"
      "<span class='schedule-time'>12:30 - 14:10</span> <span"
      " class='custom-badge' style='float: right;'>R.5.3-2</span>"
      "<div class='schedule-title'>Etika Profesi</div>"
      "<div class='schedule-dosen'>Annisa Elfina Augustia M.Kom.</div>"
      "</div>"
  )
  st.markdown(selasa_html, unsafe_allow_html=True)

  st.markdown("<div class='schedule-day'>Rabu</div>", unsafe_allow_html=True)
  rabu_html = (
      "<div class='schedule-card'>"
      "<span class='schedule-time'>07:30 - 09:40</span> <span"
      " class='custom-badge' style='float: right;'>R.5.3-2</span>"
      "<div class='schedule-title'>Filsafat Ilmu</div>"
      "<div class='schedule-dosen'>Drs. Surajiyo M.Si.</div>"
      "<hr style='border-color: #B92B27; margin: 0.8rem 0;'>"
      "<span class='schedule-time'>10:00 - 12:30</span> <span"
      " class='custom-badge' style='float: right;'>R.5.3-2</span>"
      "<div class='schedule-title'>Rekayasa Perangkat Lunak *) ##)</div>"
      "<div class='schedule-dosen'>Aminah M.Kom.</div>"
      "</div>"
  )
  st.markdown(rabu_html, unsafe_allow_html=True)

  st.markdown("<div class='schedule-day'>Kamis</div>", unsafe_allow_html=True)
  kamis_html = (
      "<div class='schedule-card'>"
      "<span class='schedule-time'>07:00 - 09:30</span> <span"
      " class='custom-badge' style='float: right;'>R.5.3-2</span>"
      "<div class='schedule-title'>Riset Operasional</div>"
      "<div class='schedule-dosen'>Agung Ferdinan Sandy S.T., M.K...</div>"
      "<hr style='border-color: #B92B27; margin: 0.8rem 0;'>"
      "<span class='schedule-time'>09:30 - 12:00</span> <span"
      " class='custom-badge' style='float: right;'>R.5.3-2</span>"
      "<div class='schedule-title'>Machine Learning *) #)</div>"
      "<div class='schedule-dosen'>Nurfidah Dwitiyanti M.Si.</div>"
      "</div>"
  )
  st.markdown(kamis_html, unsafe_allow_html=True)

# --- TAB 4: JADWAL LAB ---
with tab4:
  st.markdown(
      "<p class='section-title'>🧪 Jadwal Praktikum / Lab (LKMM1)</p>",
      unsafe_allow_html=True,
  )
  st.markdown("<br>", unsafe_allow_html=True)

  lab1_html = (
      "<div class='group-card'>"
      "<h3>1. E-Commerce (+)</h3>"
      "<span class='custom-badge' style='margin-bottom: 10px;'>Ruang:"
      " LKMM1</span>"
      "<div style='color: #F5E6CC; margin-top: 10px;'>"
      "<b>Waktu:</b> Selasa, 10.50 - 12.30<br>"
      "<b>Dosen:</b> Rahmadanil, M.Kom."
      "</div>"
      "<hr style='border-color: #B92B27; margin: 1rem 0;'>"
      "<div style='color: #D68A82; font-size: 0.9rem;'>"
      "<span style='color: #B92B27; font-weight: 600;'>Pra-UTS:</span> 15 Sept,"
      " 29 Sept, 13 Okt 2026<br>"
      "<span style='color: #B92B27; font-weight: 600;'>Pra-UAS:</span> 10 Nov,"
      " 24 Nov, 8 Des 2026"
      "</div>"
      "</div>"
  )
  st.markdown(lab1_html, unsafe_allow_html=True)

  lab2_html = (
      "<div class='group-card'>"
      "<h3>2. Machine Learning (*)</h3>"
      "<span class='custom-badge' style='margin-bottom: 10px;'>Ruang:"
      " LKMM1</span>"
      "<div style='color: #F5E6CC; margin-top: 10px;'>"
      "<b>Waktu:</b> Kamis, 09.30 - 12.00<br>"
      "<b>Dosen:</b> Nurfidah Dwitiyanti, M.Si."
      "</div>"
      "<hr style='border-color: #B92B27; margin: 1rem 0;'>"
      "<div style='color: #D68A82; font-size: 0.9rem;'>"
      "<span style='color: #B92B27; font-weight: 600;'>Pra-UTS:</span> 24 Sept,"
      " 8 Okt, 22 Okt 2026<br>"
      "<span style='color: #B92B27; font-weight: 600;'>Pra-UAS:</span> 19 Nov,"
      " 3 Des, 17 Des 2026"
      "</div>"
      "</div>"
  )
  st.markdown(lab2_html, unsafe_allow_html=True)