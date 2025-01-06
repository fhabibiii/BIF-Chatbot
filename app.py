from flask import Flask, render_template, request, jsonify
import json
import random
import os
from transformers import pipeline, BertForSequenceClassification, BertTokenizerFast

app = Flask(__name__)

# Ambil nilai dari environment variable MODEL_PATH atau gunakan default jika tidak ada
model_path = os.getenv('MODEL_PATH', 'chatbot')

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer= BertTokenizerFast.from_pretrained(model_path)
chatbot= pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Load Dataset
def load_json_file(filename):
    # Dapatkan direktori dari script yang sedang berjalan
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Bangun path absolut ke file JSON
    json_path = os.path.join(base_dir, 'dataset', filename)

    with open(json_path, encoding='utf-8') as f:
        file = json.load(f)
    return file

# Ubah nama file ke 'intents.json'
filename = 'intents_LAA.json'
intents = load_json_file(filename)

# Create a mapping from label names to numerical IDs for classification
label2id = {'Greetings': 0,
 'name': 1,
 'Yudisium': 2,
 'Persyaratan Yudisium': 3,
 'Predikat Cumlaude': 4,
 'Kehadiran Yudisium': 5,
 'Hasil Sidang Yudisium': 6,
 'Waktu Pendaftaran Yudisium': 7,
 'Yudisium Pending': 8,
 'Pengajuan Similarity': 9,
 'Hasil Cek Similarity': 10,
 'Batas Maksimum Similarity': 11,
 'Similarity Score Lebih dari 20%': 12,
 'Status Similarity Rejected': 13,
 'Kerja Praktek': 14,
 'Surat Pengantar Kerja Praktek': 15,
 'Waktu Pelaksanaan Kerja Praktek': 16,
 'Dosen Pembimbing Kerja Praktek': 17,
 'Pelaksanaan KP Tidak Sesuai Timeline': 18,
 'Syarat SK Bimbingan TA': 19,
 'Mendapatkan SK Bimbingan TA': 20,
 'Masa Berlaku SK Bimbingan Habis': 21,
 'SK Bimbingan Tidak Bisa Diperpanjang': 22,
 'Perubahan Dosen Pembimbing TA': 23,
 'Perubahan Judul TA': 24,
 'Waktu Sidang TA': 25,
 'Pendaftaran Sidang TA': 26,
 'Jadwal Seminar Internal': 27,
 'Sertifikat Seminar Internal': 28,
 'Aktivasi Mahasiswa': 29,
 'Dispensasi': 30,
 'Transkrip Sementara': 31,
 'SKL': 32,
 'Keringanan Biaya Kuliah': 33,
 'Pengajuan Cuti': 34,
 'Batas Pengajuan Cuti': 35,
 'Jumlah Cuti': 36,
 'Pengajuan Undur Diri': 37,
 'Batas Pengajuan Undur Diri': 38,
 'Kalender Akademik': 39,
 'Pedoman Akademik': 40,
 'Ijazah dan transkrip digital': 41,
 'basila': 42,
 'wisuda': 43,
 'ijazah': 44,
 'proposal TA': 45,
 'grup kelas': 46,
 'jadwal kuliah': 47,
 'praktikum': 48,
 'Dosen Terlambat': 49,
 'Kontak Dosen': 50,
 'goodbye': 51}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        msg = request.form["msg"]
        user_input = msg.strip().lower()
        resp = get_chat_response(user_input)
        return jsonify(resp)
    else:
        return "Metode GET tidak didukung."
    
def get_chat_response(text):
    score = chatbot(text)[0]['score']

    if score < 0.8:
        return("Maaf saya tidak bisa memahami apa yang anda maksud")
    else:
        label = label2id[chatbot(text)[0]['label']]
        response = random.choice(intents['intents'][label]['responses'])
        return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)