import asyncio

import websockets

import socket
# def encode_text_msg_websocket(data):
#     bytesFormatted = []
#     bytesFormatted.append(chr(129))
#     bytesRaw = data.encode()
#     bytesLength = len(bytesRaw)
#     if bytesLength <= 125:
#         bytesFormatted.append(chr(bytesLength))
#     elif 126 <= bytesLength <= 65535:
#         bytesFormatted.append(chr(126))
#         bytesFormatted.append((chr(bytesLength >> 8)) & 255)
#         bytesFormatted.append(chr(bytesLength) & 255)
#     else:
#         bytesFormatted.append(chr(127))
#         bytesFormatted.append(chr((bytesLength >> 56)) & 255)
#         bytesFormatted.append(chr((bytesLength >> 48)) & 255)
#         bytesFormatted.append(chr((bytesLength >> 40)) & 255)
#         bytesFormatted.append(chr((bytesLength >> 32)) & 255)
#         bytesFormatted.append(chr((bytesLength >> 24)) & 255)
#         bytesFormatted.append(chr((bytesLength >> 16)) & 255)
#         bytesFormatted.append(chr((bytesLength >> 8)) & 255)
#         bytesFormatted.append(chr(bytesLength) & 255)
#     send_str = ""
#     for i in bytesFormatted:
#         send_str+=i
#     send_str += bytesRaw
#     return send_str
#
# # connect
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.settimeout(5.0)
# try:
#     sock.connect((socket.gethostbyname('ws://192.168.167.68'), 8000))
# except:
#     print ("Connection failed")
# handshake = '\
# GET /echo HTTP/1.1\r\n\
# Host: 192.168.167.68\r\n\
# Upgrade: websocket\r\n\
# Connection: Upgrade\r\n\
# Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==\r\n\
# Origin: http://example.com\r\n\
# WebSocket-Protocol: echo\r\n\
# Sec-WebSocket-Version: 13\r\n\r\n\
# '
# sock.send(bytes(handshake))
# data = sock.recv(1024).decode('UTF-8')
# print (data)
#
# # send test msg
# msg = encode_text_msg_websocket('Now is the winter of our discontent, made glorious Summer by this son of York')
# print ("Sent: ",repr(msg))
# sock.sendall(bytes(msg))
# # receive it back
# response = sock.recv(1024)
# #decode not sorted so ignore the first 2 bytes
# print ("\nReceived: ", response[2:].decode())
# sock.close()




# import socket
#
# target_host = "192.168.167.68"
#
# target_port = 8000  # create a socket object
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # connect the client
# client.connect((target_host, target_port))
#
# # send some data
# request = "hello" % target_host
# client.send(request.encode())
#
# # receive some data
# response = client.recv(4096)
# http_response = repr(response)
# http_response_len = len(http_response)
#
# #display the response
# gh_imgui.text("[RECV] - length: %d" % http_response_len)
# gh_imgui.text_wrapped(http_response)
#
#
# import asyncio
# import websockets
# import logging
#
# # logging.basicConfig(level=logging.INFO)
# # async def consumer_handler(websocket:WebSocketClientProtocol):
# #     async for message in websocket:
# #         log_message(message)
# host = "192.168.167.68"
# print(host)
# # async def consume(message:"hello this is new socket",hostname:host,port:8000):
# #     websocket_resource_url = f"ws://{hostname}:{port}/newsocket/123"
# async with websockets.connect(f"ws://192.168.167.68:8000/newsocket/123") as websocket:
#     data2 = await websocket.send(message)
#     print(data2)
#     await websocket.recv()
#     await consumer_handler(websocket)
# #
# # def log_message(message:"hello this is new socket"):
# #     logging.info(f"Message: {message}")



import socket
#from SqlServerRequest import SqlServerRequest

# host = '192.168.167.68'
# port = 8000
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(s)
#
# s.bind((host,port))
# s.listen(5)
#
# while True:
#     # now our endpoint knows about the OTHER endpoint.
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established.")
#     inputdata = input("enter the data:")
#
#     h = clientsocket.send(bytes(inputdata, "utf-8"))
#     print("hello", h,"type",type(h))
#     data = clientsocket.recv(1024).decode()
#     print("hello data",data,"data",type(data))
#     socketclient = clientsocket.send(bytes(data, "utf-8"))
#     print("heloooo end",)
#     if data == "exit":
#         break
#     if data == "data":
#
#         d = SqlServerRequest.readData()
#         clientsocket.send(bytes(d,"utf-8"))
#         print("hello data socket", socketclient, "type",type(socketclient))

# #
# #create handler for each connection
import asyncio

import websockets

import socket
async def handler(websocket, path):
    data = await websocket.recv()

    reply = f"Data recieved as:  {data}!"
    print(reply)

    await websocket.send(reply)


start_server = websockets.serve(handler, "192.168.167.68", 8000)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()


import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print('self.client_address[0]', self.client_address[0])
        print("{} wrote:".format(self.client_address[0]))
        print('hkgj', self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "192.168.167.68", 8000

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print('self.client_address[0]', self.client_address[0])

        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())