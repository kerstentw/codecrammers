import web, site

site.addsitedir("/home/tk/pprojects/codecrammers/bin")
import codecrammers

urls = ("/codecrammers", "Index",
		"/codecrammers/archive", "Archives",
		"/codecrammers/forum", "Forum",
		"/codecrammers/links", "Links",
		"/codecrammers/contact", "Contact"
		)
		
render = web.template.render(
"/home/tk/pprojects/CodeCrammers/templates/",
base = "/home/tk/pprojects/CodeCrammers/templates/layout"
)

class Index(object):
	def GET(self):
		content = ("Code Crammers!", 
		codecrammers.generate_frontpage()
		)  ##Title of page, article generator
		
		
		return render.index(content = content)
		
	def POST(self):
		pass

class Archives(object):
	
	def GET(self):
		My_RSS = codecrammers.RSSEngine()
		content = My_RSS.createRSS()
		return render.archives(content = content)
		
	def POST(self):
		pass

class Forum(object):
	def GET(self):
		content = "Frame Linked"
		return render.forum(content = content)
		
	def POST(self):
		pass

class Links(object):
	def GET(self):
		content = "Frame Linked"
		return render.links(content = content)
		
	def POST(self):
		pass
		
class Contact(object):
	def GET(self):
		content = codecrammers.generate_contact()
		return render.contact(content = content)
		
	def POST(self):
		pass
		
app = web.application(urls,globals())
application = app.wsgifunc()

if __name__ == "__main__":
	app.run()
