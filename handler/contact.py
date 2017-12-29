# -*- coding:utf-8 -*-
from handler.base import *


class ContactHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('contact.html')