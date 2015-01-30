import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "Welcome"
        description = ""
        keywords = ""
        banner="<video style=\"width:100%;max-width: 100%;height:auto;z-index:-100;display: block;\" autoplay poster=\"/images/other/gary.png\"><source src=\"/videos/gary.ogv\" type=\"video/ogg\"><source src=\"/videos/gary.mp4\" type=\"video/mp4\"></video>"
        template_vars = {"title":title,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("index.html")
        self.response.write(template.render(template_vars))

class StoryHandler(webapp2.RequestHandler):
    def get(self):
        title = "Our Story"
        description = "White Collar Boxing Training offers premier world class training for professionals throughout London and the UK."
        keywords = "white collar,collar boxing,boxing training,london,uk,training sessions,professionals,trainers,big fight"
        banner = "<picture><source srcset=\"/images/banner/banner.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner.jpg\" width=\"960\" height=\"378\" alt=\"White Collar Boxing Training\" /></picture>"
        template_vars = {"title":title,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("story.html")
        self.response.write(template.render(template_vars))

class TrainersHandler(webapp2.RequestHandler):
    def get(self):
        title = "Our Trainers"
        description = ""
        keywords = ""
        banner = "<picture><source srcset=\"/images/banner/banner_3.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner_3.jpg\" width=\"960\" height=\"378\" alt=\"White Collar Boxing Training\" /></picture>"
        template_vars = {"title":title,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("trainers.html")
        self.response.write(template.render(template_vars))

class WhatsInvolvedHandler(webapp2.RequestHandler):
    def get(self):
        title = "What's involved"
        description = ""
        keywords = ""
        banner = "<picture><source srcset=\"/images/banner/banner_2.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner_2.jpg\" width=\"960\" height=\"378\" alt=\"White Collar Boxing Training\" /></picture>"
        template_vars = {"title":title,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("whats-involved.html")
        self.response.write(template.render(template_vars))

class GetInTouchHandler(webapp2.RequestHandler):
    def get(self):
        title = "Get in touch"
        description = ""
        keywords = ""
        banner = "<picture><source srcset=\"/images/banner/banner_4.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner_4.jpg\" width=\"960\" height=\"378\" alt=\"White Collar Boxing Training\" /></picture>"
        template_vars = {"title":title,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("get-in-touch.html")
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/story.html', StoryHandler),
    ('/trainers.html', TrainersHandler),
    ('/whats-involved.html', WhatsInvolvedHandler),
    ('/get-in-touch.html', GetInTouchHandler),
], debug=True)
