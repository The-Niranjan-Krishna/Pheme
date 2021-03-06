import socket
from .parser import Parser
class Pheme:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.response_codes = {"200":"HTTP/1.0 200 OK\n\n","404":"HTTP/1.0 404 NOT FOUND\n\n"}
        self.content = {}
    def get(self,route,content_function):
        self.content[route] = content_function
    def serve(self,host,port):
        self.server.bind((host,port))
        self.server.listen(1)
        while True:
            client,client_addr = self.server.accept()
            complete_request = ""
            request = client.recv(1024).decode()
            while True:
                if "\r\n" in request:
                    complete_request+=request
                    break
                complete_request+=request
                request = client.recv(1024).decode()
            req = Parser(request)
            req.parse()
            res= None
            print(req.path['uri'])

            try:
                res = self.response_codes["200"] + self.content[req.path['uri']](req)
            except:
                res = self.response_codes["404"]+"Path not found"
            client.sendall(res.encode())
            client.close()


