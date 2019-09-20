import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write('Hello, World! From the folks at Loonycorn!')

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
