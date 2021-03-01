from pheme import Pheme
def hello_world():
    return "Hello World"
app = Pheme.App()
app.get("/",hello_world)
app.serve("127.0.0.1",8000)
