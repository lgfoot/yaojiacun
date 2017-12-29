# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import torndb
import os
from tornado.options import define, options
from model.taobao import TaoBaoModel
from handler.taobao import TaoBaoHandler
from handler.index import IndexHandler
from handler.about import AboutHandler
from handler.contact import ContactHandler
from handler.news import NewsHandler
from handler.services import ServicesHandler

define('port', default=8000, type=int, help='运行端口')
define('mysql_host', default='192.168.1.13', type=str, help='服务地址')
define('mysql_database', default='illness', type=str, help='数据库名称')
define('mysql_user', default='root', type=str, help='登录账户')
define('mysql_password', default='975109', type=str, help='登录密码')


class Application(tornado.web.Application):
    def __init__(self):
        # 静态文件
        handlers = [
            (r"/", TaoBaoHandler),
            (r"/index", IndexHandler),
            (r"/about", AboutHandler),
            (r"/services", ServicesHandler),
            (r"/news", NewsHandler),
            (r"/contact", ContactHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="cookie_secret_code",
            login_url="/login",
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = torndb.Connection(host=options.mysql_host, database=options.mysql_database
                                    , user=options.mysql_user, password=options.mysql_password)
        self.taobao_model = TaoBaoModel(self.db)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port, address='127.0.0.1')
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
