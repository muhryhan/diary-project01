# Muhammad Ryhan
# Kelompok 4

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

connection_string = 'mongodb+srv://mryhan:mryhan@cluster0.cq5ursx.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp'
client = MongoClient(connection_string)
db = client.dbmryhan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    # sample_receive = request.args.get('sample_give')
    # print(sample_receive)

    articles = list(db.diary.find({},{'_id':False}))
    
    return jsonify({'articles': articles})

@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form["title_give"]
    content_receive = request.form["content_give"]
    content_receive = request.form["content_give"]

    today = datetime.now()
    mytime = today.strftime('%Y-%M-%d-%H-%M-%S')

    # kode logika utama menyimpan file gambar
    file = request.files["file_give"]
    extension = file.filename.split('.')[-1]
    filename = f'static/post-{mytime}.{extension}'
    file.save(filename)

    profile = request.files["profile_give"]
    extension = profile.filename.split('.')[-1]
    profilename = f'static/profile-{mytime}.{extension}'
    profile.save(profilename)

    time = today.strftime('%Y.%m.%d')

    doc = {
        'title':title_receive,
        'content':content_receive,
        'file': filename,
        'profile': profilename,
        'time' : time
    }
    db.diary.insert_one(doc)

    return jsonify({'msg':'Upload complete!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)