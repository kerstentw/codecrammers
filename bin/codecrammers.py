import sqlite3, site

site.addsitedir("/home/tk/pprojects/CodeCrammers/bin")
import archive
	
ARCHIVE_PAGE_MAX = 5 	
	
#Replace the .py archive with the sqllite3 one

def generate_posttuple(post_dic):
	
	postTuple = (
	post_dic["heading"],
	post_dic["author"],
	post_dic["content"],
	)
	
	return postTuple

def generate_frontpage():
	gen_me = list()
	
	for entry in archive.front_page_posts: #Change this to increase number on front page
		print "Here is ENTRY:", entry
		gen_me.append(generate_posttuple(entry))
		
	return gen_me
	

	
	for index in range(len(page_list)): 
		link = '<a href = "//{0}">{0}</a>'.format(index)
		archive_pages.append(link)
		
		aggegate_page = page_list[index]


def generate_contact():
	contact_page = """
	<h3>Cole R.</h3>
		<br/>
		<div id = "Text"> 
		  Cole is a filthy horse-man who wandered into Montana on a 
	frosty morning in the middle of October.  Hungry, he demanded oats 
	from a nearby farmer. A bit non-plussed about the equestrian-mount
	making demands, the farmer challenged Cole to a fight.  Cole, being
	a horse and quite strong, tidily killed the farmer with a swift
	back kick.  At first, Cole felt no guilt for his deed as it was 
	the farmer who started the fight.  However, as he grew he began
	to understand that a young stallion must learn to own a situation
	and that death is so permanent and its affects so wide, it is no
	creatures's right to take the life of another.  Cole then swore
	to never fight again, became a vegetarian and joined the Unitarian 
	church.  To this day, Cole the Colt still wonders what would have 
	been had he diffused the situation.  Perhaps him and the farmer 
	could have separated in peace.  Perhaps they could have become 
	friends.  Perhaps. 
	<br><br>
		Cole currently studies Java, game design, and android app dev.
	He graduated from Montana State University and has a BA in 
	graphic design. 
		</div>
	<br>
	<br>
	<br>
	
	<h3> Tai K. </h3>
		<div id = "Text">
		Tai is a lizard person.  He likes to eat flies and occationally
	takes naps on rocks.  He also likes watching youtube videos about
	knitting.  
		<br><br>
		
		Tai is currently working in Python.
		
		<div>
	
	
	"""
	
	return contact_page


class ArchiveEngine(object):
	
	def __init__(self):
		pass
		
	def generate_archive(self):
		
		archive_pages = []
		counter = 0
		aggregate_page = []
		working_page = ""
		page_list = []
		
		archiveTuples = (generate_posttuple(post) for post in archive.allposts)
			
		for post in archiveTuples:
			working_page = """
			<h2>{title}</h2>
			<h3>{author}</h3>
			<div id = "Text">{body}</div>
			""".format(title = post[0], author = post[1], body = post[2])
			
			aggregate_page.append(working_page)
			
			if len(aggregate_page) >= ARCHIVE_PAGE_MAX:
				page_list.append(aggregate_page)
				aggregate_page = []  
		
		
		### Place entry from list into front, include link, link goes 
		### next entry in list
			
			archive_pages = []
			
class RSSEngine(object):
	
	"""
	RSS_Engine holds the methods
for querying a database, constructing 
posts, then placing them into a structure
that fits on a web page.
	"""
	
	def __init__(self):
		self.infodict = {}
		self.frame = """
			<!--?xml-version="1.0"?--!>
			<rss version = "2.0">
			{0}
			</rss>
			"""
		
		
	def buildRSS(self,postDic):
		
		linelist = []
		for dic in postDic:
			for key in dic:
				line = "<{tag}> {body} </{tag}>".format(tag = key, body = dic[key])
				linelist.append(line)
			
			linelist = "".join(linelist)
			
			return self.frame.format(linelist)
			
	def queryDB(self):
		pass
	
	
	def queryFile_buildRSS(self):
		"""
		crappy alternative to queryDB
		Pulls all posts
		"""
		#post_list = []
		
		#for post in archive.all_posts:
		#	 p
		
		pass
		
	def updateRSS(self):
		pass
	
	def createRSS(self):
		final = self.buildRSS(archive.all_posts)
		return final
		
		
		
	
		
