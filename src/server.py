#coding:utf-8

import config
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: python server.py [environment]"
        print "environment:\t production|testing|development"
        sys.exit(os.EX_USAGE)

    ENVIRONMENT = sys.argv[1]

    config.set_config(ENVIRONMENT)

    CONFIG = config.get_config()

    import tornado.ioloop
    import tornado.web
    import tornado.httpserver
    import tornado.options

    from urls import urls

    # application

    SETTINGS = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=CONFIG['runtime']['debug'],
        login_url="/login",
        cookie_secret=CONFIG['runtime']['cookie-secret']
    )

    application = tornado.web.Application(
        handlers = urls,
        **SETTINGS
    )

    print 'Development server is running at {0}://{1}:{2}/'.format(
        CONFIG['runtime']['protocol'],
        CONFIG['runtime']['base-url'],
        CONFIG['runtime']['port']
    )

    print 'Quit the server with CONTROL-C'

    # print urls
    for url, handler in urls:
        print url,'\t',handler

    if ENVIRONMENT != "production":
        tornado.options.parse_command_line()
        server = tornado.httpserver.HTTPServer(application)
        server.listen(CONFIG['runtime']['port'])
        tornado.ioloop.IOLoop.instance().start()
    else:
        # mutiple processes in production environment
        server = tornado.httpserver.HTTPServer(application)
        server.bind(CONFIG['runtime']['port'])
        server.start(0)  # forks one process per cpu
        tornado.ioloop.IOLoop.current().start()
