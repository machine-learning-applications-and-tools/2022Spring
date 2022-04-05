from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import os
import numpy as np

app = Flask(__name__)

######## Preparing the Classifier
cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir,
                 'pkl_objects',
                 'model.pkl'), 'rb'))

def classify(document):
    # complete the function to classify the text with the pickled model
    return 'test'

######## Flask
class ReviewForm(Form):
    moviereview = TextAreaField('',
                                [validators.DataRequired(),
                                validators.length(min=15)])

@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('reviewform.html', form=form)

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['moviereview']
        y = classify(review)
        return render_template('results.html',
                                content=review,
                                prediction=y)
    return render_template('reviewform.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
