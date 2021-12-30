"""
Client that sends the file (uploads)
"""
# import socket
# import tqdm
# import os
# import argparse
#
# SEPARATOR = "<SEPARATOR>"
#
# BUFFER_SIZE = 1024 * 4
#
#
# def send_file(filename, host, port):
#     # get the file size
#     filesize = os.path.getsize(filename)
#     # create the client socket
#     s = socket.socket()
#     print(f"[+] Connecting to {host}:{port}")
#     s.connect((host, port))
#     print("[+] Connected.")
#
#     # send the filename and filesize
#     s.send(f"{filename}{SEPARATOR}{filesize}".encode())
#
#     # start sending the file
#     progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
#     with open(filename, "rb") as f:
#         while True:
#             # read the bytes from the file
#             bytes_read = f.read(BUFFER_SIZE)
#             if not bytes_read:
#                 # file transmitting is done
#                 break
#             # we use sendall to assure transimission in
#             # busy networks
#             s.sendall(bytes_read)
#             # update the progress bar
#             progress.update(len(bytes_read))
#
#     # close the socket
#     s.close()
#
#
# if __name__ == "__main__":
#     import argparse
#     parser = argparse.ArgumentParser(description="Simple File Sender")
#     parser.add_argument("file", help="File name to send")
#     parser.add_argument("host", help="The host/IP address of the receiver")
#     parser.add_argument("-p", "--port", help="Port to use, default is 5001", type=int, default=5001)
#     args = parser.parse_args()
#     filename = args.file
#     host = args.host
#     port = args.port
#     send_file(filename, host, port)

