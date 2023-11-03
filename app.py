#! -*- encoding: utf-8 -*-
import json
import requests
from flask import Flask,render_template,request
import change as change_new
import login as login_game
import getserver
import login_super
import sendemail

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
    url = f"https://api.kit9.cn/api/random_word/api.php"
    res = requests.get(url).text
    data = json.loads(res)
    return f"{render_template('index.html')}<br/>每日一句:{data['data']['text']}"

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/admin_panel')
def admin_panel():
    return render_template("admin_panel.html")

@app.route('/admin_super',methods=['get','post'])
def admin_super():
    if request.method == 'GET':
        return render_template("admin_login.html")
    if request.method == 'POST':
        name = request.form.get('name')
        psw = request.form.get('psw')
        if login_super.is_admin(name,psw):
            return render_template('admin_su_panel.html')

@app.route('/feedback',methods=['get','post'])
def feedback():
    if request.method == 'GET':
        return render_template("feedback.html")
    if request.method == 'POST':
        des = request.form.get('feedback')
        res = sendemail.main(des)
        return f"{res}"

@app.route('/change_userdata',methods=['post'])
def change():
    print(uid,usecret)
    des = request.form.get('des')
    name = request.form.get('name')
    print(des,name)
    a = change_new.change_data_a(uid,usecret,des,name)
    print(a)
    return f"{a[1]}</br>{a[0]}"

@app.route('/getscp',methods=['post'])
def getscp():
    if request.method == 'POST':
        scp_name = request.form.get('scp_name')
        


@app.route('/server')
def server():
    serverlist = ""
    text = f"<h1>以下是列表中存在的服务器:</h1></br>电脑可以通过Ctrl+f来查找服务器</br>如果你想找的不存在可以进行刷新试试</br><h5>{serverlist.join(getserver.getlist())}</h5>"
    return text


if __name__ == "__main__":
    app.run()
