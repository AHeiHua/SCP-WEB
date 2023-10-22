# -*- encoding: utf-8 -*-
import json

from flask import Flask,render_template,request
import change as change_new
import login as login_game
import getserver

app = Flask(__name__)

uid = 1
usecret = ""


@app.route('/change',methods=["get","post"])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        name = request.form.get('user')
        psw = request.form.get('psw')
        print(name,psw)
        json_data = login_game.login(name,psw)
        print(json_data)
        data = json.loads(json_data)
        global uid
        global usecret
        uid = data['id']
        usecret = data['secret']
        return f"登录状态:{data['msg']}</br>{render_template('change_data.html')}"

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/change_userdata',methods=['post'])
def change():
    print(uid,usecret)
    des = request.form.get('des')
    name = request.form.get('name')
    print(des,name)
    a = change_new.change_data_a(uid,usecret,des,name)
    print(a)
    return f"{a[1]}</br>{a[0]}"

@app.route('/server')
def server():
    serverlist = ""
    text = f"<h1>以下是列表中存在的服务器:</h1></br>电脑可以通过Ctrl+f来查找服务器</br>如果你想找的不存在可以进行刷新试试</br><h5>{serverlist.join(getserver.getlist())}</h5>"
    return text


if __name__ == "__main__":
    app.run()