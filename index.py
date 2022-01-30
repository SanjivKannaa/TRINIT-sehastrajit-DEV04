import tornado.ioloop
import tornado.web

class home_RequestHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('Welcome to my server!\n\ngoogle\napple\namazon\ndigilocker\ndiscord\nfacebook\nfiitjee\nfitbit\ninstagram\nmicrosoft\nsony\nwalker\ncarparking\nwifi')
        self.render("index.html")
    def post():
        pass

class _RequestHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('Welcome to my server!\n\ngoogle\napple\namazon\ndigilocker\ndiscord\nfacebook\nfiitjee\nfitbit\ninstagram\nmicrosoft\nsony\nwalker\ncarparking\nwifi')
        self.render("index.html")









if __name__ == '__main__':
    app =  tornado.web.Application([
        (r"/home",  home_RequestHandler),
        (r"/",  _RequestHandler),
        ()
    ])
    port = 8080
    app.listen(port)
    print('working on port', port)
    tornado.ioloop.IOLoop.current().start() #infinite loop  