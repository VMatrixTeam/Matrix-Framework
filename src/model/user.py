
from tornado.web import gen

class User(object):
    @gen.coroutine
    def get_user_by_id(user_id):
        user = {
            "user_id" : user_id,
            "username" : "matrix",
            "email" : "service@vmatrix.org.cn",
            "avatar" : "matrix.png"
        }
        raise gen.Return(User)
