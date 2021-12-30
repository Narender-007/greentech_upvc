from django.shortcuts import render,redirect
from django.http import HttpResponse
from Upvc_application.models import *
from pyotp import otp


# Create your views here.

def Indexss(request):
    return render(request,"index.html")

def Contact_us(request):
    return render(request,"contact.html")

def Features(request):
    return render(request,"features.html")

def Gallery(request):
    return render(request,"gallery.html")

def About_Us(request):
    return render(request,"about-us.html")

def Products(request):
    return render(request,"products.html")

def Testimonials(request):
    return render(request,"testimonials.html")

#payment gateway testing

from django.shortcuts import render
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from .Paytm import Checksum
# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):

    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

                'MID': 'Your-Merchant-Id-Here',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})

    return render(request, 'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})




# def checkout(request):
#     if request.method=="POST":
#         items_json = request.POST.get('itemsJson', '')
#         name = request.POST.get('name', '')
#         amount = request.POST.get('amount', '')
#         email = request.POST.get('email', '')
#         address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
#         city = request.POST.get('city', '')
#         state = request.POST.get('state', '')
#         zip_code = request.POST.get('zip_code', '')
#         phone = request.POST.get('phone', '')
#         order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
#                        state=state, zip_code=zip_code, phone=phone, amount=amount)
#         order.save()
#         update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
#         update.save()
#         thank = True
#         id = order.order_id
#     #     return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
#     # return render(request, 'shop/checkout.html')
#         # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
#         # request paytm to transfer the amount to your account after payment by user
#         param_dict = {
#
#             'MID': 'WorldP64425807474247',
#             'ORDER_ID': 'order.order_id',
#             'TXN_AMOUNT': '1',
#             'CUST_ID': 'email',
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID': 'WEB',
#             'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlepayment/',
#
#         }
#         return render(request, 'shop/paytm.html', {'param_dict': param_dict})
#     return render(request, 'shop/checkout.html')


"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import argparse
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.db.models import ImageField
import sys
@csrf_exempt
def sender(request):
    if request.method == "POST":
        try:
                file = BytesIO()
                data = request.POST.get("socketfile")
                print(data,type(data))
                # print(type(data),data)  # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
                # print(type(data.read()),data)  # <class 'bytes'>
                # print(type(str(data.read())),data)  # <class 'str'>
                # print(type(data),data)
                # data11 = str(data.read())
                # print(data11)
                # decods = data.read().decode()
                # print('hjgjhgjh',decods,type(decods))
                # print(type(data11), data11)
                print("sendig socket with file")
                SEPARATOR = "<SEPARATOR>"
                BUFFER_SIZE = 1024 * 4
                host = "192.168.167.26"
                # the port, let's use 5001
                port = 5001
                # the name of file we want to send, make sure it exists
                filename =    "D:/narender_workspace/newfolder/Ecommerce_Fashions/Ecommerce_Fashions/KitchenApp1.35.apk"
                print(filename,type(filename))
                h = len(filename)
                print("h",h)

                # get the file size

                filesize = os.path.getsize(filename)
                print(filesize)


                #filesize = os.path.getsize(filename)
                # create the client socket
                s = socket.socket()
                print(f"[+] Connecting to {host}:{port}")

                s.connect((host, port))
                print("[+] Connected.")

                # send the filename and filesize
                s.send(f"{filename}{SEPARATOR}{filesize}".encode())

                # start sending the file
                progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
                with open(filename, "rb") as f:
                    while True:
                        # read the bytes from the file
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            # file transmitting is done
                            break
                        # we use sendall to assure transimission in
                        # busy networks
                        s.sendall(bytes_read)
                        # update the progress bar
                        progress.update(len(bytes_read))

                # close the socket
                s.close()
                return render(request, "sender.html",{"message":"succesfully uploaded"})
        except Exception as e:
            print(e)
            return render(request,"sender.html",{"message":"file not upload"})
    else:
        return render(request, "sender.html")

def reciever(request):
    import socket
    import tqdm
    import os

    # device's IP address
    SERVER_HOST = "192.168.167.68"
    SERVER_PORT = 5001

    # receive 4096 bytes each time
    BUFFER_SIZE = 4096

    SEPARATOR = "<SEPARATOR>"

    # create the server socket
    # TCP socket
    s = socket.socket()
    # bind the socket to our local address
    s.bind((SERVER_HOST, SERVER_PORT))
    # enabling our server to accept connections
    # 5 here is the number of unaccepted connections that
    # the system will allow before refusing new connections
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    # accept connection if there is any
    client_socket, address = s.accept()
    # if below code is executed, that means the sender is connected
    print(f"[+] {address} is connected.")

    # receive the file infos
    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    print(filename)
    # convert to integer
    filesize = int(filesize)
    print(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the client socket
    client_socket.close()
    # close the server socket
    s.close()
import requests
import pyotp
@csrf_exempt
def signup(request):
    print("in")
    if request.method == 'POST':
        username = request.POST["username"]
        last_name = request.POST["last_name"]
        first_name = request.POST["first_name"]
        date_of_birth = request.POST["birthday"]
        email = request.POST["email"]
        password = request.POST["password"]
        Phone = request.POST["phone"]
        gender = request.POST["gender"]
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already taken')
            return render(request,"signup.html")
        else:

            sent = pyotp
            print(sent)
            return otp_call(un=username,pswrd= password,mail = email, fn=first_name,ln=last_name,pn=Phone,dob=date_of_birth,gen=gender)
    else:
        return render(request,"signup.html")

@csrf_exempt
def otp_call(request,**kwargs):
    print("in2")
    if request.method == 'POST':
        trials = 0
        while trials<3:
            input_otp= request.POST["six_digit"]
            if input_otp == otp:
                signedup_user = User.objects.create_user(
                    username=un,
                    password=pswrd,
                    email=mail,
                    first_name=fn,
                    last_name =ln,
                    phone_no=pn,
                    date_of_birth=dob,
                    gender= gen
                )
                signedup_user.save()
                break
                return redirect('login')
            if input_otp != otp:
                trials+=1
                messages.error(request,"wrong otp")
                return render(request,'otp_recieve.html')
    else:
        return render(request,'otp_recieve.html')



# import socketserver
#
# class MyTCPHandler(socketserver.BaseRequestHandler):
#     """
#     The request handler class for our server.
#
#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """
#
#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         print('self.client_address[0]',self.client_address[0])
#         print("{} wrote:".format(self.client_address[0]))
#         print('hkgj',self.data)
#         # just send back the same data, but upper-cased
#         self.request.sendall(self.data.upper())
#
# if __name__ == "__main__":
#     HOST, PORT = "192.168.167.68", 9999
#
#     # Create the server, binding to localhost on port 9999
#     with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
#         # Activate the server; this will keep running until you
#         # interrupt the program with Ctrl-C
#         server.serve_forever()
#
# class MyTCPHandler(socketserver.StreamRequestHandler):
#
#     def handle(self):
#         # self.rfile is a file-like object created by the handler;
#         # we can now use e.g. readline() instead of raw recv() calls
#         self.data = self.rfile.readline().strip()
#         print('self.client_address[0]', self.client_address[0])
#
#         print("{} wrote:".format(self.client_address[0]))
#         print(self.data)
#         # Likewise, self.wfile is a file-like object used to write back
#         # to the client
#         self.wfile.write(self.data.upper())
#
import socket
import sys
@csrf_exempt
def sendingSocket(request):
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
        HOST, PORT = "127.0.0.1", 8000

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

def socket(request):
    return render(request,'sender.html')

#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
#
#
# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)