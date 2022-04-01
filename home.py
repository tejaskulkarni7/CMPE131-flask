from flask import Flask

myobj = Flask(__name__)
name = "Lisa"
city_names = ['Paris','London', 'Rome', 'Tahiti']
@myobj.route("/")
def home():
	citystring=''
	for i in city_names:
		citystring=citystring+'<li>'+i+'</li>'+'\n'
	return '''
	<html>
	<body>
	<h1>Welcome '''+name+'''!</h1>
	<a href="www.google.com">not google</a>
	<ul>'''+citystring+'''</ul>
	</body>
	</html>'''
#myobj.run()
