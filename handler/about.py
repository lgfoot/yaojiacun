# -*- coding:utf-8 -*-
from handler.base import *


class AboutHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('about.html')