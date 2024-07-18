from flask import Flask, request, jsonify
from encryption_decryption import encrypt_message, decrypt_message

app = Flask(_name_)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    message = data['message']
    key = data['key'].encode()
    cipher_text = encrypt_message(key, message)
    return jsonify({ 'cipherText': cipher_text.decode() })

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    cipher_text = data['cipherText'].