#coding:utf-8

import router

urls = []

urls += router.hello.urls

from handlers.error import ExceptionHandler

urls += [(r".*", ExceptionHandler)]
