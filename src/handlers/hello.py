from handlers.base import BaseController
from tornado import gen

class HelloHandler(BaseController):
    @gen.coroutine
    def get(self):
        self.render("hello.jade")

    @gen.coroutine
    def post(self):
        data = {"abc" : 1}
        self.sendData(True, "post success", data)
