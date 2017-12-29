# -*- coding:utf-8 -*-
from handler.base import *


class NewsHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('news.html')