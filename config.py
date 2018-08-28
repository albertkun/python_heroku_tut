import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # config for postgresql/mysql databates
    HOST = 'YOUR HOST NAME'
    SECRET_KEY = 'YOUR PASSWORD'
    DATABASE = 'DATABASE NAME'
    USERNAME = 'YOUR USER NAME'
    SSL_DISABLE = False    
    PORT = '5432'

    @staticmethod
    def init_app(app):
        pass

    @classmethod
    def init_app(app):
        Config.init_app(app)

config = {

}
