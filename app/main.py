
from google.appengine.ext import webapp
import jinja2, os

current_dir = os.path.dirname(__file__)
current_path = os.path.abspath(current_dir)

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(current_dir, 'templates')))

def render(template_file, data = {}):
    template = jinja_environment.get_template(template_file)
    response = webapp.get_request().app.response_class()
    response.out.write(template.render(data))
    return response

def handle(route):
    def handler(request):
        return render('%s.html' % route)
    return handler
        
application = webapp.WSGIApplication([
        ('/', handle('index'))
    ], debug=True)