#
#
# #
# # import pandas as pd
# #
# # data = pd.read_csv("D:/docments/HeartDiseasePrediction/predict_risk/machine_learning_models/HealthData.csv")
# # print(data)
# # df = pd.DataFrame
# # print(df)
#
#
#
# # dicts = [{'business_name': 'ALASKA NAN', 'devices_name': 'SAMSUNG TABLET', 'deviceCount': 2}, {'business_name': 'Tandoori', 'devices_name': 'SAMSUNG TABLET', 'deviceCount':
# # 2}, {'business_name': 'AUTOMATION RESTRO', 'devices_name': 'SAMSUNG TABLET', 'deviceCount': 1}]
# #
# # entry = input("enter your name")
# # print(entry)
# # search = next(item for item in dicts if item["business_name"] == entry)
#
#
# dicts = ['ALASKA NAN', 'SAMSUNG TABLET', 'deviceCount']
# # {'business_name': 'Tandoori', 'devices_name': 'SAMSUNG TABLET', 'deviceCount':
# #  2}, {'business_name': 'AUTOMATION RESTRO', 'devices_name': 'SAMSUNG TABLET', 'deviceCount': 1}
# # seatch = input("enter your name  :")
# # print(seatch)
# # cd = next(item for item in dicts if item["business_name"] == seatch)
# # print(cd)
#
# #!/usr/bin/env python3
# # Define a list of flowers
# flowerList = ['rose', 'daffodil', 'sunflower', 'poppy', 'bluebell']
#
#
# x = input("enter a name:")
# L = [{'count': 2, 'business_name': 'ALASKA NAN', 'support_id': '8945492', 'customer_name': 'Bhas Kalangi Kalangi', 'email_id': '', 'customer_number': '01315553330', 'is_active': 'Active'}, {'count': 2, 'business_name': 'Tandoori', 'support_id': '2294655', 'customer_name': 'Max ', 'email_id': '', 'customer_number': '44444444444', 'is_active': 'Active'}, {'count': 2, 'business_name': 'ALASKA NAN', 'support_id': '8945492', 'customer_name': 'Bhas Kalangi Kalangi', 'email_id': '', 'customer_number':
#  '01315553330', 'is_active': 'Active'}, {'count': 2, 'business_name': 'Tandoori', 'support_id': '2294655', 'customer_name': 'Max ', 'email_id': '', 'customer_number'
# : '44444444444', 'is_active': 'Active'}, {'count': 1, 'business_name': 'AUTOMATION RESTRO', 'support_id': '1932838', 'customer_name': 'James Bell Bell', 'email_id':
# '', 'customer_number': '02030028299', 'is_active': 'Active'}]
# res = [y for y in L if x in y["business_name"]]
# print(res)
#
#
# # # pip install pycryptodome
# # import base64
# # import string
# # import random
# # import hashlib
# #
# # from Cryptodome.Cipher import AES
# # #from Crypto.Cipher import AES
# #
# #
# # IV = "@@@@&&&&####$$$$"
# # BLOCK_SIZE = 16
# #
# #
# # def generate_checksum(param_dict, merchant_key, salt=None):
# #     params_string = __get_param_string__(param_dict)
# #     salt = salt if salt else __id_generator__(4)
# #     final_string = '%s|%s' % (params_string, salt)
# #
# #     hasher = hashlib.sha256(final_string.encode())
# #     hash_string = hasher.hexdigest()
# #
# #     hash_string += salt
# #
# #     return __encode__(hash_string, IV, merchant_key)
# #
# # def generate_refund_checksum(param_dict, merchant_key, salt=None):
# #     for i in param_dict:
# #         if("|" in param_dict[i]):
# #             param_dict = {}
# #             exit()
# #     params_string = __get_param_string__(param_dict)
# #     salt = salt if salt else __id_generator__(4)
# #     final_string = '%s|%s' % (params_string, salt)
# #
# #     hasher = hashlib.sha256(final_string.encode())
# #     hash_string = hasher.hexdigest()
# #
# #     hash_string += salt
# #
# #     return __encode__(hash_string, IV, merchant_key)
# #
# #
# # def generate_checksum_by_str(param_str, merchant_key, salt=None):
# #     params_string = param_str
# #     salt = salt if salt else __id_generator__(4)
# #     final_string = '%s|%s' % (params_string, salt)
# #
# #     hasher = hashlib.sha256(final_string.encode())
# #     hash_string = hasher.hexdigest()
# #
# #     hash_string += salt
# #
# #     return __encode__(hash_string, IV, merchant_key)
# #
# #
# # def verify_checksum(param_dict, merchant_key, checksum):
# #     # Remove checksum
# #     if 'CHECKSUMHASH' in param_dict:
# #         param_dict.pop('CHECKSUMHASH')
# #
# #     # Get salt
# #     paytm_hash = __decode__(checksum, IV, merchant_key)
# #     salt = paytm_hash[-4:]
# #     calculated_checksum = generate_checksum(param_dict, merchant_key, salt=salt)
# #     return calculated_checksum == checksum
# #
# # def verify_checksum_by_str(param_str, merchant_key, checksum):
# #     # Remove checksum
# #     #if 'CHECKSUMHASH' in param_dict:
# #         #param_dict.pop('CHECKSUMHASH')
# #
# #     # Get salt
# #     paytm_hash = __decode__(checksum, IV, merchant_key)
# #     salt = paytm_hash[-4:]
# #     calculated_checksum = generate_checksum_by_str(param_str, merchant_key, salt=salt)
# #     return calculated_checksum == checksum
# #
# #
# #
# # def __id_generator__(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
# #     return ''.join(random.choice(chars) for _ in range(size))
# #
# #
# # def __get_param_string__(params):
# #     params_string = []
# #     for key in sorted(params.keys()):
# #         if("REFUND" in params[key] or "|" in params[key]):
# #             respons_dict = {}
# #             exit()
# #         value = params[key]
# #         params_string.append('' if value == 'null' else str(value))
# #     return '|'.join(params_string)
# #
# #
# # __pad__ = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
# # __unpad__ = lambda s: s[0:-ord(s[-1])]
# #
# #
# # def __encode__(to_encode, iv, key):
# #     # Pad
# #     to_encode = __pad__(to_encode)
# #     # Encrypt
# #     c = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
# #     to_encode = c.encrypt(to_encode.encode('utf-8'))
# #     # Encode
# #     to_encode = base64.b64encode(to_encode)
# #     return to_encode.decode("UTF-8")
# #
# #
# # def __decode__(to_decode, iv, key):
# #     # Decode
# #     to_decode = base64.b64decode(to_decode)
# #     # Decrypt
# #     c = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
# #     to_decode = c.decrypt(to_decode)
# #     if type(to_decode) == bytes:
# #         # convert bytes array to str.
# #         to_decode = to_decode.decode()
# #     # remove pad
# #     return __unpad__(to_decode)
# #
# #
# # if __name__ == "__main__":
# #     params = {
# #         "MID": "mid",
# #         "ORDER_ID": "order_id",
# #         "CUST_ID": "cust_id",
# #         "TXN_AMOUNT": "1",
# #         "CHANNEL_ID": "WEB",
# #         "INDUSTRY_TYPE_ID": "Retail",
# #         "WEBSITE": "xxxxxxxxxxx"
# #     }
# #
# #     print(verify_checksum(
# #         params, 'xxxxxxxxxxxxxxxx',
# #         "CD5ndX8VVjlzjWbbYoAtKQIlvtXPypQYOg0Fi2AUYKXZA5XSHiRF0FDj7vQu66S8MHx9NaDZ/uYm3WBOWHf+sDQAmTyxqUipA7i1nILlxrk="))
# #
# #     # print(generate_checksum(params, "xxxxxxxxxxxxxxxx"))
# #
# #
# #
# # # import base64
# # # import string
# # # import random
# # # import hashlib
# # #
# # # #from Crypto.Cipher import AES
# # # from Cryptodome.Cipher import AES
# # #
# # #
# # # IV = "@@@@&&&&####$$$$"
# # # BLOCK_SIZE = 16
# # #
# # #
# # # def generate_checksum(param_dict, merchant_key, salt=None):
# # #     params_string = __get_param_string__(param_dict)
# # #     salt = salt if salt else __id_generator__(4)
# # #     final_string = '%s|%s' % (params_string, salt)
# # #
# # #     hasher = hashlib.sha256(final_string.encode())
# # #     hash_string = hasher.hexdigest()
# # #
# # #     hash_string += salt
# # #
# # #     return __encode__(hash_string, IV, merchant_key)
# # #
# # # def generate_refund_checksum(param_dict, merchant_key, salt=None):
# # #     for i in param_dict:
# # #         if("|" in param_dict[i]):
# # #             param_dict = {}
# # #             exit()
# # #     params_string = __get_param_string__(param_dict)
# # #     salt = salt if salt else __id_generator__(4)
# # #     final_string = '%s|%s' % (params_string, salt)
# # #
# # #     hasher = hashlib.sha256(final_string.encode())
# # #     hash_string = hasher.hexdigest()
# # #
# # #     hash_string += salt
# # #
# # #     return __encode__(hash_string, IV, merchant_key)
# # #
# # #
# # # def generate_checksum_by_str(param_str, merchant_key, salt=None):
# # #     params_string = param_str
# # #     salt = salt if salt else __id_generator__(4)
# # #     final_string = '%s|%s' % (params_string, salt)
# # #
# # #     hasher = hashlib.sha256(final_string.encode())
# # #     hash_string = hasher.hexdigest()
# # #
# # #     hash_string += salt
# # #
# # #     return __encode__(hash_string, IV, merchant_key)
# # #
# # #
# # # def verify_checksum(param_dict, merchant_key, checksum):
# # #     # Remove checksum
# # #     if 'CHECKSUMHASH' in param_dict:
# # #         param_dict.pop('CHECKSUMHASH')
# # #
# # #     # Get salt
# # #     paytm_hash = __decode__(checksum, IV, merchant_key)
# # #     salt = paytm_hash[-4:]
# # #     calculated_checksum = generate_checksum(param_dict, merchant_key, salt=salt)
# # #     return calculated_checksum == checksum
# # #
# # # def verify_checksum_by_str(param_str, merchant_key, checksum):
# # #     # Remove checksum
# # #     #if 'CHECKSUMHASH' in param_dict:
# # #         #param_dict.pop('CHECKSUMHASH')
# # #
# # #     # Get salt
# # #     paytm_hash = __decode__(checksum, IV, merchant_key)
# # #     salt = paytm_hash[-4:]
# # #     calculated_checksum = generate_checksum_by_str(param_str, merchant_key, salt=salt)
# # #     return calculated_checksum == checksum
# # #
# # #
# # #
# # # def __id_generator__(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
# # #     return ''.join(random.choice(chars) for _ in range(size))
# # #
# # #
# # # def __get_param_string__(params):
# # #     params_string = []
# # #     for key in sorted(params.keys()):
# # #         if("REFUND" in params[key] or "|" in params[key]):
# # #             respons_dict = {}
# # #             exit()
# # #         value = params[key]
# # #         params_string.append('' if value == 'null' else str(value))
# # #     return '|'.join(params_string)
# # #
# # #
# # # __pad__ = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
# # # __unpad__ = lambda s: s[0:-ord(s[-1])]
# # #
# # #
# # # def __encode__(to_encode, iv, key):
# # #     # Pad
# # #     to_encode = __pad__(to_encode)
# # #     # Encrypt
# # #     c = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
# # #     to_encode = c.encrypt(to_encode.encode('utf-8'))
# # #     # Encode
# # #     to_encode = base64.b64encode(to_encode)
# # #     return to_encode.decode("UTF-8")
# # #
# # #
# # # def __decode__(to_decode, iv, key):
# # #     # Decode
# # #     to_decode = base64.b64decode(to_decode)
# # #     # Decrypt
# # #     c = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
# # #     to_decode = c.decrypt(to_decode)
# # #     if type(to_decode) == bytes:
# # #         # convert bytes array to str.
# # #         to_decode = to_decode.decode()
# # #     # remove pad
# # #     return __unpad__(to_decode)
# # #
# # #
# # # if __name__ == "__main__":
# # #     params = {
# # #         "MID": "mid",
# # #         "ORDER_ID": "order_id",
# # #         "CUST_ID": "cust_id",
# # #         "TXN_AMOUNT": "1",
# # #         "CHANNEL_ID": "WEB",
# # #         "INDUSTRY_TYPE_ID": "Retail",
# # #         "WEBSITE": "xxxxxxxxxxx"
# # #     }
# # #
# # #     print(verify_checksum(
# # #         params, 'xxxxxxxxxxxxxxxx',
# # #         "CD5ndX8VVjlzjWbbYoAtKQIlvtXPypQYOg0Fi2AUYKXZA5XSHiRF0FDj7vQu66S8MHx9NaDZ/uYm3WBOWHf+sDQAmTyxqUipA7i1nILlxrk="))
# # #
# # #     # print(generate_checksum(params, "xxxxxxxxxxxxxxxx"))

