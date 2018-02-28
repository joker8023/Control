import tornado.ioloop
import tornado.web
from tornado_sqlalchemy import make_session_factory
from database.database import databaseconnet
from model.model import DatabaseFactory

session = databaseconnet('localdb')
class DatabaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def  post(self):
        self.write("asdadasd")

    def put(self, *args, **kwargs):
        session = databaseconnet('localdb')
        databaseFactory = DatabaseFactory(name='MSCNCMS', type='mssql', server='WONALIDBSTAGE', database='MSCNCMS',
                                          user='stagemscn', password='Dai2017!')
        session.add(databaseFactory)
        session.commit()
        session.close()


def make_app():
    return tornado.web.Application([
        (r"/database", DatabaseHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()