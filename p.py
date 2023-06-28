import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

#---SIDE-BAR---#
st.sidebar.image('ltmpt.jpg')
st.sidebar.image('33.png')
option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('	📒Home','🛠️EDA')
)
#menampilkan halaman utama
if option == '	📒Home' :
    # Menampilkan judul aplikasi
    st.title('Visualisasi Data Passing Grade UTBK Jurusan IPA Perguruan Tinggi Negeri Tahun 2019')
    st.markdown('kelompok tiga')
    #menampilkan tabel data
    st.write(df)
    #menampilkan penjelasan
    st.markdown('Passing grade adalah sebuah patokan nilai yang harus dicapai oleh peserta untuk bisa masuk ke perguruan tinggi negeri. Apabila peserta tidak bisa mencapai atau memenuhi presentase minimal nilai yang telah ditentukan, maka secara otomatis mereka gagal untuk lolos di kampus dan jurusan tersebut.')
    st.header('Filterisasi berdasarkan PTN')
    # Mengambil daftar unik PTN
    list_ptn = df['PTN'].unique()

    # Filter PTN menggunakan selectbox di sidebar
    selected_ptn = st.selectbox('Pilih PTN', list_ptn)

    # Melakukan filtrasi data berdasarkan PTN terpilih
    filterisasi_data = df[df['PTN'] == selected_ptn]

    # Menampilkan data yang telah difilter
    st.write(filterisasi_data)
    
