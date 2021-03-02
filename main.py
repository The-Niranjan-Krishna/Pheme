from pheme import Pheme
def hello_world(req):
    print(req.path)
    return "Hello World "+req.path['params']["a"]
app = Pheme()
app.get("/",hello_world)
app.serve("127.0.0.1",8000)
