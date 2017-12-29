# -*- coding:utf-8 -*-
from handler.base import *
import json

class TaoBaoHandler(BaseHandler):

    def get(self, *args, **kwargs):
        list = self.taobao_model.get_taobao_list()
        self.render('taobao.html', **{'list':list})