from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/results')
def results():
	return render_template('results.html')

@app.route('/research')
def research():
	return render_template('researchq.html')

@app.route('/project')
def project():
	return render_template('project.html')

@app.route('/methodology')
def methodology():
	return render_template('methodology.html')

if __name__ == '__main__':
	app.run()