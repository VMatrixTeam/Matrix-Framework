#coding:utf-8

from tornado import gen

import config

import asynctorndb

import user

CONFIG = config.get_config()

DB_config = dict(
    user=CONFIG['database']['test']['username'],
    passwd=CONFIG['database']['test']['password'],
    database=CONFIG['database']['test']['database'],
    host=CONFIG['database']['test']['host'],
    port=CONFIG['database']['test']['port'],
    charset=CONFIG['database']['test']['charset']
)

class DB(object):
    @staticmethod
    @gen.coroutine
    def query(sql):
        db = asynctorndb.Connect(**DB_config)
        yield db.connect()
        result = yield db.query(sql)
        yield db.close()
        raise gen.Return(result)

    @staticmethod
    @gen.coroutine
    def execute(sql):
        db = asynctorndb.Connect(**DB_config)
        yield db.connect()
        result = yield db.execute(sql)
        yield db.close()
        raise gen.Return(result)

    @staticmethod
    @gen.coroutine
    def get(sql):
        db = asynctorndb.Connect(**DB_config)
        yield db.connect()
        result = yield db.get(sql)
        yield db.close()
        raise gen.Return(result)
