# -*- coding:utf-8 -*-
from handler.base import *
import json

class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')