from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    @property
    def taobao_model(self):
        return self.application.taobao_model