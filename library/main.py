# in the main.py outside the website folder
from fontend import create_app

app = create_app()
if __name__== '__main__':
#only if we run this file, not if we import this file
#You only want it to run the web server 
#if you actually run this file directly.
	app.run(debug=True)
	#debug=True means every time we make a change to any of our Python code,
	#it's going to automatically rerun the web server.
