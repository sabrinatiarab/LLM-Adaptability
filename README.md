# LLM Adaptability : Membuat Soal Pilihan Ganda Menggunakan API LLM dari Cakra.ai
  Deskripsi: Anda diminta untuk membuat aplikasi yang dapat menghasilkan 5 pertanyaan dengan pilihan ganda (ABCD) dalam bahasa Indonesia berdasarkan dokumen yang diberikan. Anda akan menggunakan API LLM dari cakra.ai untuk membantu menghasilkan pertanyaan-pertanyaan tersebut.

https://llm-adaptability.streamlit.app/

## Ringkasan:
  Pengguna mengunggah dokumen PDF dan memasukkan kunci API dan pertanyaan mereka. Dokumen PDF dibaca, dan teks diekstraksi menggunakan load_document. Teks yang diekstrak dan pertanyaan pengguna dikirim ke layanan AI. AI menghasilkan ringkasan dan kemudian pertanyaan pilihan ganda berdasarkan ringkasan tersebut. Pertanyaan yang dihasilkan diuraikan dan ditampilkan di aplikasi Streamlit.
