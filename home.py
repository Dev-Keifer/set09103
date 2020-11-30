from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/software/')
def software():
    return render_template('software.html')

@app.route('/cms/')
def cms():
	return render_template('cms.html')
	
@app.route('/text/')
def text():
	return render_template('text.html')
	
@app.route('/design/')
def design():
	return render_template('design.html')

@app.route('/database/')
def database():
	return render_template('database.html')

@app.route('/tools/')
def tools():
	return render_template('tools.html')
	
@app.route('/testing/')
def testing():
	return render_template('testing.html')

@app.route('/hosting/')
def hosting():
	return render_template('hosting.html') 
	
@app.route('/security/')
def security():
	return render_template('security.html')
	
@app.route('/resources/')
def resources():
	return render_template('resources.html')
	
@app.route('/images/')
def images():
	return render_template('images.html')
	
@app.route('/video/')
def video():
	return render_template('video.html')
	
@app.route('/domain/')
def domain():
	return render_template('domain.html')
	
@app.route('/learn/')
def learn():
	return render_template('learn.html')
	
@app.route('/contact/')
def contact():
	return render_template('contact.html')



if __name__== "__main__":
    app.run(host='0.0.0.0', debug=True)


    



