import tornado.web
import tornado.ioloop
import json
class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        """
        It opens a file, reads the contents, splits the contents into a list, closes the file, and writes
        the list to the browser
        """
        fh = open("file_handling/list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))
    def post(self):
        """
        It takes the value of the fruit argument from the request, appends it to the list.txt file, and
        returns a JSON response
        """
        fruit = self.get_argument("fruit")
        fh = open("file_handling/list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))
    
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", mainRequestHandler),
        (r"/list", listRequestHandler)
    ])
    
    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()