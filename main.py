import tornado.ioloop
import tornado.web

class HomeRequestHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('Welcome to my server!\n\ngoogle\napple\namazon\ndigilocker\ndiscord\nfacebook\nfiitjee\nfitbit\ninstagram\nmicrosoft\nsony\nwalker\ncarparking\nwifi')
        self.render("home.html")

class RequestHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('Welcome to my server!\n\ngoogle\napple\namazon\ndigilocker\ndiscord\nfacebook\nfiitjee\nfitbit\ninstagram\nmicrosoft\nsony\nwalker\ncarparking\nwifi')
        self.render("home.html")








if __name__ == '__main__':
    app =  tornado.web.Application([
        (r"/home",  HomeRequestHandler),
        (r"/",  RequestHandler),
    ])
    port = 8080
    app.listen(port)
    print('working on port', port)
    tornado.ioloop.IOLoop.current().start() #infinite loop