list1 = ["1, 3, 4, 7, 13"]
list2 = ["1, 2, 4, 13, 16"]
intersection_set = set.intersection(set(list1), set(list2))


intersection_list = list(intersection_set)

lsttest = list(intersection_list)
print('test',lsttest)

class fininfocom(object):
    def __init__(self,name):
        self.name = name


    def display(self):
        return self.name

class eMployee(fininfocom):
    def __init__(self,name,idNumber):
        fininfocom.__init__(self, name)
        self.name = name
        self.idNumber = idNumber
    def display2(self):
        return self.idNumber
class manager(eMployee):
    def __init__(self,name,idNumber,role):

        eMployee.__init__(self,name,idNumber)
        self.role = role
    def display3(self):
        return self.role,self.name,self.idNumber



c = manager("vedava", 12345, "ceo")
print(c.display3())
#
# class rentals():
#     def Plots(self):
#         print("only lease do not rent")
#
#     def homes(self):
#         print("only rent  and lease")
#
# class apartments(rentals):
#     def plots(self):
#         print("dont rent")
#
# class villas(rentals):
#     def homes(self):
#         print("dont lease")
#
# # from datetime import datetime,date
# #
# # inputdate = "11/18/2021 - 12/29/2021"
# # print(inputdate)
# # datess = slice(10)
# # datessss1 = inputdate[datess]
# # # date = datetime.strptime(inputdate, '%d/%m/%Y')
# # # print(date, type(date))
# # # dates = datetime.strftime(date, '%Y-%m-%d')
# # # print(dates, type(dates))
# # print(datessss1)
# # datess2 = slice(13,24)
# # datessss2 = inputdate[datess2]
# # print(datessss2)
#
#
# def bracket(l,r):
#   if r>0:
#     if l>r:
#       return bracket(l-1,r)+ bracket(l,r-1)
#     else:
#       return bracket(l,r-1)
#   else:
#     return 1
# def BracketCombinations(num):
#   # code goes here
#   res=bracket(num,num)
#   return res
#
# # keep this function call here
# print(BracketCombinations(input()))