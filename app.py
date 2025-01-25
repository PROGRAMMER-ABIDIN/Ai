from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Konfigurasi API Gemini
GEMINI_API_URL = "https://api.gemini.com/endpoint"  # Ganti dengan URL endpoint Gemini
API_KEY = "AIzaSyA-1r0yU9iuxO3iNcu9p0WKLF435R03bmE"  # Ganti dengan API Key Gemini

# Fungsi untuk memanggil API Gemini
def call_gemini_api(user_message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"message": user_message}
    response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("reply", "Maaf, tidak ada balasan.")
    else:
        return "Terjadi kesalahan pada server AI."

# Endpoint untuk menerima input dari frontend
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    if user_message:
        ai_reply = call_gemini_api(user_message)
        return jsonify({"reply": ai_reply})
    return jsonify({"reply": "Pesan tidak valid."}), 400

if __name__ == '__main__':
    app.run(debug=True)