elif option == '🛠️EDA':
    #membuat tabs
    slide1,slide2,slide3 = st.tabs(["📈 Explorasi Data","☕ Perbandingan ","🎧 Analisis"])

    ##TABS-1##
    with slide1:
        # Menampilkan judul aplikasi
        slide1.title('Data Passing Grade')
        #menampilkan dataframe
        slide1.write(df)

        # Menampilkan deskripsi dataset
        slide1.write('Deskripsi Dataset:')
        #menampilkan deskripsi kolom bagian yang dipilih
        kolom_deskripsi = ['RATAAN', 'S.BAKU','MIN','MAX']
        deskripsi = df[kolom_deskripsi].describe()
        slide1.write(deskripsi)

        # Menampilkan preview beberapa baris pertama dari dataset
        slide1.write('Preview Data:')
        slide1.write(df.head())

        # Menampilkan kolom-kolom yang ada di dataset
        slide1.write('Kolom-kolom yang ada di dataset:')
        slide1.write(df.columns)

        # Menampilkan statistik ringkasan untuk kolom-kolom numerik
        numeric_cols = ['RATAAN', 'S.BAKU','MIN','MAX']
        slide1.write('Statistik Ringkasan untuk Kolom Numerik:')
        slide1.write(df[numeric_cols].describe())

        # Menampilkan grafik histogram untuk kolom-kolom numerik
        slide1.write('Histogram untuk Kolom Numerik:')
        for col in numeric_cols:
            slide1.write(f'Grafik Histogram untuk Kolom {col}:')
            slide1.bar_chart(df[col])

    ##TABS-2##
    with slide2 :
        slide2.subheader('Visualisasi Umum' )
        frekuensi_ptn = df["PTN"].value_counts().reset_index()
        frekuensi_ptn.columns = ['PTN', 'Frekuensi']

        # Menampilkan bar chart menggunakan Plotly
        fig = px.bar(frekuensi_ptn, x='Frekuensi', y='PTN')
        st.plotly_chart(fig)

        # Menampilkan grafik hislide2ogram untuk kolom-kolom non numerik
        frekuensi_nama_prodi = df["NAMA PRODI"].value_counts().reset_index()
        frekuensi_nama_prodi.columns = ['NAMA PRODI', 'Frekuensi']

        # Menampilkan bar chart menggunakan Plotly
        fig = px.bar(frekuensi_nama_prodi, x='Frekuensi', y='NAMA PRODI')

        st.plotly_chart(fig)
        # Filter data untuk masing-masing PTN
        jatim_data_ub = df[df['PTN'].isin(['UNIVERSITAS BRAWIJAYA'])]
        jatim_data_unesa = df[df['PTN'].isin(['UNIVERSITAS NEGERI SURABAYA'])]
        jatim_data_unair = df[df['PTN'].isin(['UNIVERSITAS AIRLANGGA'])]
        jatim_data_its = df[df['PTN'].isin(['INSTITUT TEKNOLOGI SEPULUH NOPEMBER'])]
        jatim_data_upn = df[df['PTN'].isin(['UPN "VETERAN" JAWA TIMUR'])]
        jatim_data_unej = df[df['PTN'].isin(['UNIVERSITAS JEMBER'])]
        jatim_data_um = df[df['PTN'].isin(['UNIVERSITAS NEGERI MALANG'])]
        jatim_data_uinma = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI MALANG'])]
        
        jateng_data_undip = df[df['PTN'].isin(['UNIVERSITAS DIPONEGORO'])]
        jateng_data_uns = df[df['PTN'].isin(['UNIVERSITAS SEBELAS MARET'])]
        jateng_data_unsoed = df[df['PTN'].isin(['UNIVERSITAS JENDERAL SOEDIRMAN'])]
        jateng_data_unnes = df[df['PTN'].isin(['UNIVERSITAS NEGERI SEMARANG'])]
        jateng_data_tidar = df[df['PTN'].isin(['UNIVERSITAS TIDAR'])]

        jabar_data_itb = df[df['PTN'].isin(['INSTITUT TEKNOLOGI BANDUNG'])]
        jabar_data_unpad = df[df['PTN'].isin(['UNIVERSITAS PADJADJARAN'])]
        jabar_data_upi = df[df['PTN'].isin(['UNIVERSITAS PENDIDIKAN INDONESIA'])]
        jabar_data_uin_sgd = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI'])]

        yogya_data_ugm = df[df['PTN'].isin(['UNIVERSITAS GADJAH MADA'])]
        yogya_data_uny = df[df['PTN'].isin(['UNIVERSITAS NEGERI YOGYAKARTA'])]
        yogya_data_upn_yogya = df[df['PTN'].isin(['UPN "VETERAN" YOGYAKARTA'])]
        yogya_data_uinsuka = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA'])]

        jabodetabek_data_ui = df[df['PTN'].isin(['UNIVERSITAS INDONESIA'])]
        jabodetabek_data_uinjak = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI JAKARTA'])]
        jabodetabek_data_upn_jakarta = df[df['PTN'].isin(['UPN "VETERAN" JAKARTA'])]
        jabodetabek_data_ipb = df[df['PTN'].isin(['INSTITUT PERTANIAN BOGOR'])]
        jabodetabek_data_unj = df[df['PTN'].isin(['UNIVERSITAS NEGERI JAKARTA'])]

        bali_data_udayana = df[df['PTN'].isin(['UNIVERSITAS UDAYANA'])]
        bali_data_ganesha = df[df['PTN'].isin(['UNIVERSITAS PENDIDIKAN GANESHA'])]

        sumatra_data_sriwijaya = df[df['PTN'].isin(['UNIVERSITAS SRIWIJAYA'])]
        sumatra_data_sumatera_utara = df[df['PTN'].isin(['UNIVERSITAS SUMATERA UTARA'])]
        sumatra_data_andalas = df[df['PTN'].isin(['UNIVERSITAS ANDALAS'])]
        sumatra_data_bengkulu = df[df['PTN'].isin(['UNIVERSITAS BENGKULU'])]

        aceh_data_kuala = df[df['PTN'].isin(['UNIVERSITAS SYIAH KUALA'])]
        aceh_data_maliku = df[df['PTN'].isin(['UNIVERSITAS MALIKUSSALEH'])]
        aceh_data_palangkaraya = df[df['PTN'].isin(['UNIVERSITAS PALANGKARAYA'])]

        kalimantan_data_mulawarman = df[df['PTN'].isin(['UNIVERSITAS MULAWARMAN'])]
        kalimantan_data_lambung_mangkurat = df[df['PTN'].isin(['UNIVERSITAS LAMBUNG MANGKURAT'])]
        kalimantan_data_tanjungpura = df[df['PTN'].isin(['UNIVERSITAS TANJUNGPURA'])]

        sulawesi_data_unhas = df[df['PTN'].isin(['UNIVERSITAS HASANUDDIN'])]
        sulawesi_data_alaudin = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI ALAUDDIN'])]
        sulawesi_data_haluoleo = df[df['PTN'].isin(['UNIVERSITAS HALUOLEO'])]

        timur_data_mataram = df[df['PTN'].isin(['UNIVERSITAS MATARAM'])]
        timur_data_riau = df[df['PTN'].isin(['UNIVERSITAS RIAU'])]
        timur_data_jambi = df[df['PTN'].isin(['UNIVERSITAS JAMBI'])]
        timur_data_cendrawasih = df[df['PTN'].isin(['UNIVERSITAS CENDERAWASIH'])]
        timur_data_sam = df[df['PTN'].isin(['UNIVERSITAS SAM RATULANGI'])]
        timur_data_nusa = df[df['PTN'].isin(['UNIVERSITAS NUSA CENDANA'])]
        timur_data_patimura = df[df['PTN'].isin(['UNIVERSITAS PATTIMURA'])]
        timur_data_tadulako = df[df['PTN'].isin(['UNIVERSITAS TADULAKO'])]


        # Menghitung jumlah frekuensi hasil filter
        jatim_ub_freq = len(jatim_data_ub)
        jatim_unesa_freq = len(jatim_data_unesa)
        jatim_unair_freq = len(jatim_data_unair)
        jatim_its_freq = len(jatim_data_its)
        jatim_upn_freq = len(jatim_data_upn)
        jatim_unej_freq = len(jatim_data_unej)
        jatim_um_freq = len(jatim_data_um)
        jatim_uinma_freq = len(jatim_data_uinma)

        jateng_undip_freq = len(jateng_data_undip)
        jateng_uns_freq = len(jateng_data_uns)
        jateng_unsoed_freq = len(jateng_data_unsoed)
        jateng_unnes_freq = len(jateng_data_unnes)
        jateng_tidar_freq = len(jateng_data_tidar)

        jabar_itb_freq = len(jabar_data_itb)
        jabar_unpad_freq = len(jabar_data_unpad)
        jabar_upi_freq = len(jabar_data_upi)
        jabar_uin_sgd_freq = len(jabar_data_uin_sgd)

        yogya_ugm_freq = len(yogya_data_ugm)
        yogya_uny_freq = len(yogya_data_uny)
        yogya_upn_yogya_freq = len(yogya_data_upn_yogya)
        yogya_uinsuka_freq = len(yogya_data_uinsuka)

        jabodetabek_ui_freq = len(jabodetabek_data_ui)
        jabodetabek_uinjak_freq = len(jabodetabek_data_uinjak)
        jabodetabek_upn_jakarta_freq = len(jabodetabek_data_upn_jakarta)
        jabodetabek_ipb_freq = len(jabodetabek_data_ipb)
        jabodetabek_unj_freq = len(jabodetabek_data_unj)

        bali_ui_freq = len(bali_data_udayana)
        bali_ganesha_freq = len(bali_data_ganesha)

        total_sumatra_sriwijaya_freq = len(sumatra_data_sriwijaya)
        total_sumatra_sumatera_utara_freq = len(sumatra_data_sumatera_utara)
        total_sumatra_andalas_freq = len(sumatra_data_andalas)
        total_sumatra_bengkulu_freq = len(sumatra_data_bengkulu)

        aceh_kuala_freq = len(aceh_data_kuala)
        aceh_maliku_freq = len(aceh_data_maliku)
        aceh_palangkaraya_freq = len(aceh_data_palangkaraya)

        kalimantan_mulawarman_freq = len(kalimantan_data_mulawarman)
        kalimantan_lambung_mangkurat_freq = len(kalimantan_data_lambung_mangkurat)
        kalimantan_tanjungpura_freq = len(kalimantan_data_tanjungpura)

        sulawesi_unhas_freq = len(sulawesi_data_unhas)
        sulawesi_alaudin_freq = len(sulawesi_data_alaudin)
        sulawesi_haluoleo_freq = len(sulawesi_data_haluoleo)

        timur_mataram_freq = len(timur_data_mataram)
        timur_riau_freq = len(timur_data_riau)
        timur_jambi_freq = len(timur_data_jambi)
        timur_cendrawasih_freq = len(timur_data_cendrawasih)
        timur_sam_freq = len(timur_data_sam)
        timur_nusa_freq = len(timur_data_nusa)
        timur_patimura_freq = len(timur_data_patimura)
        timur_tadulako_freq = len(timur_data_tadulako)

        # Total frekuensi
        jatim_freq = jatim_ub_freq + jatim_unesa_freq + jatim_unair_freq + jatim_its_freq + jatim_upn_freq + jatim_unej_freq + jatim_um_freq + jatim_uinma_freq
        jateng_freq = jateng_undip_freq + jateng_uns_freq + jateng_unsoed_freq + jateng_unnes_freq + jateng_tidar_freq
        jabar_freq = jabar_itb_freq + jabar_unpad_freq + jabar_upi_freq + jabar_uin_sgd_freq
        yogya_freq = yogya_ugm_freq + yogya_uny_freq + yogya_upn_yogya_freq + yogya_uinsuka_freq
        jabodetabek_freq = jabodetabek_ui_freq + jabodetabek_uinjak_freq + jabodetabek_upn_jakarta_freq + jabodetabek_ipb_freq + jabodetabek_unj_freq
        bali_freq = bali_ui_freq + bali_ganesha_freq
        sumatra_freq = total_sumatra_sriwijaya_freq + total_sumatra_sumatera_utara_freq + total_sumatra_andalas_freq + total_sumatra_bengkulu_freq
        aceh_freq = aceh_kuala_freq + aceh_maliku_freq + aceh_palangkaraya_freq
        kalimantan_freq = kalimantan_mulawarman_freq + kalimantan_lambung_mangkurat_freq + kalimantan_tanjungpura_freq
        sulawesi_freq = sulawesi_unhas_freq + sulawesi_alaudin_freq + sulawesi_haluoleo_freq
        timur_freq = timur_mataram_freq + timur_riau_freq + timur_jambi_freq + timur_cendrawasih_freq + timur_sam_freq + timur_nusa_freq + timur_patimura_freq + timur_tadulako_freq

        # Variabel baru dengan isi jumlah frekuensi
        jatim = jatim_freq
        jateng = jateng_freq
        jabar = jabar_freq
        yogya = yogya_freq
        jabodetabek = jabodetabek_freq
        bali = bali_freq
        sumatra = sumatra_freq
        aceh = aceh_freq
        kalimantan = kalimantan_freq
        sulawesi = sulawesi_freq
        timur = timur_freq

        # Membuat DataFrame untuk bar chart
        data = pd.DataFrame({'Wilayah': ['Jawa Timur','Jawa Tengah','Jawa Barat','Yogyakarta','Jabodetabek','Bali','Sumatra','Aceh','Kalimantan','Sulawesi','Daerah Timur'],
                            'Frekuensi': [jatim, jateng, jabar, yogya, jabodetabek, bali, sumatra, aceh, kalimantan, sulawesi, timur]})

        # Membuat bar chart menggunakan Plotly Express
        fig = px.bar(data, x='Wilayah', y='Frekuensi', title='Jumlah Frekuensi disetiap Provinsi')
        fig.update_layout(xaxis_title='Wilayah', yaxis_title='Frekuensi')
        st.plotly_chart(fig)

        scatter_data = pd.DataFrame({'Wilayah': ['Jawa Timur', 'Jawa Tengah', 'Jawa Barat', 'Yogyakarta', 'Jabodetabek', 'Bali', 'Sumatra', 'Aceh', 'Kalimantan', 'Sulawesi', 'Daerah Timur'],
                            'Frekuensi': [jatim, jateng, jabar, yogya, jabodetabek, bali, sumatra, aceh, kalimantan, sulawesi, timur]})

        # Membuat scatter plot menggunakan Plotly Express
        fig_scatter = px.scatter(scatter_data, x='Wilayah', y='Frekuensi', title='Jumlah Frekuensi disetiap Provinsi')
        fig_scatter.update_layout(xaxis_title='Wilayah', yaxis_title='Frekuensi')
        st.plotly_chart(fig_scatter)

        # Create a radar plot using Plotly Graph Objects
        radar_fig = go.Figure(data=go.Scatterpolar(
            r=data['Frekuensi'],
            theta=data['Wilayah'],
            fill='toself'
        ))

        # Set the title and layout of the radar plot
        radar_fig.update_layout(
            title='Jumlah Frekuensi disetiap Provinsi',
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(data['Frekuensi'])]  # Adjust the range if needed
                )
            )
        )

        # Display the radar plot
        st.plotly_chart(radar_fig)

    ##TABS-3##
    with slide3 :
        options = ['Jawa Timur','Jawa Tengah','Jawa Barat','Yogyakarta','JABODETABEK','BALI','SUMATRA','ACEH','KALIMANTAN','SULAWESI','DAERAH TIMUR']
        selected_option = slide3.selectbox('Pilih opsi:', options)

        if selected_option == 'Jawa Timur':
                # Filter data untuk masing-masing PTN
                jatim_data_ub = df[df['PTN'].isin(['UNIVERSITAS BRAWIJAYA'])]
                jatim_data_unesa = df[df['PTN'].isin(['UNIVERSITAS NEGERI SURABAYA'])]
                jatim_data_unair = df[df['PTN'].isin(['UNIVERSITAS AIRLANGGA'])]
                jatim_data_its = df[df['PTN'].isin(['INSTITUT TEKNOLOGI SEPULUH NOPEMBER'])]
                jatim_data_upn = df[df['PTN'].isin(['UPN "VETERAN" JAWA TIMUR'])]
                jatim_data_unej = df[df['PTN'].isin(['UNIVERSITAS JEMBER'])]
                jatim_data_um = df[df['PTN'].isin(['UNIVERSITAS NEGERI MALANG'])]
                jatim_data_uinma = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI MALANG'])]

                    # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [jatim_data_ub['MAX'].mean(), jatim_data_unesa['MAX'].mean(), jatim_data_unair['MAX'].mean(),
                                jatim_data_its['MAX'].mean(), jatim_data_upn['MAX'].mean(), jatim_data_unej['MAX'].mean(),
                                jatim_data_um['MAX'].mean(), jatim_data_uinma['MAX'].mean()]

                min_per_ptn = [jatim_data_ub['MIN'].mean(), jatim_data_unesa['MIN'].mean(), jatim_data_unair['MIN'].mean(),
                                jatim_data_its['MIN'].mean(), jatim_data_upn['MIN'].mean(), jatim_data_unej['MIN'].mean(),
                                jatim_data_um['MIN'].mean(), jatim_data_uinma['MIN'].mean()]
                    
                rataan_per_ptn = [jatim_data_ub['RATAAN'].mean(), jatim_data_unesa['RATAAN'].mean(), jatim_data_unair['RATAAN'].mean(),
                                jatim_data_its['RATAAN'].mean(), jatim_data_upn['RATAAN'].mean(), jatim_data_unej['RATAAN'].mean(),
                                jatim_data_um['RATAAN'].mean(), jatim_data_uinma['RATAAN'].mean()]

                nama_ptn = ['UNIVERSITAS BRAWIJAYA', 'UNIVERSITAS NEGERI SURABAYA', 'UNIVERSITAS AIRLANGGA',
                                'INSTITUT TEKNOLOGI SEPULUH NOPEMBER', 'UPN "VETERAN" JAWA TIMUR',
                                'UNIVERSITAS NEGERI JEMBER', 'UNIVERSITAS NEGERI MALANG', 'UNIVERSITAS ISLAM NEGERI MALANG']

                    # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                    # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                    # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                    # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jumlah dta yang dipilih
                total_jatim_ub = len(jatim_data_ub)
                total_jatim_unesa = len(jatim_data_unesa)
                total_jatim_unair = len(jatim_data_unair)
                total_jatim_its = len(jatim_data_its)
                total_jatim_upn = len(jatim_data_upn)
                total_jatim_unej = len(jatim_data_unej)
                total_jatim_um = len(jatim_data_um)
                total_jatim_uinma = len(jatim_data_uinma)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS BRAWIJAYA': total_jatim_ub,
                    'UNIVERSITAS NEGERI SURABAYA': total_jatim_unesa,
                    'UNIVERSITAS AIRLANGGA': total_jatim_unair,
                    'INSTITUT TEKNOLOGI SEPULUH NOPEMBER': total_jatim_its,
                    'UPN "VETERAN" JAWA TIMUR': total_jatim_upn,
                    'UNIVERSITAS JEMBER': total_jatim_unej,
                    'UNIVERSITAS NEGERI MALANG': total_jatim_um,
                    'UNIVERSITAS ISLAM NEGERI MALANG': total_jatim_uinma
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)

                jt = slide3.radio(
                "Pilih PTN di Jawa Timur",
                ('PILIH PTN','UB', 'UNESA', 'UNAIR','ITS','UPN "VETERAN" JAWA TIMUR','UNEJ','UM','UINMA'))

                if jt == 'PILIH PTN':
                    slide3.write('PILIH PTN')

                if jt == 'UB':
                    slide3.write('UNIVERSITAS BRAWIJAYA')
                    # Memfilter baris yang mengandung "UB" di kolom "PTN"
                    filtered_data_ub = df[df['PTN'].str.contains('UNIVERSITAS BRAWIJAYA')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_ub)
                    
                    # Membuat subset data hanya untuk UNIVERSITAS BRAWIJAYA
                    ub_data = df[df['PTN'] == 'UNIVERSITAS BRAWIJAYA']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    nama_prodi = ub_data['NAMA PRODI']
                    rata_ub_nilai = ub_data['RATAAN']
                    minim_ub_nilai = ub_data['MIN']
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    data = pd.concat([nama_prodi, rata_ub_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(data, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    data = pd.concat([nama_prodi, minim_ub_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(data, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_ub = ub_data['RATAAN'].mean()
                    average2_ub = ub_data['S.BAKU'].mean()
                    average3_ub = ub_data['MIN'].mean()
                    average4_ub = ub_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_ub, average2_ub, average3_ub, average4_ub]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS BRAWIJAYA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jt == 'UNESA':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS NEGERI SURABAYA ')

                    # Memfilter baris yang mengandung "UNIVERSITAS NEGERI SURABAYA" di kolom "PTN"
                    filtered_data_unesa = df[df['PTN'].str.contains('UNIVERSITAS NEGERI SURABAYA')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_unesa)

                    # Membuat subset data hanya untuk UNIVERSITAS NEGERI SURABAYA
                    unesa_data = df[df['PTN'] == 'UNIVERSITAS NEGERI SURABAYA']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    unesa_prodi = unesa_data['NAMA PRODI']
                    rata_unesa_nilai = unesa_data['RATAAN']
                    minim_unesa_nilai = unesa_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unesa_data_gabung = pd.concat([unesa_prodi, rata_unesa_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(unesa_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unesa_data_gabung = pd.concat([unesa_prodi, minim_unesa_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(unesa_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unesa_data_gabung = pd.concat([unesa_prodi, rata_unesa_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(unesa_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_unesa = unesa_data['RATAAN'].mean()
                    average2_unesa = unesa_data['S.BAKU'].mean()
                    average3_unesa = unesa_data['MIN'].mean()
                    average4_unesa = unesa_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_unesa, average2_unesa,average3_unesa, average4_unesa]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS BRAWIJAYA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jt == 'UNAIR':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS AIRLANGGA ')

                    # Memfilter baris yang mengandung "UNIVERSITAS AIRLANGGA" di kolom "PTN"
                    filtered_data_unair = df[df['PTN'].str.contains('UNIVERSITAS AIRLANGGA')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_unair)

                    # Membuat subset data hanya untuk UNIVERSITAS AIRLANGGA
                    unair_data = df[df['PTN'] == 'UNIVERSITAS AIRLANGGA']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    unair_prodi = unair_data['NAMA PRODI']
                    rata_unair_nilai = unair_data['RATAAN']
                    minim_unair_nilai = unair_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unair_data_gabung = pd.concat([unair_prodi, rata_unair_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(unair_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unair_data_gabung = pd.concat([unair_prodi, minim_unair_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(unair_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unair_data_gabung = pd.concat([unair_prodi, rata_unair_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(unair_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_unair = unair_data['RATAAN'].mean()
                    average2_unair = unair_data['S.BAKU'].mean()
                    average3_unair = unair_data['MIN'].mean()
                    average4_unair = unair_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_unair = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_unair, average2_unair, average3_unair, average4_unair]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_unair, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS AIRLANGGA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jt == 'ITS':
                    #menampilkan tulisan
                    slide3.write("INSTITUT TEKNOLOGI SEPULUH NOPEMBER")
                    
                    # Memfilter baris yang mengandung "INSTITUT TEKNOLOGI SEPULUH NOPEMBER" di kolom "PTN"
                    filtered_data_its = df[df['PTN'].str.contains('INSTITUT TEKNOLOGI SEPULUH NOPEMBER')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_its)

                    # Membuat subset data hanya untuk INSTITUT TEKNOLOGI SEPULUH NOPEMBER
                    its_data = df[df['PTN'] == 'INSTITUT TEKNOLOGI SEPULUH NOPEMBER']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    its_prodi = its_data['NAMA PRODI']
                    rata_its_nilai = its_data['RATAAN']
                    minim_its_nilai = its_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    its_data_gabung = pd.concat([its_prodi, rata_its_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(its_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    its_data_gabung = pd.concat([its_prodi, minim_its_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(its_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_its = its_data['RATAAN'].mean()
                    average2_its = its_data['S.BAKU'].mean()
                    average3_its = its_data['MIN'].mean()
                    average4_its = its_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_its = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_its, average2_its, average3_its, average4_its]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_its, x='Metrik', y='Nilai', title='Metrik Statistik untuk INSTITUT TEKNOLOGI SEPULUH NOPEMBER')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)
                if jt == 'UPN "VETERAN" JAWA TIMUR':
                    #meampilkan tulisan
                    slide3.write('UPN "VETERAN" JAWA TIMUR') 
                    # Memfilter baris yang mengandung "UPN VETERAN JAWA TIMUR" di kolom "PTN"
                    filtered_data_upn = df[df['PTN'].str.contains('UPN "VETERAN" JAWA TIMUR')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_upn)

                    # Membuat subset data hanya untuk UPN "VETERAN" JAWA TIMUR
                    upn_data = df[df['PTN'] == 'UPN "VETERAN" JAWA TIMUR']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    upn_prodi = upn_data['NAMA PRODI']
                    rata_upn_nilai = upn_data['RATAAN']
                    minim_upn_nilai = upn_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upn_data_gabung = pd.concat([upn_prodi, rata_upn_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(upn_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upn_data_gabung = pd.concat([upn_prodi, minim_upn_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(upn_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upn_data_gabung = pd.concat([upn_prodi, rata_upn_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(upn_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_upn = upn_data['RATAAN'].mean()
                    average2_upn = upn_data['S.BAKU'].mean()
                    average3_upn = upn_data['MIN'].mean()
                    average4_upn = upn_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_upn = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_upn, average2_upn, average3_upn, average4_upn]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_upn, x='Metrik', y='Nilai', title='Metrik Statistik untuk UPN VETERAN JAWA TIMUR')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jt == 'UNEJ':
                    #menampilkan tulisan
                    slide3.write("UNIVERSITAS JEMBER")
                    # Memfilter baris yang mengandung "UNIVERSITAS JEMBER" di kolom "PTN"
                    filtered_data_unej = df[df['PTN'].str.contains('UNIVERSITAS JEMBER')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_unej)

                    # Membuat subset data hanya untuk UNIVERSITAS JEMBER
                    unej_data = df[df['PTN'] == 'UNIVERSITAS JEMBER']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    unej_prodi = unej_data['NAMA PRODI']
                    rata_unej_nilai = unej_data['RATAAN']
                    minim_unej_nilai = unej_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unej_data_gabung = pd.concat([unej_prodi, rata_unej_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(unej_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unej_data_gabung = pd.concat([unej_prodi, minim_unej_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(unej_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unej_data_gabung = pd.concat([unej_prodi, rata_unej_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(unej_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_unej = unej_data['RATAAN'].mean()
                    average2_unej = unej_data['S.BAKU'].mean()
                    average3_unej = unej_data['MIN'].mean()
                    average4_unej = unej_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_unej = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_unej, average2_unej, average3_unej, average4_unej]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_unej, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS JEMBER')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)
                
                if jt == 'UM':
                    #menampilkan tulisan
                    slide3.write("UNIVERSITAS NEGERI MALANG")
                    # Memfilter baris yang mengandung "UNIVERSITAS NEGERI MALANG" di kolom "PTN"
                    filtered_data_um = df[df['PTN'].str.contains('UNIVERSITAS NEGERI MALANG')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_um)

                    # Membuat subset data hanya untuk UNIVERSITAS NEGERI MALANG
                    um_data = df[df['PTN'] == 'UNIVERSITAS NEGERI MALANG']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    um_prodi = um_data['NAMA PRODI']
                    rata_um_nilai = um_data['RATAAN']
                    minim_um_nilai = um_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    um_data_gabung = pd.concat([um_prodi, rata_um_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(um_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    um_data_gabung = pd.concat([um_prodi, minim_um_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(um_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    um_data_gabung = pd.concat([um_prodi, rata_um_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(um_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_um = um_data['RATAAN'].mean()
                    average2_um = um_data['S.BAKU'].mean()
                    average3_um = um_data['MIN'].mean()
                    average4_um = um_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_um = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_um, average2_um, average3_um, average4_um]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_um, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS NEGERI MALANG')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)
                if jt == 'UINMA':
                    #menampilkan tulisan
                    slide3.write("UNIVERSITAS ISLAM NEGERI MALANG")
                    # Memfilter baris yang mengandung "UNIVERSITAS ISLAM NEGERI MALANG" di kolom "PTN"
                    filtered_data_unisma = df[df['PTN'].str.contains('UNIVERSITAS ISLAM NEGERI MALANG')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_unisma)

                    # Membuat subset data hanya untuk UNIVERSITAS ISLAM NEGERI MALANG
                    unisma_data = df[df['PTN'] == 'UNIVERSITAS ISLAM NEGERI MALANG']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    unisma_prodi = unisma_data['NAMA PRODI']
                    rata_unisma_nilai = unisma_data['RATAAN']
                    minim_unisma_nilai = unisma_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unisma_data_gabung = pd.concat([unisma_prodi, rata_unisma_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(unisma_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unisma_data_gabung = pd.concat([unisma_prodi, minim_unisma_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(unisma_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unisma_data_gabung = pd.concat([unisma_prodi, rata_unisma_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(unisma_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_unisma = unisma_data['RATAAN'].mean()
                    average2_unisma = unisma_data['S.BAKU'].mean()
                    average3_unisma = unisma_data['MIN'].mean()
                    average4_unisma = unisma_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_unisma = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_unisma, average2_unisma, average3_unisma, average4_unisma]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_unisma, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS ISLAM NEGERI MALANG')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)
            
        elif selected_option == 'Jawa Tengah':
                
                # Filter data untuk masing-masing PTN
                jateng_data_undip = df[df['PTN'].isin(['UNIVERSITAS DIPONEGORO'])]
                jateng_data_uns = df[df['PTN'].isin(['UNIVERSITAS SEBELAS MARET'])]
                jateng_data_unsoed = df[df['PTN'].isin(['UNIVERSITAS JENDERAL SOEDIRMAN'])]
                jateng_data_unnes = df[df['PTN'].isin(['UNIVERSITAS NEGERI SEMARANG'])]
                jateng_data_tidar = df[df['PTN'].isin(['UNIVERSITAS TIDAR'])]

                    # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [jateng_data_undip['MAX'].mean(), jateng_data_uns['MAX'].mean(), jateng_data_unsoed['MAX'].mean(),
                                jateng_data_unnes['MAX'].mean(), jateng_data_tidar['MAX'].mean()]

                min_per_ptn = [jateng_data_undip['MIN'].mean(), jateng_data_uns['MIN'].mean(), jateng_data_unsoed['MIN'].mean(),
                                jateng_data_unnes['MIN'].mean(), jateng_data_tidar['MIN'].mean()]
                    
                rataan_per_ptn = [jateng_data_undip['RATAAN'].mean(), jateng_data_uns['RATAAN'].mean(), jateng_data_unsoed['RATAAN'].mean(),
                                jateng_data_unnes['RATAAN'].mean(), jateng_data_tidar['RATAAN'].mean()]

                nama_ptn = ['UNIVERSITAS DIPONEGORO', 'UNIVERSITAS SEBELAS MARET', 'UNIVERSITAS JENDERAL SOEDIRMAN',
                            'UNIVERSITAS NEGERI SEMARANG', 'UNIVERSITAS TIDAR']

                    # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                    # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                    # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                    # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)

                # Calculate the total count per PTN
                total_jateng_undip = len(jateng_data_undip)
                total_jateng_uns = len(jateng_data_uns)
                total_jateng_unsoed = len(jateng_data_unsoed)
                total_jateng_unnes = len(jateng_data_unnes)
                total_jateng_tidar = len(jateng_data_tidar)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS DIPONEGORO': total_jateng_undip,
                    'UNIVERSITAS SEBELAS MARET': total_jateng_uns,
                    'UNIVERSITAS JENDERAL SOEDIRMAN': total_jateng_unsoed,
                    'UNIVERSITAS NEGERI SEMARANG': total_jateng_unnes,
                    'UNIVERSITAS TIDAR': total_jateng_tidar,
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)
                jteng = slide3.radio(
                "Pilih PTN di Jawa Tengah",
                ('PILIH PTN','UNDIP', 'UNS', 'UNSOED','UNNES','UNIVERSITAS TIDAR'))

                if jteng == 'pilih PTN':
                    slide3.write('PILIH PTN')


                if jteng == 'UNDIP':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS DIPONEGORO')
                    # Memfilter baris yang mengandung "UNIVERSITAS DIPONEGORO" di kolom "PTN"
                    filtered_data_undip = df[df['PTN'].str.contains('UNIVERSITAS DIPONEGORO')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_undip)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS DIPONEGORO
                    undip_data = df[df['PTN'] == 'UNIVERSITAS DIPONEGORO']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    nama_prodi = undip_data['NAMA PRODI']
                    rata_undip_nilai = undip_data['RATAAN']
                    minim_undip_nilai = undip_data['MIN']
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    data = pd.concat([nama_prodi, rata_undip_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(data, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    data = pd.concat([nama_prodi, minim_undip_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(data, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    data = pd.concat([nama_prodi, rata_undip_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(data, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_undip = undip_data['RATAAN'].mean()
                    average2_undip = undip_data['S.BAKU'].mean()
                    average3_undip = undip_data['MIN'].mean()
                    average4_undip = undip_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_undip, average2_undip, average3_undip, average4_undip]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS DIPONEGORO')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jteng == 'UNS':
                    #menampilkan tulisan
                    slide3.write("UNIVERSITAS SEBELAS MARET")
                    # Memfilter baris yang mengandung "UNIVERSITAS SEBELAS MARET" di kolom "PTN"
                    filtered_data_uns = df[df['PTN'].str.contains('UNIVERSITAS SEBELAS MARET')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_uns)

                    # Membuat subset data hanya untuk UNIVERSITAS SEBELAS MARET
                    uns_data = df[df['PTN'] == 'UNIVERSITAS SEBELAS MARET']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    uns_prodi = uns_data['NAMA PRODI']
                    rata_uns_nilai = uns_data['RATAAN']
                    minim_uns_nilai = uns_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uns_data_gabung = pd.concat([uns_prodi, rata_uns_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(uns_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uns_data_gabung = pd.concat([uns_prodi, minim_uns_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(uns_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uns_data_gabung = pd.concat([uns_prodi, rata_uns_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(uns_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimuns, dan nilai maksimuns untuk kolom-kolom tertentu
                    average1_uns = uns_data['RATAAN'].mean()
                    average2_uns = uns_data['S.BAKU'].mean()
                    average3_uns = uns_data['MIN'].mean()
                    average4_uns = uns_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_uns = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_uns, average2_uns, average3_uns, average4_uns]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_uns, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS SEBELAS MARET')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jteng == 'UNSOED':
                    #menampilkan tulisan
                    slide3.write("UNIVERSITAS JENDERAL SOEDIRMAN")
                    # Memfilter baris yang mengandung "UNIVERSITAS JENDERAL SOEDIRMAN" di kolom "PTN"
                    filtered_data_unsoed = df[df['PTN'].str.contains('UNIVERSITAS JENDERAL SOEDIRMAN')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_unsoed)

                    # Membuat subset data hanya untuk UNIVERSITAS JENDERAL SOEDIRMAN
                    unsoed_data = df[df['PTN'] == 'UNIVERSITAS JENDERAL SOEDIRMAN']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    unsoed_prodi = unsoed_data['NAMA PRODI']
                    rata_unsoed_nilai = unsoed_data['RATAAN']
                    minim_unsoed_nilai = unsoed_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unsoed_data_gabung = pd.concat([unsoed_prodi, rata_unsoed_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(unsoed_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unsoed_data_gabung = pd.concat([unsoed_prodi, minim_unsoed_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(unsoed_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unsoed_data_gabung = pd.concat([unsoed_prodi, rata_unsoed_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(unsoed_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimunsoed, dan nilai maksimunsoed untuk kolom-kolom tertentu
                    average1_unsoed = unsoed_data['RATAAN'].mean()
                    average2_unsoed = unsoed_data['S.BAKU'].mean()
                    average3_unsoed = unsoed_data['MIN'].mean()
                    average4_unsoed = unsoed_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_unsoed = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_unsoed, average2_unsoed, average3_unsoed, average4_unsoed]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_unsoed, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS JENDERAL SOEDIRMAN')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jteng == 'UNNES':
                    #menampilkan tulisan
                    slide3.write("UNIVERSITAS NEGERI SEMARANG")
                    # Memfilter baris yang mengandung "UNIVERSITAS NEGERI SEMARANG" di kolom "PTN"
                    filtered_data_unnes = df[df['PTN'].str.contains('UNIVERSITAS NEGERI SEMARANG')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_unnes)

                    # Membuat subset data hanya untuk UNIVERSITAS NEGERI SEMARANG
                    unnes_data = df[df['PTN'] == 'UNIVERSITAS NEGERI SEMARANG']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    unnes_prodi = unnes_data['NAMA PRODI']
                    rata_unnes_nilai = unnes_data['RATAAN']
                    minim_unnes_nilai = unnes_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unnes_data_gabung = pd.concat([unnes_prodi, rata_unnes_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(unnes_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unnes_data_gabung = pd.concat([unnes_prodi, minim_unnes_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(unnes_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unnes_data_gabung = pd.concat([unnes_prodi, rata_unnes_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(unnes_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_unnes = unnes_data['RATAAN'].mean()
                    average2_unnes = unnes_data['S.BAKU'].mean()
                    average3_unnes = unnes_data['MIN'].mean()
                    average4_unnes = unnes_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_unnes = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_unnes, average2_unnes, average3_unnes, average4_unnes]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_unnes, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS NEGERI SEMARANG')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jteng == 'UNIVERSITAS TIDAR':
                    #menampilkan tulisan
                    slide3.write("UNIVERSITAS TIDAR")
                    # Memfilter baris yang mengandung "UNIVERSITAS TIDAR" di kolom "PTN"
                    filtered_data_tidar = df[df['PTN'].str.contains('UNIVERSITAS TIDAR')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_tidar)

                    # Membuat subset data hanya untuk UNIVERSITAS TIDAR
                    tidar_data = df[df['PTN'] == 'UNIVERSITAS TIDAR']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    tidar_prodi = tidar_data['NAMA PRODI']
                    rata_tidar_nilai = tidar_data['RATAAN']
                    minim_tidar_nilai = tidar_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    tidar_data_gabung = pd.concat([tidar_prodi, rata_tidar_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(tidar_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    tidar_data_gabung = pd.concat([tidar_prodi, minim_tidar_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(tidar_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_tidar = tidar_data['RATAAN'].mean()
                    average2_tidar = tidar_data['S.BAKU'].mean()
                    average3_tidar = tidar_data['MIN'].mean()
                    average4_tidar = tidar_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data_tidar = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_tidar, average2_tidar, average3_tidar, average4_tidar]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data_tidar, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS TIDAR')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

        elif selected_option == 'Jawa Barat':
                
                # Filter data untuk masing-masing PTN
                jabar_data_itb = df[df['PTN'].isin(['INSTITUT TEKNOLOGI BANDUNG'])]
                jabar_data_unpad = df[df['PTN'].isin(['UNIVERSITAS PADJADJARAN'])]
                jabar_data_upi = df[df['PTN'].isin(['UNIVERSITAS PENDIDIKAN INDONESIA'])]
                jabar_data_uin_sgd = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI'])]

                    # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [jabar_data_itb['MAX'].mean(), jabar_data_unpad['MAX'].mean(), jabar_data_upi['MAX'].mean(),
                                jabar_data_uin_sgd['MAX'].mean()]

                min_per_ptn = [jabar_data_itb['MIN'].mean(), jabar_data_unpad['MIN'].mean(), jabar_data_upi['MIN'].mean(),
                                jabar_data_uin_sgd['MIN'].mean()]
                    
                rataan_per_ptn = [jabar_data_itb['RATAAN'].mean(), jabar_data_unpad['RATAAN'].mean(), jabar_data_upi['RATAAN'].mean(),
                                jabar_data_uin_sgd['RATAAN'].mean()]

                nama_ptn = ['INSTITUT TEKNOLOGI BANDUNG', 'UNIVERSITAS PADJADJARAN', 'UNIVERSITAS PENDIDIKAN INDONESIA',
                            'UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI', 'UNIVERSITAS TIDAR']

                    # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                    # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                    # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                    # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)

                # Calculate the total count per PTN
                total_jabar_itb = len(jabar_data_itb)
                total_jabar_unpad = len(jabar_data_unpad)
                total_jabar_upi = len(jabar_data_upi)
                total_jabar_uin_sgd = len(jabar_data_uin_sgd)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'INSTITUT TEKNOLOGI BANDUNG': total_jabar_itb,
                    'UNIVERSITAS PADJADJARAN': total_jabar_unpad,
                    'UNIVERSITAS PENDIDIKAN INDONESIA': total_jabar_upi,
                    'UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI': total_jabar_uin_sgd,
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
                # Display the chart using Streamlit
                st.plotly_chart(fig)
                
                jbar = slide3.radio(
                "Pilih PTN di Jawa Barat",
                ('PILIH PTN','ITB','UNPAD','UPI','UIN SGD',))
                if jbar == 'PILIH PTN':
                    slide3.write('PILIH PTN')

                if jbar == 'ITB':
                    #menampilkan tulisan
                    slide3.write('INSTITUT TEKNOLOGI BANDUNG')
                    # Memfilter baris yang mengandung "INSTITUT TEKNOLOGI BANDUNG" di kolom "PTN"
                    filtered_data_itb = df[df['PTN'].str.contains('INSTITUT TEKNOLOGI BANDUNG')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_itb)
                    
                    # Membuat supset data hanya untuk INSTITUT TEKNOLOGI BANDUNG
                    itb_data = df[df['PTN'] == 'INSTITUT TEKNOLOGI BANDUNG']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    itb_prodi = itb_data['NAMA PRODI']
                    rata_itb_nilai = itb_data['RATAAN']
                    minim_itb_nilai = itb_data['MIN']
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    itb_data_gabung = pd.concat([itb_prodi, rata_itb_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(itb_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    itb_data_gabung = pd.concat([itb_prodi, minim_itb_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(itb_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    itb_data_gabung = pd.concat([itb_prodi, rata_itb_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(itb_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_itb = itb_data['RATAAN'].mean()
                    average2_itb = itb_data['S.BAKU'].mean()
                    average3_itb = itb_data['MIN'].mean()
                    average4_itb = itb_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_itb, average2_itb, average3_itb, average4_itb]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk INSTITUT TEKNOLOGI BANDUNG')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jbar == 'UNPAD':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS PADJADJARAN')
                    # Memfilter baris yang mengandung "UNIVERSITAS PADJADJARAN" di kolom "PTN"
                    filtered_data_unpad = df[df['PTN'].str.contains('UNIVERSITAS PADJADJARAN')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_unpad)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS PADJADJARAN
                    unpad_data = df[df['PTN'] == 'UNIVERSITAS PADJADJARAN']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    unpad_prodi = unpad_data['NAMA PRODI']
                    rata_unpad_nilai = unpad_data['RATAAN']
                    minim_unpad_nilai = unpad_data['MIN']
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unpad_data_gabung = pd.concat([unpad_prodi, rata_unpad_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(unpad_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unpad_data_gabung = pd.concat([unpad_prodi, minim_unpad_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(unpad_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unpad_data_gabung = pd.concat([unpad_prodi, rata_unpad_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(unpad_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_unpad = unpad_data['RATAAN'].mean()
                    average2_unpad = unpad_data['S.BAKU'].mean()
                    average3_unpad = unpad_data['MIN'].mean()
                    average4_unpad = unpad_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_unpad, average2_unpad, average3_unpad, average4_unpad]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS PADJADJARAN')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jbar == 'UPI':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS PENDIDIKAN INDONESIA')
                    # Memfilter baris yang mengandung "UNIVERSITAS PENDIDIKAN INDONESIA" di kolom "PTN"
                    filtered_data_upi = df[df['PTN'].str.contains('UNIVERSITAS PENDIDIKAN INDONESIA')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_upi)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS PENDIDIKAN INDONESIA
                    upi_data = df[df['PTN'] == 'UNIVERSITAS PENDIDIKAN INDONESIA']

                    # Mengambil kolom "NAMA PRODI" dari DataFrame yang telah difilter
                    upi_prodi = upi_data['NAMA PRODI']
                    rata_upi_nilai = upi_data['RATAAN']
                    minim_upi_nilai = upi_data['MIN']
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upi_data_gabung = pd.concat([upi_prodi, rata_upi_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(upi_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upi_data_gabung = pd.concat([upi_prodi, minim_upi_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(upi_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upi_data_gabung = pd.concat([upi_prodi, rata_upi_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(upi_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_upi = upi_data['RATAAN'].mean()
                    average2_upi = upi_data['S.BAKU'].mean()
                    average3_upi = upi_data['MIN'].mean()
                    average4_upi = upi_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_upi, average2_upi, average3_upi, average4_upi]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS PENDIDIKAN INDONESIA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jbar == 'UIN SGD':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI')
                    # Memfilter baris yang mengandung "UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI" di kolom "PTN"
                    filtered_data_uins_sgd = df[df['PTN'].str.contains('UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_uins_sgd)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI
                    uins_sgd_data = df[df['PTN'] == 'UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI']

                    uin_sgd_prodi = uins_sgd_data['NAMA PRODI']
                    rata_uins_sgd_nilai = uins_sgd_data['RATAAN']
                    minim_uins_sgd_nilai = uins_sgd_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uins_sgd_data_gabung = pd.concat([uin_sgd_prodi, rata_uins_sgd_nilai, minim_uins_sgd_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_uin_sgd = uins_sgd_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_uin_sgd)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(uins_sgd_data_gabung, x='MIN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uins_sgd_data_gabung = pd.concat([uin_sgd_prodi, rata_uins_sgd_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(uins_sgd_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uins_sgd_data_gabung = pd.concat([uin_sgd_prodi, minim_uins_sgd_nilai], axis=1)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_uins_sgd = uins_sgd_data['RATAAN'].mean()
                    average2_uins_sgd = uins_sgd_data['S.BAKU'].mean()
                    average3_uins_sgd = uins_sgd_data['MIN'].mean()
                    average4_uins_sgd = uins_sgd_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_uins_sgd, average2_uins_sgd, average3_uins_sgd, average4_uins_sgd]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

        elif selected_option == 'Yogyakarta':
                yogya_data_ugm = df[df['PTN'].isin(['UNIVERSITAS GADJAH MADA'])]
                yogya_data_uny = df[df['PTN'].isin(['UNIVERSITAS NEGERI YOGYAKARTA'])]
                yogya_data_upn_yogya = df[df['PTN'].isin(['UPN "VETERAN" YOGYAKARTA'])]
                yogya_data_uinsuka = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA'])]

                    # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [yogya_data_ugm['MAX'].mean(), yogya_data_uny['MAX'].mean(), yogya_data_upn_yogya['MAX'].mean(),
                                yogya_data_uinsuka['MAX'].mean()]

                min_per_ptn = [yogya_data_ugm['MIN'].mean(), yogya_data_uny['MIN'].mean(), yogya_data_upn_yogya['MIN'].mean(),
                                yogya_data_uinsuka['MIN'].mean()]
                    
                rataan_per_ptn = [yogya_data_ugm['RATAAN'].mean(), yogya_data_uny['RATAAN'].mean(), yogya_data_upn_yogya['RATAAN'].mean(),
                                yogya_data_uinsuka['RATAAN'].mean()]

                nama_ptn = ['UNIVERSITAS GADJAH MADA', 'UNIVERSITAS NEGERI YOGYAKARTA', 'UPN "VETERAN" YOGYAKARTA',
                                'UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA']

                    # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                    # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                    # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                    # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jumlah dta yang dipilih
                total_yogya_ugm = len(yogya_data_ugm)
                total_yogya_uny = len(yogya_data_uny)
                total_yogya_upn_yogya = len(yogya_data_upn_yogya)
                total_yogya_uinsuka = len(yogya_data_uinsuka)


                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS GADJAH MADA': total_yogya_ugm,
                    'UNIVERSITAS NEGERI YOGYAKARTA': total_yogya_uny,
                    'UPN "VETERAN" YOGYAKARTA': total_yogya_upn_yogya,
                    'UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA': total_yogya_uinsuka,
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)
                
                jjogja = slide3.radio(
                "Pilih PTN di YOGYAKARTA",
                ('PILIH PTN','UGM','UNY','UPN "VETERAN" YOGYAKARTA','UINSUKA',))

                if jjogja == 'PILIH PTN':
                    slide3.write('PILIH PTN')

                if jjogja == 'UGM':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS GADJAH MADA')
                    # Memfilter baris yang mengandung "UNIVERSITAS GADJAH MADA" di kolom "PTN"
                    filtered_data_ugm = df[df['PTN'].str.contains('UNIVERSITAS GADJAH MADA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_ugm)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS GADJAH MADA
                    ugm_data = df[df['PTN'] == 'UNIVERSITAS GADJAH MADA']
                    
                    ugm_prodi = ugm_data['NAMA PRODI']
                    rata_ugm_nilai = ugm_data['RATAAN']
                    minim_ugm_nilai = ugm_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ugm_data_gabung = pd.concat([ugm_prodi, rata_ugm_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(ugm_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ugm_data_gabung = pd.concat([ugm_prodi, minim_ugm_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(ugm_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_ugm =ugm_data['RATAAN'].mean()
                    average2_ugm =ugm_data['S.BAKU'].mean()
                    average3_ugm =ugm_data['MIN'].mean()
                    average4_ugm =ugm_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_ugm, average2_ugm, average3_ugm, average4_ugm]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS GADJAH MADA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jjogja == 'UNY':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS NEGERI YOGYAKARTA')
                    # Memfilter baris yang mengandung "UNIVERSITAS NEGERI YOGYAKARTA" di kolom "PTN"
                    filtered_data_uny = df[df['PTN'].str.contains('UNIVERSITAS NEGERI YOGYAKARTA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_uny)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS NEGERI YOGYAKARTA
                    uny_data = df[df['PTN'] == 'UNIVERSITAS NEGERI YOGYAKARTA']
                    
                    uny_prodi = uny_data['NAMA PRODI']
                    rata_uny_nilai = uny_data['RATAAN']
                    minim_uny_nilai = uny_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uny_data_gabung = pd.concat([uny_prodi, rata_uny_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(uny_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uny_data_gabung = pd.concat([uny_prodi, minim_uny_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(uny_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uny_data_gabung = pd.concat([uny_prodi, rata_uny_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(uny_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_uny =uny_data['RATAAN'].mean()
                    average2_uny =uny_data['S.BAKU'].mean()
                    average3_uny =uny_data['MIN'].mean()
                    average4_uny =uny_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_uny, average2_uny, average3_uny, average4_uny]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS NEGERI YOGYAKARTA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jjogja == 'UPN "VETERAN" YOGYAKARTA':
                    #menampilkan tulisan
                    slide3.write('UPN "VETERAN" YOGYAKARTA')
                    # Memfilter baris yang mengandung " UPN "VETERAN" YOGYAKARTA" di kolom "PTN"
                    filtered_data_upn_jogja = df[df['PTN'].str.contains('UPN "VETERAN" YOGYAKARTA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_upn_jogja)
                    
                    # Membuat supset data hanya untuk  UPN "VETERAN" YOGYAKARTA
                    upn_jogja_data = df[df['PTN'] == 'UPN "VETERAN" YOGYAKARTA']
                    
                    upn_jogja_prodi = upn_jogja_data['NAMA PRODI']
                    rata_upn_jogja_nilai = upn_jogja_data['RATAAN']
                    minim_upn_jogja_nilai = upn_jogja_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upn_jogja_data_gabung = pd.concat([upn_jogja_prodi, rata_upn_jogja_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(upn_jogja_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upn_jogja_data_gabung = pd.concat([upn_jogja_prodi, minim_upn_jogja_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(upn_jogja_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upn_jogja_data_gabung = pd.concat([upn_jogja_prodi, rata_upn_jogja_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(upn_jogja_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_upn_jogja =upn_jogja_data['RATAAN'].mean()
                    average2_upn_jogja =upn_jogja_data['S.BAKU'].mean()
                    average3_upn_jogja =upn_jogja_data['MIN'].mean()
                    average4_upn_jogja =upn_jogja_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_upn_jogja, average2_upn_jogja, average3_upn_jogja, average4_upn_jogja]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UPN "VETERAN" YOGYAKARTA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jjogja == 'UINSUKA':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA')
                    # Memfilter baris yang mengandung " UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA" di kolom "PTN"
                    filtered_data_uinsuka = df[df['PTN'].str.contains('UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_uinsuka)
                    
                    # Membuat supset data hanya untuk  UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA
                    uinsuka_data = df[df['PTN'] == 'UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA']
                    
                    uinsuka_prodi = uinsuka_data['NAMA PRODI']
                    rata_uinsuka_nilai = uinsuka_data['RATAAN']
                    minim_uinsuka_nilai = uinsuka_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uinsuka_data_gabung = pd.concat([uinsuka_prodi, rata_uinsuka_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(uinsuka_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uinsuka_data_gabung = pd.concat([uinsuka_prodi, minim_uinsuka_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(uinsuka_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uinsuka_data_gabung = pd.concat([uinsuka_prodi, rata_uinsuka_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(uinsuka_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_uinsuka =uinsuka_data['RATAAN'].mean()
                    average2_uinsuka =uinsuka_data['S.BAKU'].mean()
                    average3_uinsuka =uinsuka_data['MIN'].mean()
                    average4_uinsuka =uinsuka_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_uinsuka, average2_uinsuka, average3_uinsuka, average4_uinsuka]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS ISLAM NEGERI SUNAN KALIJAGA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

        elif selected_option == 'JABODETABEK':
                # Filter data untuk masing-masing PTN
                jabodetabek_data_ui = df[df['PTN'].isin(['UNIVERSITAS INDONESIA'])]
                jabodetabek_data_uinjak = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI JAKARTA'])]
                jabodetabek_data_upn_jakarta = df[df['PTN'].isin(['UPN "VETERAN" JAKARTA'])]
                jabodetabek_data_ipb = df[df['PTN'].isin(['INSTITUT PERTANIAN BOGOR'])]
                jabodetabek_data_unj = df[df['PTN'].isin(['UNIVERSITAS NEGERI JAKARTA'])]

                    # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [jabodetabek_data_ui['MAX'].mean(), jabodetabek_data_uinjak['MAX'].mean(), jabodetabek_data_upn_jakarta['MAX'].mean(),
                                jabodetabek_data_ipb['MAX'].mean(), jabodetabek_data_upn_jakarta['MAX'].mean(), jabodetabek_data_unj['MAX'].mean(),
                                ]

                min_per_ptn = [jabodetabek_data_ui['MIN'].mean(), jabodetabek_data_uinjak['MIN'].mean(), jabodetabek_data_upn_jakarta['MIN'].mean(),
                                jabodetabek_data_ipb['MIN'].mean(), jabodetabek_data_upn_jakarta['MIN'].mean(), jabodetabek_data_unj['MIN'].mean(),
                                ]
                    
                rataan_per_ptn = [jabodetabek_data_ui['RATAAN'].mean(), jabodetabek_data_uinjak['RATAAN'].mean(), jabodetabek_data_upn_jakarta['RATAAN'].mean(),
                                jabodetabek_data_ipb['RATAAN'].mean(), jabodetabek_data_upn_jakarta['RATAAN'].mean(), jabodetabek_data_unj['RATAAN'].mean(),
                                ]

                nama_ptn = ['UNIVERSITAS INDONESIA', 'UNIVERSITAS ISLAM NEGERI JAKARTA', 'UPN "VETERAN" JAKARTA',
                            'INSTITUT PERTANIAN BOGOR', 'UPN "VETERAN" JAWA TIMUR',
                            'UNIVERSITAS NEGERI JAKARTA']

                    # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                    # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                    # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                    # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jumlah dta yang dipilih
                total_jabodetabek_ui = len(jabodetabek_data_ui)
                total_jabodetabek_uinjak = len(jabodetabek_data_uinjak)
                total_jabodetabek_upn_jakarta = len(jabodetabek_data_upn_jakarta)
                total_jabodetabek_ipb = len(jabodetabek_data_ipb)
                total_jabodetabek_unj = len(jabodetabek_data_unj)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS INDONESIA': total_jabodetabek_ui,
                    'UNIVERSITAS ISLAM NEGERI JAKARTA': total_jabodetabek_uinjak,
                    'UPN "VETERAN" JAKARTA': total_jabodetabek_upn_jakarta,
                    'INSTITUT PERTANIAN BOGOR': total_jabodetabek_ipb,
                    'UNIVERSITAS NEGERI JAKARTA': total_jabodetabek_unj,
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)


                jjabokdetabek = slide3.radio(
                "Pilih PTN di JABODETABEK",
                ('PILIH PTN','UI','UINJAK','UPN "VETERAN" JAKARTA','IPB','UNJ',))
                if jjabokdetabek == 'PILIH PTN':
                    slide3.write("PILIH PTN")

                if jjabokdetabek == 'UI':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS INDONESIA')
                    # Memfilter baris yang mengandung " UNIVERSITAS INDONESIA" di kolom "PTN"
                    filtered_data_ui = df[df['PTN'].str.contains('UNIVERSITAS INDONESIA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_ui)
                    
                    # Membuat supset data hanya untuk  UNIVERSITAS INDONESIA
                    ui_data = df[df['PTN'] == 'UNIVERSITAS INDONESIA']
                    
                    ui_prodi = ui_data['NAMA PRODI']
                    rata_ui_nilai = ui_data['RATAAN']
                    minim_ui_nilai = ui_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ui_data_gabung = pd.concat([ui_prodi, rata_ui_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(ui_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ui_data_gabung = pd.concat([ui_prodi, minim_ui_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(ui_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_ui =ui_data['RATAAN'].mean()
                    average2_ui =ui_data['S.BAKU'].mean()
                    average3_ui =ui_data['MIN'].mean()
                    average4_ui =ui_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_ui, average2_ui, average3_ui, average4_ui]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS INDONESIA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jjabokdetabek == 'UINJAK':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS ISLAM NEGERI JAKARTA')
                    # Memfilter baris yang mengandung "UNIVERSITAS ISLAM NEGERI JAKARTA" di kolom "PTN"
                    filtered_data_uinjak = df[df['PTN'].str.contains('UNIVERSITAS ISLAM NEGERI JAKARTA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_uinjak)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS ISLAM NEGERI JAKARTA
                    uinjak_data = df[df['PTN'] == 'UNIVERSITAS ISLAM NEGERI JAKARTA']
                    
                    uinjak_prodi = uinjak_data['NAMA PRODI']
                    rata_uinjak_nilai = uinjak_data['RATAAN']
                    minim_uinjak_nilai = uinjak_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uinjak_data_gabung = pd.concat([uinjak_prodi, rata_uinjak_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(uinjak_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    uinjak_data_gabung = pd.concat([uinjak_prodi, minim_uinjak_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(uinjak_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_uinjak =uinjak_data['RATAAN'].mean()
                    average2_uinjak =uinjak_data['S.BAKU'].mean()
                    average3_uinjak =uinjak_data['MIN'].mean()
                    average4_uinjak =uinjak_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_uinjak, average2_uinjak, average3_uinjak, average4_uinjak]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS ISLAM NEGERI JAKARTA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jjabokdetabek == 'UPN "VETERAN" JAKARTA':
                    #menampilkan tulisan
                    slide3.write('UPN "VETERAN" JAKARTA')
                    # Memfilter baris yang mengandung "UPN "VETERAN" JAKARTA" di kolom "PTN"
                    filtered_data_upn_jakarta = df[df['PTN'].str.contains('UPN "VETERAN" JAKARTA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_upn_jakarta)
                    
                    # Membuat supset data hanya untuk UPN "VETERAN" JAKARTA
                    upn_jakarta_data = df[df['PTN'] == 'UPN "VETERAN" JAKARTA']
                    
                    upn_jakarta_prodi = upn_jakarta_data['NAMA PRODI']
                    rata_upn_jakarta_nilai = upn_jakarta_data['RATAAN']
                    minim_upn_jakarta_nilai = upn_jakarta_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upn_jakarta_data_gabung = pd.concat([upn_jakarta_prodi, rata_upn_jakarta_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(upn_jakarta_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    upn_jakarta_data_gabung = pd.concat([upn_jakarta_prodi, minim_upn_jakarta_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(upn_jakarta_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_upn_jakarta =upn_jakarta_data['RATAAN'].mean()
                    average2_upn_jakarta =upn_jakarta_data['S.BAKU'].mean()
                    average3_upn_jakarta =upn_jakarta_data['MIN'].mean()
                    average4_upn_jakarta =upn_jakarta_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_upn_jakarta, average2_upn_jakarta, average3_upn_jakarta, average4_upn_jakarta]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UPN "VETERAN" JAKARTA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jjabokdetabek == 'IPB':
                    #menampilkan tulisan
                    slide3.write('INSTITUT PERTANIAN BOGOR')
                    # Memfilter baris yang mengandung "INSTITUT PERTANIAN BOGOR" di kolom "PTN"
                    filtered_data_ipb = df[df['PTN'].str.contains('INSTITUT PERTANIAN BOGOR')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_ipb)
                    
                    # Membuat supset data hanya untuk INSTITUT PERTANIAN BOGOR
                    ipb_data = df[df['PTN'] == 'INSTITUT PERTANIAN BOGOR']
                    
                    ipb_prodi = ipb_data['NAMA PRODI']
                    rata_ipb_nilai = ipb_data['RATAAN']
                    minim_ipb_nilai = ipb_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ipb_data_gabung = pd.concat([ipb_prodi, rata_ipb_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(ipb_data_gabung, x='RATAAN', y='NAMA PRODI', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ipb_data_gabung = pd.concat([ipb_prodi, minim_ipb_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(ipb_data_gabung, x='MIN', y='NAMA PRODI', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)
                    

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_ipb =ipb_data['RATAAN'].mean()
                    average2_ipb =ipb_data['S.BAKU'].mean()
                    average3_ipb =ipb_data['MIN'].mean()
                    average4_ipb =ipb_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_ipb, average2_ipb, average3_ipb, average4_ipb]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  INSTITUT PERTANIAN BOGOR')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jjabokdetabek == 'UNJ':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS NEGERI JAKARTA')
                    # Memfilter baris yang mengandung "UNIVERSITAS NEGERI JAKARTA" di kolom "PTN"
                    filtered_data_unj = df[df['PTN'].str.contains('UNIVERSITAS NEGERI JAKARTA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_unj)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS NEGERI JAKARTA
                    unj_data = df[df['PTN'] == 'UNIVERSITAS NEGERI JAKARTA']
                    
                    unj_prodi = unj_data['NAMA PRODI']
                    rata_unj_nilai = unj_data['RATAAN']
                    minim_unj_nilai = unj_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unj_data_gabung = pd.concat([unj_prodi, rata_unj_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(unj_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    unj_data_gabung = pd.concat([unj_prodi, minim_unj_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(unj_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_unj =unj_data['RATAAN'].mean()
                    average2_unj =unj_data['S.BAKU'].mean()
                    average3_unj =unj_data['MIN'].mean()
                    average4_unj =unj_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_unj, average2_unj, average3_unj, average4_unj]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS NEGERI JAKARTA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

        elif selected_option == 'BALI':
                # Filter data untuk masing-masing PTN
                bali_data_udayana = df[df['PTN'].isin(['UNIVERSITAS UDAYANA'])]
                bali_data_ganesha = df[df['PTN'].isin(['UNIVERSITAS PENDIDIKAN GANESHA'])]

                    # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [bali_data_udayana['MAX'].mean(), bali_data_ganesha['MAX'].mean()]

                min_per_ptn = [bali_data_udayana['MIN'].mean(), bali_data_ganesha['MIN'].mean()]
                rataan_per_ptn = [bali_data_udayana['RATAAN'].mean(), bali_data_ganesha['RATAAN'].mean()]
                nama_ptn = ['UNIVERSITAS UDAYANA', 'UNIVERSITAS PENDIDIKAN GANESHA']

                    # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                    # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                    # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                    # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jumlah dta yang dipilih
                total_bali_ui = len(bali_data_udayana)
                total_bali_ganesha = len(bali_data_ganesha)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS UDAYANA': total_bali_ui,
                    'UNIVERSITAS PENDIDIKAN GANESHA': total_bali_ganesha,
                }
                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)
                
                jbali = slide3.radio(
                "Pilih PTN di BALI",
                ('PILIH PTN','UDAYANA', 'UNIVERSITAS PENDIDIKAN GANESHA'))
                if jbali == 'PILIH PTN':
                    slide3.write('PILIH PTN')

                if jbali == 'UDAYANA':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS UDAYANA')
                    # Memfilter baris yang mengandung "UNIVERSITAS UDAYANA" di kolom "PTN"
                    filtered_data_udayana = df[df['PTN'].str.contains('UNIVERSITAS UDAYANA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_udayana)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS UDAYANA
                    udayana_data = df[df['PTN'] == 'UNIVERSITAS UDAYANA']
                    
                    udayana_prodi = udayana_data['NAMA PRODI']
                    rata_udayana_nilai = udayana_data['RATAAN']
                    minim_udayana_nilai = udayana_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    udayana_data_gabung = pd.concat([udayana_prodi, rata_udayana_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(udayana_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    udayana_data_gabung = pd.concat([udayana_prodi, minim_udayana_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(udayana_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    udayana_data_gabung = pd.concat([udayana_prodi, rata_udayana_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(udayana_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)


                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_udayana =udayana_data['RATAAN'].mean()
                    average2_udayana =udayana_data['S.BAKU'].mean()
                    average3_udayana =udayana_data['MIN'].mean()
                    average4_udayana =udayana_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_udayana, average2_udayana, average3_udayana, average4_udayana]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS UDAYANA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jbali == 'UNIVERSITAS PENDIDIKAN GANESHA':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS PENDIDIKAN GANESHA')
                    # Memfilter baris yang mengandung "UNIVERSITAS PENDIDIKAN GANESHA" di kolom "PTN"
                    filtered_data_ganesha = df[df['PTN'].str.contains('UNIVERSITAS PENDIDIKAN GANESHA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_ganesha)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS PENDIDIKAN GANESHA
                    ganesha_data = df[df['PTN'] == 'UNIVERSITAS PENDIDIKAN GANESHA']
                    
                    ganesha_prodi = ganesha_data['NAMA PRODI']
                    rata_ganesha_nilai = ganesha_data['RATAAN']
                    minim_ganesha_nilai = ganesha_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ganesha_data_gabung = pd.concat([ganesha_prodi, rata_ganesha_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(ganesha_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ganesha_data_gabung = pd.concat([ganesha_prodi, minim_ganesha_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(ganesha_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_ganesha =ganesha_data['RATAAN'].mean()
                    average2_ganesha =ganesha_data['S.BAKU'].mean()
                    average3_ganesha =ganesha_data['MIN'].mean()
                    average4_ganesha =ganesha_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_ganesha, average2_ganesha, average3_ganesha, average4_ganesha]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS PENDIDIKAN GANESHA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

        elif selected_option == 'SUMATRA':
                # Filter data untuk masing-masing PTN
                sumatra_data_sriwijaya = df[df['PTN'].isin(['UNIVERSITAS SRIWIJAYA'])]
                sumatra_data_sumatera_utara = df[df['PTN'].isin(['UNIVERSITAS SUMATERA UTARA'])]
                sumatra_data_andalas = df[df['PTN'].isin(['UNIVERSITAS ANDALAS'])]
                sumatra_data_bengkulu = df[df['PTN'].isin(['UNIVERSITAS BENGKULU'])]

                # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [sumatra_data_sriwijaya['MAX'].mean(), sumatra_data_sumatera_utara['MAX'].mean(), sumatra_data_andalas['MAX'].mean(),
                                sumatra_data_bengkulu['MAX'].mean()]

                min_per_ptn = [sumatra_data_sriwijaya['MIN'].mean(), sumatra_data_sumatera_utara['MIN'].mean(), sumatra_data_andalas['MIN'].mean(),
                                sumatra_data_bengkulu['MIN'].mean()]
                    
                rataan_per_ptn = [sumatra_data_sriwijaya['RATAAN'].mean(), sumatra_data_sumatera_utara['RATAAN'].mean(), sumatra_data_andalas['RATAAN'].mean(),
                                sumatra_data_bengkulu['RATAAN'].mean()]

                nama_ptn = ['UNIVERSITAS SRIWIJAYA', 'UNIVERSITAS SUMATERA UTARA', 'UNIVERSITAS ANDALAS','UNIVERSITAS BENGKULU']

                # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jumlah dta yang dipilih
                total_sumatra_sriwijaya = len(sumatra_data_sriwijaya)
                total_sumatra_sumatera_utara = len(sumatra_data_sumatera_utara)
                total_sumatra_andalas = len(sumatra_data_andalas)
                total_sumatra_bengkulu = len(sumatra_data_bengkulu)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS SRIWIJAYA': total_sumatra_sriwijaya,
                    'UNIVERSITAS SUMATERA UTARA': total_sumatra_sumatera_utara,
                    'UNIVERSITAS ANDALAS': total_sumatra_andalas,
                    'UNIVERSITAS BENGKULU': total_sumatra_bengkulu,
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)

                jsumatra = slide3.radio(
                "Pilih PTN di Jawa Timur",
                ('PILIH PTN','UNIVERSITAS SRIWIJAYA','UNIVERSITAS SUMATERA UTARA','UNIVERSITAS ANDALAS','UNIVERSITAS BENGKULU'))
                if jsumatra == 'PILIH PTN':
                    slide3.write ('PILIH PTN')

                if jsumatra == 'UNIVERSITAS SRIWIJAYA':
                    slide3.write('UNIVERSITAS SRIWIJAYA')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS SRIWIJAYA')
                    # Memfilter baris yang mengandung "UNIVERSITAS SRIWIJAYA" di kolom "PTN"
                    filtered_data_ganesha = df[df['PTN'].str.contains('UNIVERSITAS SRIWIJAYA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_ganesha)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS SRIWIJAYA
                    ganesha_data = df[df['PTN'] == 'UNIVERSITAS SRIWIJAYA']
                    
                    ganesha_prodi = ganesha_data['NAMA PRODI']
                    rata_ganesha_nilai = ganesha_data['RATAAN']
                    minim_ganesha_nilai = ganesha_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ganesha_data_gabung = pd.concat([ganesha_prodi, rata_ganesha_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(ganesha_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ganesha_data_gabung = pd.concat([ganesha_prodi, minim_ganesha_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(ganesha_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    ganesha_data_gabung = pd.concat([ganesha_prodi, rata_ganesha_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(ganesha_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_ganesha =ganesha_data['RATAAN'].mean()
                    average2_ganesha =ganesha_data['S.BAKU'].mean()
                    average3_ganesha =ganesha_data['MIN'].mean()
                    average4_ganesha =ganesha_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_ganesha, average2_ganesha, average3_ganesha, average4_ganesha]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS SRIWIJAYA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                    
                if jsumatra == 'UNIVERSITAS SUMATERA UTARA':
                    slide3.write('UNIVERSITAS SUMATERA UTARA')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS SUMATERA UTARA')
                    # Memfilter baris yang mengandung "UNIVERSITAS SUMATERA UTARA" di kolom "PTN"
                    filtered_data_usu = df[df['PTN'].str.contains('UNIVERSITAS SUMATERA UTARA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_usu)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS SUMATERA UTARA
                    usu_data = df[df['PTN'] == 'UNIVERSITAS SUMATERA UTARA']
                    
                    usu_prodi = usu_data['NAMA PRODI']
                    rata_usu_nilai = usu_data['RATAAN']
                    minim_usu_nilai = usu_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    usu_data_gabung = pd.concat([usu_prodi, rata_usu_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(usu_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    usu_data_gabung = pd.concat([usu_prodi, minim_usu_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(usu_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    usu_data_gabung = pd.concat([usu_prodi, rata_usu_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(usu_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_usu =usu_data['RATAAN'].mean()
                    average2_usu =usu_data['S.BAKU'].mean()
                    average3_usu =usu_data['MIN'].mean()
                    average4_usu =usu_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_usu, average2_usu, average3_usu, average4_usu]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS SUMATERA UTARA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jsumatra == 'UNIVERSITAS ANDALAS':
                    slide3.write('UNIVERSITAS ANDALAS')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS ANDALAS')
                    # Memfilter baris yang mengandung "UNIVERSITAS ANDALAS" di kolom "PTN"
                    filtered_data_andalas = df[df['PTN'].str.contains('UNIVERSITAS ANDALAS')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_andalas)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS ANDALAS
                    andalas_data = df[df['PTN'] == 'UNIVERSITAS ANDALAS']
                    
                    andalas_prodi = andalas_data['NAMA PRODI']
                    rata_andalas_nilai = andalas_data['RATAAN']
                    minim_andalas_nilai = andalas_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    andalas_data_gabung = pd.concat([andalas_prodi, rata_andalas_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(andalas_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    andalas_data_gabung = pd.concat([andalas_prodi, minim_andalas_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(andalas_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    andalas_data_gabung = pd.concat([andalas_prodi, rata_andalas_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(andalas_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_andalas =andalas_data['RATAAN'].mean()
                    average2_andalas =andalas_data['S.BAKU'].mean()
                    average3_andalas =andalas_data['MIN'].mean()
                    average4_andalas =andalas_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_andalas, average2_andalas, average3_andalas, average4_andalas]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS ANDALAS')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jsumatra == 'UNIVERSITAS BENGKULU':
                    slide3.write('UNIVERSITAS BENGKULU')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS BENGKULU')
                    # Memfilter baris yang mengandung "UNIVERSITAS BENGKULU" di kolom "PTN"
                    filtered_data_bengkulu = df[df['PTN'].str.contains('UNIVERSITAS BENGKULU')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_bengkulu)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS BENGKULU
                    bengkulu_data = df[df['PTN'] == 'UNIVERSITAS BENGKULU']
                    
                    bengkulu_prodi = bengkulu_data['NAMA PRODI']
                    rata_bengkulu_nilai = bengkulu_data['RATAAN']
                    minim_bengkulu_nilai = bengkulu_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    bengkulu_data_gabung = pd.concat([bengkulu_prodi, rata_bengkulu_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(bengkulu_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    bengkulu_data_gabung = pd.concat([bengkulu_prodi, minim_bengkulu_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(bengkulu_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_bengkulu =bengkulu_data['RATAAN'].mean()
                    average2_bengkulu =bengkulu_data['S.BAKU'].mean()
                    average3_bengkulu =bengkulu_data['MIN'].mean()
                    average4_bengkulu =bengkulu_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_bengkulu, average2_bengkulu, average3_bengkulu, average4_bengkulu]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS BENGKULU')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 


        if selected_option == 'ACEH':
                # Filter data untuk masing-masing PTN
                aceh_data_kuala = df[df['PTN'].isin(['UNIVERSITAS SYIAH KUALA'])]
                aceh_data_maliku = df[df['PTN'].isin(['UNIVERSITAS MALIKUSSALEH'])]
                aceh_data_palangkaraya = df[df['PTN'].isin(['UNIVERSITAS PALANGKARAYA'])]

                # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [aceh_data_kuala['MAX'].mean(), aceh_data_maliku['MAX'].mean(), aceh_data_palangkaraya['MAX'].mean()]

                min_per_ptn = [aceh_data_kuala['MIN'].mean(), aceh_data_maliku['MIN'].mean(), aceh_data_palangkaraya['MIN'].mean()]
                    
                rataan_per_ptn = [aceh_data_kuala['RATAAN'].mean(), aceh_data_maliku['RATAAN'].mean(), aceh_data_palangkaraya['RATAAN'].mean()]

                nama_ptn = ['UNIVERSITAS SYIAH KUALA', 'UNIVERSITAS MALIKUSSALEH', 'UNIVERSITAS PALANGKARAYA',]

                # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jumlah dta yang dipilih
                total_aceh_kuala = len(aceh_data_kuala)
                total_aceh_maliku = len(aceh_data_maliku)
                total_aceh_palangkaraya = len(aceh_data_palangkaraya)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS SYIAH KUALA': total_aceh_kuala,
                    'UNIVERSITAS MALIKUSSALEH': total_aceh_maliku,
                    'UNIVERSITAS PALANGKARAYA': total_aceh_palangkaraya,
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)

                jaceh = slide3.radio(
                "Pilih PTN di ACEH",
                ('PILIH PTN','UNIVERSITAS SYIAH KUALA','UNIVERSITAS MALIKUSSALEH','UNIVERSITAS PALANGKARAYA'))
        
                if jaceh == 'PILIH PTN':
                    slide3.write('PILIH PTN')

                if jaceh == 'UNIVERSITAS SYIAH KUALA':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS SYIAH KUALA')
                    # Memfilter baris yang mengandung "UNIVERSITAS SYIAH KUALA" di kolom "PTN"
                    filtered_data_kuala = df[df['PTN'].str.contains('UNIVERSITAS SYIAH KUALA')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_kuala)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS SYIAH KUALA
                    kuala_data = df[df['PTN'] == 'UNIVERSITAS SYIAH KUALA']

                    kuala_prodi = kuala_data['NAMA PRODI']
                    rata_kuala_nilai = kuala_data['RATAAN']
                    minim_kuala_nilai = kuala_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    kuala_data_gabung = pd.concat([kuala_prodi, rata_kuala_nilai, minim_kuala_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_kuala = kuala_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_kuala)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(kuala_data_gabung, x='NAMA PRODI', y='MIN', title='Minimum Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    kuala_data_gabung = pd.concat([kuala_prodi, rata_kuala_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(kuala_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_kuala = kuala_data['RATAAN'].mean()
                    average2_kuala = kuala_data['S.BAKU'].mean()
                    average3_kuala = kuala_data['MIN'].mean()
                    average4_kuala = kuala_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_kuala, average2_kuala, average3_kuala, average4_kuala]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS SYIAH KUALA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jaceh == 'UNIVERSITAS MALIKUSSALEH':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS MALIKUSSALEH')
                    # Memfilter baris yang mengandung "UNIVERSITAS MALIKUSSALEH" di kolom "PTN"
                    filtered_data_maliku_saleh = df[df['PTN'].str.contains('UNIVERSITAS MALIKUSSALEH')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_maliku_saleh)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS MALIKUSSALEH
                    maliku_saleh_data = df[df['PTN'] == 'UNIVERSITAS MALIKUSSALEH']

                    uin_sgd_prodi = maliku_saleh_data['NAMA PRODI']
                    rata_maliku_saleh_nilai = maliku_saleh_data['RATAAN']
                    minim_maliku_saleh_nilai = maliku_saleh_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    maliku_saleh_data_gabung = pd.concat([uin_sgd_prodi, rata_maliku_saleh_nilai, minim_maliku_saleh_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_uin_sgd = maliku_saleh_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_uin_sgd)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(maliku_saleh_data_gabung, x='NAMA PRODI', y='MIN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    maliku_saleh_data_gabung = pd.concat([uin_sgd_prodi, rata_maliku_saleh_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(maliku_saleh_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_maliku_saleh = maliku_saleh_data['RATAAN'].mean()
                    average2_maliku_saleh = maliku_saleh_data['S.BAKU'].mean()
                    average3_maliku_saleh = maliku_saleh_data['MIN'].mean()
                    average4_maliku_saleh = maliku_saleh_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_maliku_saleh, average2_maliku_saleh, average3_maliku_saleh, average4_maliku_saleh]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS MALIKUSSALEH')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jaceh == 'UNIVERSITAS PALANGKARAYA':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS PALANGKARAYA')
                    # Memfilter baris yang mengandung "UNIVERSITAS PALANGKARAYA" di kolom "PTN"
                    filtered_data_palangkaraya = df[df['PTN'].str.contains('UNIVERSITAS PALANGKARAYA')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_palangkaraya)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS PALANGKARAYA
                    palangkaraya_data = df[df['PTN'] == 'UNIVERSITAS PALANGKARAYA']

                    uin_sgd_prodi = palangkaraya_data['NAMA PRODI']
                    rata_palangkaraya_nilai = palangkaraya_data['RATAAN']
                    minim_palangkaraya_nilai = palangkaraya_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    palangkaraya_data_gabung = pd.concat([uin_sgd_prodi, rata_palangkaraya_nilai, minim_palangkaraya_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_uin_sgd = palangkaraya_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_uin_sgd)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(palangkaraya_data_gabung, x='NAMA PRODI', y='MIN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    palangkaraya_data_gabung = pd.concat([uin_sgd_prodi, rata_palangkaraya_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(palangkaraya_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_palangkaraya = palangkaraya_data['RATAAN'].mean()
                    average2_palangkaraya = palangkaraya_data['S.BAKU'].mean()
                    average3_palangkaraya = palangkaraya_data['MIN'].mean()
                    average4_palangkaraya = palangkaraya_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_palangkaraya, average2_palangkaraya, average3_palangkaraya, average4_palangkaraya]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS PALANGKARAYA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)


        elif selected_option == 'KALIMANTAN':
                # Filter data untuk masing-masing PTN
                kalimantan_data_mulawarman = df[df['PTN'].isin(['UNIVERSITAS MULAWARMAN'])]
                kalimantan_data_lambung_mangkurat = df[df['PTN'].isin(['UNIVERSITAS LAMBUNG MANGKURAT'])]
                kalimantan_data_tanjungpura = df[df['PTN'].isin(['UNIVERSITAS TANJUNGPURA'])]

                # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [kalimantan_data_mulawarman['MAX'].mean(), kalimantan_data_lambung_mangkurat['MAX'].mean(), kalimantan_data_tanjungpura['MAX'].mean()]

                min_per_ptn = [kalimantan_data_mulawarman['MIN'].mean(), kalimantan_data_lambung_mangkurat['MIN'].mean(), kalimantan_data_tanjungpura['MIN'].mean()]
                    
                rataan_per_ptn = [kalimantan_data_mulawarman['RATAAN'].mean(), kalimantan_data_lambung_mangkurat['RATAAN'].mean(), kalimantan_data_tanjungpura['RATAAN'].mean()]

                nama_ptn = ['UNIVERSITAS MULAWARMAN', 'UNIVERSITAS LAMBUNG MANGKURAT', 'UNIVERSITAS TANJUNGPURA',]

                # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jumlah dta yang dipilih
                total_kalimantan_mulawarman = len(kalimantan_data_mulawarman)
                total_kalimantan_lambung_mangkurat = len(kalimantan_data_lambung_mangkurat)
                total_kalimantan_tanjungpura = len(kalimantan_data_tanjungpura)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS MULAWARMAN': total_kalimantan_mulawarman,
                    'UNIVERSITAS LAMBUNG MANGKURAT': total_kalimantan_lambung_mangkurat,
                    'UNIVERSITAS TANJUNGPURA': total_kalimantan_tanjungpura,
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)

                jkalimantan = slide3.radio(
                "Pilih PTN di KALIMANTAN",
                ('PILIH PTN','UNIVERSITAS MULAWARMAN','UNIVERSITAS LAMBUNG MANGKURAT','UNIVERSITAS TANJUNGPURA'))

                if jkalimantan == 'PILIH PTN':
                    slide3.write('PILIH PTN')

                if jkalimantan == 'UNIVERSITAS MULAWARMAN':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS MULAWARMAN')
                    # Memfilter baris yang mengandung "UNIVERSITAS MULAWARMAN" di kolom "PTN"
                    filtered_data_mulawarman = df[df['PTN'].str.contains('UNIVERSITAS MULAWARMAN')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_mulawarman)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS MULAWARMAN
                    mulawarman_data = df[df['PTN'] == 'UNIVERSITAS MULAWARMAN']

                    mulawarman_prodi = mulawarman_data['NAMA PRODI']
                    rata_mulawarman_nilai = mulawarman_data['RATAAN']
                    minim_mulawarman_nilai = mulawarman_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    mulawarman_data_gabung = pd.concat([mulawarman_prodi, rata_mulawarman_nilai, minim_mulawarman_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_mulawarman = mulawarman_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_mulawarman)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(mulawarman_data_gabung, x='NAMA PRODI', y='MIN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    mulawarman_data_gabung = pd.concat([mulawarman_prodi, rata_mulawarman_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(mulawarman_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    mulawarman_data_gabung = pd.concat([mulawarman_prodi, rata_mulawarman_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(mulawarman_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_mulawarman = mulawarman_data['RATAAN'].mean()
                    average2_mulawarman = mulawarman_data['S.BAKU'].mean()
                    average3_mulawarman = mulawarman_data['MIN'].mean()
                    average4_mulawarman = mulawarman_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_mulawarman, average2_mulawarman, average3_mulawarman, average4_mulawarman]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS MULAWARMAN')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jkalimantan == 'UNIVERSITAS LAMBUNG MANGKURAT':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS LAMBUNG MANGKURAT')
                    # Memfilter baris yang mengandung "UNIVERSITAS LAMBUNG MANGKURAT" di kolom "PTN"
                    filtered_data_lambung_mangkurat = df[df['PTN'].str.contains('UNIVERSITAS LAMBUNG MANGKURAT')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_lambung_mangkurat)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS LAMBUNG MANGKURAT
                    lambung_mangkurat_data = df[df['PTN'] == 'UNIVERSITAS LAMBUNG MANGKURAT']

                    lambung_mangkurat_prodi = lambung_mangkurat_data['NAMA PRODI']
                    rata_lambung_mangkurat_nilai = lambung_mangkurat_data['RATAAN']
                    minim_lambung_mangkurat_nilai = lambung_mangkurat_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    lambung_mangkurat_data_gabung = pd.concat([lambung_mangkurat_prodi, rata_lambung_mangkurat_nilai, minim_lambung_mangkurat_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_lambung_mangkurat = lambung_mangkurat_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_lambung_mangkurat)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(lambung_mangkurat_data_gabung, x='NAMA PRODI', y='MIN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    lambung_mangkurat_data_gabung = pd.concat([lambung_mangkurat_prodi, rata_lambung_mangkurat_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(lambung_mangkurat_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    lambung_mangkurat_data_gabung = pd.concat([lambung_mangkurat_prodi, rata_lambung_mangkurat_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(lambung_mangkurat_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_lambung_mangkurat = lambung_mangkurat_data['RATAAN'].mean()
                    average2_lambung_mangkurat = lambung_mangkurat_data['S.BAKU'].mean()
                    average3_lambung_mangkurat = lambung_mangkurat_data['MIN'].mean()
                    average4_lambung_mangkurat = lambung_mangkurat_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_lambung_mangkurat, average2_lambung_mangkurat, average3_lambung_mangkurat, average4_lambung_mangkurat]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS LAMBUNG MANGKURAT')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jkalimantan == 'UNIVERSITAS TANJUNGPURA':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS TANJUNGPURA')
                    # Memfilter baris yang mengandung "UNIVERSITAS TANJUNGPURA" di kolom "PTN"
                    filtered_data_tanjung = df[df['PTN'].str.contains('UNIVERSITAS TANJUNGPURA')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_tanjung)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS TANJUNGPURA
                    tanjung_data = df[df['PTN'] == 'UNIVERSITAS TANJUNGPURA']

                    tanjung_prodi = tanjung_data['NAMA PRODI']
                    rata_tanjung_nilai = tanjung_data['RATAAN']
                    minim_tanjung_nilai = tanjung_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    tanjung_data_gabung = pd.concat([tanjung_prodi, rata_tanjung_nilai, minim_tanjung_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_tanjung = tanjung_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_tanjung)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(tanjung_data_gabung, x='NAMA PRODI', y='MIN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    tanjung_data_gabung = pd.concat([tanjung_prodi, rata_tanjung_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(tanjung_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    tanjung_data_gabung = pd.concat([tanjung_prodi, rata_tanjung_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(tanjung_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_tanjung = tanjung_data['RATAAN'].mean()
                    average2_tanjung = tanjung_data['S.BAKU'].mean()
                    average3_tanjung = tanjung_data['MIN'].mean()
                    average4_tanjung = tanjung_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_tanjung, average2_tanjung, average3_tanjung, average4_tanjung]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS TANJUNGPURA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)


        if selected_option == 'SULAWESI':
                # Filter data untuk masing-masing PTN
                sulawesi_data_unhas = df[df['PTN'].isin(['UNIVERSITAS HASANUDDIN'])]
                sulawesi_data_alaudin = df[df['PTN'].isin(['UNIVERSITAS ISLAM NEGERI ALAUDDIN'])]
                sulawesi_data_haluoleo = df[df['PTN'].isin(['UNIVERSITAS HALUOLEO'])]

                # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [sulawesi_data_unhas['MAX'].mean(), sulawesi_data_alaudin['MAX'].mean(), sulawesi_data_haluoleo['MAX'].mean()]

                min_per_ptn = [sulawesi_data_unhas['MIN'].mean(), sulawesi_data_alaudin['MIN'].mean(), sulawesi_data_haluoleo['MIN'].mean()]
                    
                rataan_per_ptn = [sulawesi_data_unhas['RATAAN'].mean(), sulawesi_data_alaudin['RATAAN'].mean(), sulawesi_data_haluoleo['RATAAN'].mean()]

                nama_ptn = ['UNIVERSITAS HASANUDDIN', 'UNIVERSITAS ISLAM NEGERI ALAUDDIN', 'UNIVERSITAS HALUOLEO',]

                # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jumlah dta yang dipilih
                total_sulawesi_unhas = len(sulawesi_data_unhas)
                total_sulawesi_alaudin = len(sulawesi_data_alaudin)
                total_sulawesi_haluoleo = len(sulawesi_data_haluoleo)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS HASANUDDIN': total_sulawesi_unhas,
                    'UNIVERSITAS ISLAM NEGERI ALAUDDIN': total_sulawesi_alaudin,
                    'UNIVERSITAS HALUOLEO': total_sulawesi_haluoleo,
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)

                jsulawesi = slide3.radio(
                "Pilih PTN di SULAWESI",
                ('PILIH PTN','UNIVERSITAS HASANUDDIN','UNIVERSITAS ISLAM NEGERI ALAUDDIN','UNIVERSITAS HALUOLEO'))
                if jsulawesi == 'PILIH PTN':
                    slide3.write('PILIH PTN')

                if jsulawesi == 'UNIVERSITAS HASANUDDIN':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS HASANUDDIN')
                    # Memfilter baris yang mengandung "UNIVERSITAS HASANUDDIN" di kolom "PTN"
                    filtered_data_has = df[df['PTN'].str.contains('UNIVERSITAS HASANUDDIN')]

                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_has)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS HASANUDDIN
                    has_data = df[df['PTN'] == 'UNIVERSITAS HASANUDDIN']

                    has_prodi = has_data['NAMA PRODI']
                    rata_has_nilai = has_data['RATAAN']
                    minim_has_nilai = has_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    has_data_gabung = pd.concat([has_prodi, rata_has_nilai, minim_has_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_has = has_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_has)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(has_data_gabung, x='NAMA PRODI', y='MIN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    has_data_gabung = pd.concat([has_prodi, rata_has_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(has_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    has_data_gabung = pd.concat([has_prodi, rata_has_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(has_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_has = has_data['RATAAN'].mean()
                    average2_has = has_data['S.BAKU'].mean()
                    average3_has = has_data['MIN'].mean()
                    average4_has = has_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_has, average2_has, average3_has, average4_has]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS HASANUDDIN')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jsulawesi == 'UNIVERSITAS ISLAM NEGERI ALAUDDIN':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS ISLAM NEGERI ALAUDDIN')
                    # Memfilter baris yang mengandung "UNIVERSITAS ISLAM NEGERI ALAUDDIN" di kolom "PTN"
                    filtered_data_alaudin = df[df['PTN'].str.contains('UNIVERSITAS ISLAM NEGERI ALAUDDIN')]

                    # Menampilkan dalam Streamlit
                    slide3.table(filtered_data_alaudin)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS ISLAM NEGERI ALAUDDIN
                    alaudin_data = df[df['PTN'] == 'UNIVERSITAS ISLAM NEGERI ALAUDDIN']

                    alaudin_prodi = alaudin_data['NAMA PRODI']
                    rata_alaudin_nilai = alaudin_data['RATAAN']
                    minim_alaudin_nilai = alaudin_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    alaudin_data_gabung = pd.concat([alaudin_prodi, rata_alaudin_nilai, minim_alaudin_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_alaudin = alaudin_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_alaudin)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(alaudin_data_gabung, x='NAMA PRODI', y='MIN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    alaudin_data_gabung = pd.concat([alaudin_prodi, rata_alaudin_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(alaudin_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    alaudin_data_gabung = pd.concat([alaudin_prodi, rata_alaudin_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(alaudin_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_alaudin = alaudin_data['RATAAN'].mean()
                    average2_alaudin = alaudin_data['S.BAKU'].mean()
                    average3_alaudin = alaudin_data['MIN'].mean()
                    average4_alaudin = alaudin_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_alaudin, average2_alaudin, average3_alaudin, average4_alaudin]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS ISLAM NEGERI ALAUDDIN')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jsulawesi == 'UNIVERSITAS HALUOLEO':
                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS HALUOLEO')
                    # Memfilter baris yang mengandung "UNIVERSITAS HALUOLEO" di kolom "PTN"
                    filtered_data_halue = df[df['PTN'].str.contains('UNIVERSITAS HALUOLEO')]

                    # Menampilkan dalam Streamlit
                    slide3.table(filtered_data_halue)
                    
                    # Membuat supset data hanya untuk UNIVERSITAS HALUOLEO
                    halue_data = df[df['PTN'] == 'UNIVERSITAS HALUOLEO']

                    halue_prodi = halue_data['NAMA PRODI']
                    rata_halue_nilai = halue_data['RATAAN']
                    minim_halue_nilai = halue_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    halue_data_gabung = pd.concat([halue_prodi, rata_halue_nilai, minim_halue_nilai], axis=1)

                    # Menampilkan nilai rata-rata MIN
                    nilai_rata_rata_halue = halue_data_gabung['MIN'].mean()
                    print("Nilai rata-rata MIN:", nilai_rata_rata_halue)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(halue_data_gabung, x='NAMA PRODI', y='MIN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    halue_data_gabung = pd.concat([halue_prodi, rata_halue_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(halue_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    halue_data_gabung = pd.concat([halue_prodi, rata_halue_nilai], axis=1)

                    # Membuat pie chart menggunakan Plotly Express
                    fig = px.pie(halue_data_gabung, names='NAMA PRODI', values='RATAAN', title='Pie Chart Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_halue = halue_data['RATAAN'].mean()
                    average2_halue = halue_data['S.BAKU'].mean()
                    average3_halue = halue_data['MIN'].mean()
                    average4_halue = halue_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_halue, average2_halue, average3_halue, average4_halue]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk UNIVERSITAS HALUOLEO')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

        elif selected_option == 'DAERAH TIMUR':
                # Filter data untuk masing-masing PTN
                timur_data_mataram = df[df['PTN'].isin(['UNIVERSITAS MATARAM'])]
                timur_data_riau = df[df['PTN'].isin(['UNIVERSITAS RIAU'])]
                timur_data_jambi = df[df['PTN'].isin(['UNIVERSITAS JAMBI'])]
                timur_data_cendrawasih = df[df['PTN'].isin(['UNIVERSITAS CENDERAWASIH'])]
                timur_data_sam = df[df['PTN'].isin(['UNIVERSITAS SAM RATULANGI'])]
                timur_data_nusa = df[df['PTN'].isin(['UNIVERSITAS NUSA CENDANA'])]
                timur_data_patimura = df[df['PTN'].isin(['UNIVERSITAS PATTIMURA'])]
                timur_data_tadulako = df[df['PTN'].isin(['UNIVERSITAS TADULAKO'])]

                    # Menghitung rata-rata dan minimum menggunakan fungsi mean() pada kolom 'MAX' dan 'MIN' untuk masing-masing PTN
                max_per_ptn = [timur_data_mataram['MAX'].mean(), timur_data_riau['MAX'].mean(), timur_data_jambi['MAX'].mean(),
                                timur_data_cendrawasih['MAX'].mean(), timur_data_sam['MAX'].mean(), timur_data_nusa['MAX'].mean(),
                                timur_data_patimura['MAX'].mean(), timur_data_tadulako['MAX'].mean()]

                min_per_ptn = [timur_data_mataram['MIN'].mean(), timur_data_riau['MIN'].mean(), timur_data_jambi['MIN'].mean(),
                                timur_data_cendrawasih['MIN'].mean(), timur_data_sam['MIN'].mean(), timur_data_nusa['MIN'].mean(),
                                timur_data_patimura['MIN'].mean(), timur_data_tadulako['MIN'].mean()]
                    
                rataan_per_ptn = [timur_data_mataram['RATAAN'].mean(), timur_data_riau['RATAAN'].mean(), timur_data_jambi['RATAAN'].mean(),
                                timur_data_cendrawasih['RATAAN'].mean(), timur_data_sam['RATAAN'].mean(), timur_data_nusa['RATAAN'].mean(),
                                timur_data_patimura['RATAAN'].mean(), timur_data_tadulako['RATAAN'].mean()]

                nama_ptn = ['UNIVERSITAS MATARAM', 'UNIVERSITAS RIAU', 'UNIVERSITAS JAMBI',
                                'UNIVERSITAS CENDERAWASIH', 'UNIVERSITAS SAM RATULANGI',
                                'UNIVERSITAS NUSA CENDANA', 'UNIVERSITAS PATTIMURA', 'UNIVERSITAS TADULAKO']

                    # Multiselect untuk memilih PTN yang akan ditampilkan
                selected_ptn = st.multiselect('Pilih PTN', nama_ptn, default=nama_ptn)

                    # Filter dataframe berdasarkan PTN yang dipilih
                filtered_data = df[df['PTN'].isin(selected_ptn)]
                    # Menampilkan grouped bar chart menggunakan Plotly
                fig = go.Figure(data=[
                        go.Bar(name='Rata-rata nilai MAX', x=selected_ptn, y=max_per_ptn),
                        go.Bar(name='Rata-rata nilai MIN', x=selected_ptn, y=min_per_ptn),
                        go.Bar(name='Rata-rata nilai RATAAN', x=selected_ptn, y=rataan_per_ptn)
                    ])

                fig.update_layout(barmode='group')

                    # Menampilkan chart menggunakan Streamlit
                st.plotly_chart(fig)
        
                # menhitung jpatimuralah dta yang dipilih
                total_timur_mataram = len(timur_data_mataram)
                total_timur_riau = len(timur_data_riau)
                total_timur_jambi = len(timur_data_jambi)
                total_timur_cendrawasih = len(timur_data_cendrawasih)
                total_timur_sam = len(timur_data_sam)
                total_timur_nusa = len(timur_data_nusa)
                total_timur_patimura = len(timur_data_patimura)
                total_timur_tadulako = len(timur_data_tadulako)

                # Create a dictionary with PTN names and their corresponding total count
                data_dict = {
                    'UNIVERSITAS MATARAM': total_timur_mataram,
                    'UNIVERSITAS RIAU': total_timur_riau,
                    'UNIVERSITAS JAMBI': total_timur_jambi,
                    'UNIVERSITAS CENDERAWASIH': total_timur_cendrawasih,
                    'UNIVERSITAS SAM RATULANGI': total_timur_sam,
                    'UNIVERSITAS NUSA CENDANA': total_timur_nusa,
                    'UNIVERSITAS PATTIMURA': total_timur_patimura,
                    'UNIVERSITAS TADULAKO': total_timur_tadulako
                }

                # Create pie chart data
                labels = list(data_dict.keys())
                values = list(data_dict.values())

                # Create a pie chart
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

                # Display the chart using Streamlit
                st.plotly_chart(fig)


                jtimur = slide3.radio(
                "Pilih PTN di DAERAH TIMUR",
                ('PILIH PTN','UNIVERSITAS MATARAM','UNIVERSITAS RIAU','UNIVERSITAS JAMBI','UNIVERSITAS CENDRAWASIH','UNIVERSITAS SAM RATULANGI','UNIVERSITAS NUSA CENDANA','UNIVERSITAS PATTIMURA','UNIVERSITAS TADULAKO'))

                if jtimur == 'PILIH PTN':
                    slide3.write('PILIH PTN')

                if jtimur == 'UNIVERSITAS MATARAM':
                    slide3.write('UNIVERSITAS MATARAM')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS MATARAM')
                    # Memfilter baris yang mengandung "'UNIVERSITAS MATARAM" di kolom "PTN"
                    filtered_data_mataram = df[df['PTN'].str.contains('UNIVERSITAS MATARAM')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_mataram)
                    
                    # Membuat supset data hanya untuk 'UNIVERSITAS MATARAM
                    mataram_data = df[df['PTN'] == 'UNIVERSITAS MATARAM']
                    
                    mataram_prodi = mataram_data['NAMA PRODI']
                    rata_mataram_nilai = mataram_data['RATAAN']
                    minim_mataram_nilai = mataram_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    mataram_data_gabung = pd.concat([mataram_prodi, rata_mataram_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(mataram_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    mataram_data_gabung = pd.concat([mataram_prodi, minim_mataram_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(mataram_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_mataram =mataram_data['RATAAN'].mean()
                    average2_mataram =mataram_data['S.BAKU'].mean()
                    average3_mataram =mataram_data['MIN'].mean()
                    average4_mataram =mataram_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_mataram, average2_mataram, average3_mataram, average4_mataram]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS MATARAM')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jtimur == 'UNIVERSITAS RIAU':
                    slide3.write('UNIVERSITAS RIAU')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS RIAU')
                    # Memfilter baris yang mengandung "'UNIVERSITAS RIAU" di kolom "PTN"
                    filtered_data_RIAU = df[df['PTN'].str.contains('UNIVERSITAS RIAU')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_RIAU)
                    
                    # Membuat supset data hanya untuk 'UNIVERSITAS RIAU
                    RIAU_data = df[df['PTN'] == 'UNIVERSITAS RIAU']
                    
                    RIAU_prodi = RIAU_data['NAMA PRODI']
                    rata_RIAU_nilai = RIAU_data['RATAAN']
                    minim_RIAU_nilai = RIAU_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    RIAU_data_gabung = pd.concat([RIAU_prodi, rata_RIAU_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(RIAU_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    RIAU_data_gabung = pd.concat([RIAU_prodi, minim_RIAU_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(RIAU_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_RIAU =RIAU_data['RATAAN'].mean()
                    average2_RIAU =RIAU_data['S.BAKU'].mean()
                    average3_RIAU =RIAU_data['MIN'].mean()
                    average4_RIAU =RIAU_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_RIAU, average2_RIAU, average3_RIAU, average4_RIAU]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS RIAU')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jtimur == 'UNIVERSITAS JAMBI':
                    slide3.write('UNIVERSITAS JAMBI')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS JAMBI')
                    # Memfilter baris yang mengandung "'UNIVERSITAS JAMBI" di kolom "PTN"
                    filtered_data_JAMBI = df[df['PTN'].str.contains('UNIVERSITAS JAMBI')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_JAMBI)
                    
                    # Membuat supset data hanya untuk 'UNIVERSITAS JAMBI
                    JAMBI_data = df[df['PTN'] == 'UNIVERSITAS JAMBI']
                    
                    JAMBI_prodi = JAMBI_data['NAMA PRODI']
                    rata_JAMBI_nilai = JAMBI_data['RATAAN']
                    minim_JAMBI_nilai = JAMBI_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    JAMBI_data_gabung = pd.concat([JAMBI_prodi, rata_JAMBI_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(JAMBI_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    JAMBI_data_gabung = pd.concat([JAMBI_prodi, minim_JAMBI_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(JAMBI_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_JAMBI =JAMBI_data['RATAAN'].mean()
                    average2_JAMBI =JAMBI_data['S.BAKU'].mean()
                    average3_JAMBI =JAMBI_data['MIN'].mean()
                    average4_JAMBI =JAMBI_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_JAMBI, average2_JAMBI, average3_JAMBI, average4_JAMBI]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS JAMBI')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jtimur == 'UNIVERSITAS SAM RATULANGI':
                    slide3.write('UNIVERSITAS SAM RATULANGI')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS SAM RATULANGI')
                    # Memfilter baris yang mengandung "'UNIVERSITAS SAM RATULANGI" di kolom "PTN"
                    filtered_data_RATULANGI = df[df['PTN'].str.contains('UNIVERSITAS SAM RATULANGI')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_RATULANGI)
                    
                    # Membuat supset data hanya untuk 'UNIVERSITAS SAM RATULANGI
                    RATULANGI_data = df[df['PTN'] == 'UNIVERSITAS SAM RATULANGI']
                    
                    RATULANGI_prodi = RATULANGI_data['NAMA PRODI']
                    rata_RATULANGI_nilai = RATULANGI_data['RATAAN']
                    minim_RATULANGI_nilai = RATULANGI_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    RATULANGI_data_gabung = pd.concat([RATULANGI_prodi, rata_RATULANGI_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(RATULANGI_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    RATULANGI_data_gabung = pd.concat([RATULANGI_prodi, minim_RATULANGI_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(RATULANGI_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_RATULANGI =RATULANGI_data['RATAAN'].mean()
                    average2_RATULANGI =RATULANGI_data['S.BAKU'].mean()
                    average3_RATULANGI =RATULANGI_data['MIN'].mean()
                    average4_RATULANGI =RATULANGI_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_RATULANGI, average2_RATULANGI, average3_RATULANGI, average4_RATULANGI]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS SAM RATULANGI')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jtimur == 'UNIVERSITAS CENDERAWASIH':
                    slide3.write('UNIVERSITAS CENDERAWASIH')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS CENDERAWASIH')
                    # Memfilter baris yang mengandung "'UNIVERSITAS CENDERAWASIH" di kolom "PTN"
                    filtered_data_CENDERAWASIH = df[df['PTN'].str.contains('UNIVERSITAS CENDERAWASIH')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_CENDERAWASIH)
                    
                    # Membuat supset data hanya untuk 'UNIVERSITAS CENDERAWASIH
                    CENDERAWASIH_data = df[df['PTN'] == 'UNIVERSITAS CENDERAWASIH']
                    
                    CENDERAWASIH_prodi = CENDERAWASIH_data['NAMA PRODI']
                    rata_CENDERAWASIH_nilai = CENDERAWASIH_data['RATAAN']
                    minim_CENDERAWASIH_nilai = CENDERAWASIH_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    CENDERAWASIH_data_gabung = pd.concat([CENDERAWASIH_prodi, rata_CENDERAWASIH_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(CENDERAWASIH_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    CENDERAWASIH_data_gabung = pd.concat([CENDERAWASIH_prodi, minim_CENDERAWASIH_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(CENDERAWASIH_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_CENDERAWASIH =CENDERAWASIH_data['RATAAN'].mean()
                    average2_CENDERAWASIH =CENDERAWASIH_data['S.BAKU'].mean()
                    average3_CENDERAWASIH =CENDERAWASIH_data['MIN'].mean()
                    average4_CENDERAWASIH =CENDERAWASIH_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_CENDERAWASIH, average2_CENDERAWASIH, average3_CENDERAWASIH, average4_CENDERAWASIH]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS CENDERAWASIH')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 

                if jtimur == 'UNIVERSITAS NUSA CENDANA':
                    slide3.write('UNIVERSITAS NUSA CENDANA')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS NUSA CENDANA')
                    # Memfilter baris yang mengandung "'UNIVERSITAS NUSA CENDANA" di kolom "PTN"
                    filtered_data_nusa_cendana = df[df['PTN'].str.contains('UNIVERSITAS NUSA CENDANA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_nusa_cendana)
                    
                    # Membuat supset data hanya untuk 'UNIVERSITAS NUSA CENDANA
                    nusa_cendana_data = df[df['PTN'] == 'UNIVERSITAS NUSA CENDANA']
                    
                    nusa_cendana_prodi = nusa_cendana_data['NAMA PRODI']
                    rata_nusa_cendana_nilai = nusa_cendana_data['RATAAN']
                    minim_nusa_cendana_nilai = nusa_cendana_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    nusa_cendana_data_gabung = pd.concat([nusa_cendana_prodi, rata_nusa_cendana_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(nusa_cendana_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    nusa_cendana_data_gabung = pd.concat([nusa_cendana_prodi, minim_nusa_cendana_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(nusa_cendana_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_nusa_cendana =nusa_cendana_data['RATAAN'].mean()
                    average2_nusa_cendana =nusa_cendana_data['S.BAKU'].mean()
                    average3_nusa_cendana =nusa_cendana_data['MIN'].mean()
                    average4_nusa_cendana =nusa_cendana_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_nusa_cendana, average2_nusa_cendana, average3_nusa_cendana, average4_nusa_cendana]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS NUSA CENDANA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 


                if jtimur == 'UNIVERSITAS PATTIMURA':
                    slide3.write('UNIVERSITAS PATTIMURA')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS PATTIMURA')
                    # Memfilter baris yang mengandung "'UNIVERSITAS PATTIMURA" di kolom "PTN"
                    filtered_data_patimura = df[df['PTN'].str.contains('UNIVERSITAS PATTIMURA')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_patimura)
                    
                    # Membuat supset data hanya untuk 'UNIVERSITAS PATTIMURA
                    patimura_data = df[df['PTN'] == 'UNIVERSITAS PATTIMURA']
                    
                    patimura_prodi = patimura_data['NAMA PRODI']
                    rata_patimura_nilai = patimura_data['RATAAN']
                    minim_patimura_nilai = patimura_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    patimura_data_gabung = pd.concat([patimura_prodi, rata_patimura_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(patimura_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    patimura_data_gabung = pd.concat([patimura_prodi, minim_patimura_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(patimura_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_patimura =patimura_data['RATAAN'].mean()
                    average2_patimura =patimura_data['S.BAKU'].mean()
                    average3_patimura =patimura_data['MIN'].mean()
                    average4_patimura =patimura_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_patimura, average2_patimura, average3_patimura, average4_patimura]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS PATTIMURA')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig)

                if jtimur == 'UNIVERSITAS TADULAKO':
                    slide3.write('UNIVERSITAS TADULAKO')

                    #menampilkan tulisan
                    slide3.write('UNIVERSITAS TADULAKO')
                    # Memfilter baris yang mengandung "'UNIVERSITAS TADULAKO" di kolom "PTN"
                    filtered_data_tadulako = df[df['PTN'].str.contains('UNIVERSITAS TADULAKO')]
                    
                    # Menampilkan hasil dalam Streamlit
                    slide3.table(filtered_data_tadulako)
                    
                    # Membuat supset data hanya untuk 'UNIVERSITAS TADULAKO
                    tadulako_data = df[df['PTN'] == 'UNIVERSITAS TADULAKO']
                    
                    tadulako_prodi = tadulako_data['NAMA PRODI']
                    rata_tadulako_nilai = tadulako_data['RATAAN']
                    minim_tadulako_nilai = tadulako_data['MIN']

                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    tadulako_data_gabung = pd.concat([tadulako_prodi, rata_tadulako_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(tadulako_data_gabung, x='NAMA PRODI', y='RATAAN', title='Rata-rata Nilai per Prodi')
                    slide3.plotly_chart(fig)
                    # Menggabungkan "NAMA PRODI" dan "RATAAN" menjadi satu DataFrame
                    tadulako_data_gabung = pd.concat([tadulako_prodi, minim_tadulako_nilai], axis=1)

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.histogram(tadulako_data_gabung, x='NAMA PRODI', y='MIN', title='Nilai Minimun per Prodi')
                    slide3.plotly_chart(fig)

                    # Menghitung nilai rata-rata, standar deviasi, nilai minimum, dan nilai maksimum untuk kolom-kolom tertentu
                    average1_tadulako =tadulako_data['RATAAN'].mean()
                    average2_tadulako =tadulako_data['S.BAKU'].mean()
                    average3_tadulako =tadulako_data['MIN'].mean()
                    average4_tadulako =tadulako_data['MAX'].mean()

                    # Membuat dataframe untuk ditampilkan dalam bar chart
                    chart_data = pd.DataFrame({
                        'Metrik': ['Nilai rata-rata', 'Rata-rata S.BAKU', 'Rata-rata Minimum', 'Rata-rata Maksimum'],
                        'Nilai': [average1_tadulako, average2_tadulako, average3_tadulako, average4_tadulako]
                    })

                    # Membuat bar chart menggunakan Plotly Express
                    fig = px.bar(chart_data, x='Metrik', y='Nilai', title='Metrik Statistik untuk  UNIVERSITAS TADULAKO')

                    # Menampilkan plot menggunakan Streamlit
                    slide3.plotly_chart(fig) 
