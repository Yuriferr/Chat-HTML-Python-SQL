from flask import Flask, render_template, request, send_from_directory
import os
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    
    if message:
        conn = sqlite3.connect('chat.db')
        c = conn.cursor()
        c.execute('INSERT INTO messages (message) VALUES (?)', (message,))
        conn.commit()
        conn.close()
    
    return ''

@app.route('/fetch_messages', methods=['GET'])
def fetch_messages():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('SELECT * FROM messages')
    messages = c.fetchall()
    conn.close()
    
    response = ''
    
    for message in messages:
        response += '<p>' + message[1] + '</p>'
    
    return response

def create_database():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')
    conn.commit()
    conn.close()

create_database()

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True)
