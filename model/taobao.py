
class TaoBaoModel(object):

    def __init__(self, db):
        self.db = db

    def get_taobao_list(self):
        return self.db.query('select * from taobaodata')
