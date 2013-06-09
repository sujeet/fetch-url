import webapp2, json

from google.appengine.api import urlfetch

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        source_code = urlfetch.fetch (self.request.GET['url']).content
        function_name = self.request.GET ['funcname']
        self.response.write("%s(%s);"%(function_name,json.dumps({'source':source_code})))

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
