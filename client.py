import time, socket, sys

print("\nHey! Welcome to Chat Room\n")
print("Wait, let me Initialize....\n")
time.sleep(1)

s = socket.socket()
s_host = socket.gethostname()
ip = socket.gethostbyname(s_host)
print(s_host, "(", ip, ")\n")
host = input(str("Enter your server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Server has been Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined your chat room\nEnter [e] to exit this chat room\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me(You) : "))
    if message == "e":
        message = "Server Left chat room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())
