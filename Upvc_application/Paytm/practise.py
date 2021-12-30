# # #
# # # """
# # # Server receiver of the file
# # # """
# # # import socket
# # # import tqdm
# # # import os
# # #
# # # # device's IP address
# # # SERVER_HOST = "192.168.167.68"
# # # SERVER_PORT = 44910
# # #
# # # # receive 4096 bytes each time
# # # BUFFER_SIZE = 4096
# # #
# # # #SEPARATOR = "<SEPARATOR>"
# # #
# # # # create the server socket
# # # # TCP socket
# # # # s = socket.socket()
# # # # bind the socket to our local address
# # # s.bind((SERVER_HOST, SERVER_PORT))
# # # # enabling our server to accept connections
# # # # 5 here is the number of unaccepted connections that
# # # # the system will allow before refusing new connections
# # # s.listen(5)
# # # print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# # # # accept connection if there is any
# # # client_socket, address = s.accept()
# # # # if below code is executed, that means the sender is connected
# # # print(f"[+] {address} is connected.")
# # #
# # # # receive the file infos
# # # # receive using client socket, not server socket
# # # # received = client_socket.recv(BUFFER_SIZE).decode()
# # # # filename, filesize = received.split(SEPARATOR)
# # # # # remove absolute path if there is
# # # # filename = os.path.basename(filename)
# # # # print(filename)
# # # # # convert to integer
# # # # filesize = int(filesize)
# # # # print(filesize)
# # # # # start receiving the file from the socket
# # # # # and writing to the file stream
# # # # progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
# # # # with open(filename, "wb") as f:
# # # #     while True:
# # # #         # read 1024 bytes from the socket (receive)
# # # #         bytes_read = client_socket.recv(BUFFER_SIZE)
# # # #         if not bytes_read:
# # # #             # nothing is received
# # # #             # file transmitting is done
# # # #             break
# # # #         # write to the file the bytes we just received
# # # #         f.write(bytes_read)
# # # #         # update the progress bar
# # # #         progress.update(len(bytes_read))
# # #
# # # # close the client socket
# # # client_socket.close()
# # # # close the server socket
# # # s.close()
# # #
# # #
# # #
# # # # import socket
# # # #
# # # # HOST = '192.168.167.68'
# # # # print(HOST)
# # # # #Returns: "WASS104983"
# # # # #I have also tried socket.gethostbyname(socket.gethostname)), returning: "25.38.252.147"
# # # # PORT = 50007
# # # # buffer_size = 1024
# # # # text = "hi i am the server pls active socket"
# # # #
# # # # sock = socket.socket()
# # # # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # # sock.bind((HOST, PORT))
# # # # sock.listen(10)
# # # # text = text.encode('utf-8')
# # # # print("Awaiting connection... ")
# # # # (clnt, addr) = sock.accept()
# # # # clnt.send(text)
# # # # data = clnt.recv(buffer_size)
# # # # print(data)
# # # # s.close()
# # # #
# # # # print("Client connected")
# # # # #
# # # # # st = ['JSYWYF,ZQLKFE,DCALYY,PKTRVT', 'ZQLKFE', 'JSYWYF', 'PKTRVT']
# # # # # sts = list(st)
# # # # # print(sts,type(sts))
# # # # # ot = sts[0:1]
# # # # # print(ot)
# # # # # lst = []
# # # # # for i in ot:
# # # # #     d = str(i[0:6])
# # # # #
# # # # #     d2 = str(i[7:12])
# # # # #     print(d2)
# # # # #     print(d,d2)
# # # # #     lst.append(d)
# # # # #     print(lst)
# # # # #     lst.append(d2)
# # # # #     print(lst)
# # # # #
# # # import atexit
# # # from time import time, strftime, localtime
# # # from datetime import timedelta
# # #
# # import datetime
# # currentDate = datetime.datetime.today()
# # print(currentDate)
# #
# # userInput = input('Please enter your birthday (mm/dd/yyyy %h:%m:%s)')
# # print(userInput)
# # birthday = datetime.datetime.strptime(userInput,'%m/%d/%Y %H:%M:%S')
# # print(birthday)
# # currentDate = datetime.datetime.strftime(currentDate,'%m-%d-%Y %H:%M:%S')
# # print(currentDate)
# # currentDate = datetime.datetime.strptime(currentDate,'%m-%d-%Y %H:%M:%S')
# # print(currentDate,'currentDate')
# # days = birthday - currentDate
# # print(days,type(days))
# # strda = str(days)
# # print(strda,type(strda))
# #
# # stat = strda[9:11]
# # print(stat,type(stat))
# # if stat < "7":
# #     print(stat,"in time data")
# #
# # else:
# #     print("in valied time")
# # from websocket import create_connection
# # ws = create_connection("ws://192.168.167.68:9999/websocket")
# # print ("Sending 'Hello, World'...")
# # ws.send("Hello, World")
# # print ("Sent")
# # print ("Receiving...")
# # result =  ws.recv()
# # print ("Received '%s'" % result)
# # ws.close()
# #


# import socket
# HOST = '192.168.167.68'# Standard loopback interface address(localhost)
# PORT = 8000  # Port to listen on(non - privileged ports are > 1023)
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('192.168.167.68', PORT))
# s.listen()
# conn, addr = s.accept()
# with conn:
#    print('Connected by', addr)
# while True:
#    data = conn.recv(1024)
# if not data:
#     pirnt("hello")
#
# conn.sendall(data)
#
# import socket
# import sys
#
# input = input("enter the data:")
#
# HOST, PORT = "192.168.167.68", 8000
# data = input#" ".join(sys.argv[1:])
# print(data)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(s)
# s.connect((HOST, PORT))

# Create a socket (SOCK_STREAM means a TCP socket)

# Connect to server and send data
#sock.connect((HOST, PORT))
#
# s.sendall(bytes(data + "\n", "utf-8"))
#
# # Receive data from the server and shut down
# received = str(s.recv(1024), "utf-8")
#
# print("Sent:     {}".format(data))
# print("Received: {}".format(received))
# # import socket
# # import sys
# #
# # HOST, PORT = "192.168.167.68", 9999
# # data = " ".join(sys.argv[1:])
# #
# # # SOCK_DGRAM is the socket type to use for UDP sockets
# # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #
# # # As you can see, there is no connect() call; UDP has no connections.
# # # Instead, data is directly sent to the recipient via sendto().
# # sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
# # received = str(sock.recv(1024), "utf-8")
# #
# # print("Sent:     {}".format(data))
# # print("Received: {}".format(received))

# list=['dddd',9,'sssss','ffffff',8]
# for lst in list:
#     print(type(lst))
#     if type(lst) in type(lst):
#         print("string data")
#     else:
#         print("int data")


# import mysql.connector
#
#
# conn = mysql.connector.connect(host="localhost",database="mydatabasesss",user="root",password='root',port=3307)
# if conn.is_connected():
#     db_Info = conn.get_server_info()
#     print("Connected to MySQL Server version ", db_Info)
#     mycursor = conn.cursor()
#     mycursor.execute("CREATE TABLE yourdata (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")
#     record = mycursor.fetchall()
#     print("You're connected to database: ", record)
#
#
# else:
#     print("no connect")
A = 4
B = 6
c = Add(5+6)
print(c)



