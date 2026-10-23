# 🥗 Prediksi Kalori Makanan Berdasarkan Kandungan Karbohidrat (TA-02)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

Repositori ini berisi proyek Tugas Akhir Modul 01 Praktikum Pembelajaran Mesin (TA-02) mengenai implementasi algoritma **Regresi Linear Sederhana** (*Simple Linear Regression*) untuk memprediksi total kalori makanan berbasis web interaktif menggunakan *framework* Flask.

---

## 📌 Deskripsi & Latar Belakang Studi Kasus

Asupan kalori dan karbohidrat merupakan salah satu fokus utama dalam menjaga pola makan yang seimbang. Dalam proyek ini, dibangun sebuah model prediktif yang mempelajari hubungan sebab-akibat antara jumlah **Karbohidrat (gram)** sebagai variabel independen ($X$) dengan total **Kalori (kcal)** sebagai variabel dependen ($y$) dari suatu makanan/minuman.

### **Detail Variabel Dataset:**
- **Variabel Independen ($X$)**: `carbs` (Kandungan karbohidrat dalam gram)
- **Variabel Dependen ($y$)**: `calories` (Total energi/kalori dalam kcal)

---

## 🛠️ Tools & Teknologi

- **Bahasa Pemrograman**: Python 3.11
- **Machine Learning & Data Processing**: `scikit-learn`, `pandas`, `numpy`, `joblib`
- **Backend Web**: Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Deployment Platform**: Render.com
- **WSGI Server**: Gunicorn

---

## 📁 Struktur Direktori Proyek

```text
m2_ta02_makanan_nutrisi_arimauludin_5c/
│
├── Food_Nutrition_Dataset.csv   # Dataset nutrisi makanan
├── train_model.py               # Script pelatihan & evaluasi model Regresi Linear
├── app.py                       # Backend Flask Web Server
├── model/
│   └── model_nutrisi.pkl        # File model ML yang sudah dilatih (.pkl)
├── templates/
│   └── index.html               # Tampilan UI antarmuka web (Bootstrap 5)
├── static/
│   └── css/
│       └── style.css            # Custom Styling CSS
├── requirements.txt             # Daftar dependensi & library Python
├── Procfile                     # Konfigurasi deployment Gunicorn
└── README.md                    # Dokumentasi utama proyek
