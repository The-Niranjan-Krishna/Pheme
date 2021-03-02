class Parser:
    def __init__(self,request):
        self.request = request
        self.method = None
        self.path = {}
        self.headers = {}
        self.body = {}
    def parse(self):
        contents = self.request.split("\r\n") 
        request_line = contents[0].split()
        self.method = request_line[0]
        abs_path = request_line[1].split("?")
        self.path['uri'] = abs_path[0]
        self.path["params"] = {i.split("=")[0]:i.split("=")[1] for i in abs_path[-1].split("&") }
        ei = contents.index("")
        self.headers = {i.split(":")[0]:i.split(":")[1] for i in contents[2:ei] }
        self.body = contents[ei:-1]
        
        
