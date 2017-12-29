# -*- coding:utf-8 -*-
from handler.base import *


class ServicesHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('services.html')