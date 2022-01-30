import tornado.ioloop
import tornado.web

class homeRequestHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('Welcome to my server!\n\ngoogle\napple\namazon\ndigilocker\ndiscord\nfacebook\nfiitjee\nfitbit\ninstagram\nmicrosoft\nsony\nwalker\ncarparking\nwifi')
        self.render("index.html")

class RequestHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('Welcome to my server!\n\ngoogle\napple\namazon\ndigilocker\ndiscord\nfacebook\nfiitjee\nfitbit\ninstagram\nmicrosoft\nsony\nwalker\ncarparking\nwifi')
        self.render("index.html")









if __name__ == '__main__':
    app =  tornado.web.Application([
        (r"/home",  homeRequestHandler),
        (r"/",  RequestHandler)
    ])
    port = 9090
    app.listen(port)
    print('working on port', port)
    print("open your browser and go to http://localhost:9090")
    tornado.ioloop.IOLoop.current().start() #infinite loop  