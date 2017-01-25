import webapp2, json

from google.appengine.api import urlfetch

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(urlfetch.fetch(self.request.GET['url']).content)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
