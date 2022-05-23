import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(
            "Hello, World this is a python command executed from the backend.")


class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        """
        If the argument is a valid integer, then the function writes back to the client whether the
        integer is odd or even
        """
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        """
        The function takes in two parameters, studentName and courseId, and returns a string that says
        "Welcome {studentName} you are viewing course {courseId}"

        :param studentName: This is the name of the student
        :param courseId: This is the parameter that we are passing in the URL
        """
        self.write(f"Welcome {studentName} you are viewing course {courseId}")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animal", listRequestHandler),

        # http://localhost:8000/isEven?num=8
        (r"/isEven", queryParamRequestHandler),

        # http://localhost:8000/students/william/8
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler)
    ])

    port = 8000
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
