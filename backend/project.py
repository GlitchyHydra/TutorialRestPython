from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('project_main.html')

@app.route('/abstract')
def abstract():
    return render_template('project_abstract.html')

@app.route('/background')
def background():
    return render_template('project_background.html')

@app.route('/methods')
def methods():
    return render_template('project_methods.html')

@app.route('/results')
def results():
    return render_template('project_results.html')

@app.route('/discussion')
def discussion():
    return render_template('project_discussion.html')

@app.route('/conclusions')
def conclusions():
    return render_template('project_conclusions.html')

@app.route('/references')
def references():
    return render_template('project_references.html')

@app.route('/acknowledgments')
def acknowledgments():
    return render_template('project_acknowledgments.html')

@app.route('/author_information')
def author_information():
    return render_template('project_author_information.html')

@app.route('/ethics_declarations')
def ethics_declarations():
    return render_template('project_ethics_declarations.html')

@app.route('/rights_and_permissions')
def rights_and_permissions():
    return render_template('project_rights_and_permissions.html')

@app.route('/cite_this_article')
def citethisarticle():
    return render_template('project_cite_this_article.html')

if __name__ == "__main__":
    app.run(debug=True)