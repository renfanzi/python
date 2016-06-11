
import pickle
import os
import sys
import hashlib
lj_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(lj_path)
from config import setting
from lib import modules
from db import *
import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('server waiting....')
        conn,addr = sk.accept()  #接受
        client_data = conn.recv(1024)  #recovery获取，最大1024字节
    #    str(client_data, encoding='utf-8')
        conn.sendall(bytes('输入用户名 ',encoding='utf-8'))
        #---------用户登录或注册
        log_or_reg = conn.recv(1024)
        log_or_reg_content = str(log_or_reg, encoding='utf-8')
        #________用户（客户端输入的用户名）
        user_data = conn.recv(1024)
        user_data_name = str(user_data, encoding='utf-8')
    #    print(user_data_name)
        #---------用户（客户端输入的密码）
        user_data2 = conn.recv(1024)
        user_data_pwd = str(user_data2, encoding='utf-8')
    #    print(user_data_pwd)
        #---------利用类创建对象
        hash = hashlib.md5(bytes('aaa', encoding='utf-8'))
        hash.update(bytes(user_data_pwd, encoding='utf-8'))
        jiami_md = hash.hexdigest()
        print(jiami_md)
        obj = modules.Client(user_data_name, jiami_md)
        print(obj)
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), MyServer)
    server.serve_forever()

