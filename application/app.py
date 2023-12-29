from flask import Flask, render_template, request

import pandas as pd
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def transform_text(text):
    
    # step 1: lower case
    text = text.lower()
    
    # step 2: tokenisation 
    text = nltk.word_tokenize(text)
    
    # step 3: appending the words which only have alphabets and numbers
    text = [word for word in text if word.isalnum()]
    
    # step 4: appending those words which are not in stopwords and punctuation
    text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation]
        
    # step 5: stem the words in the list
    text = [ps.stem(word) for word in text]
    
    return " ".join(text)

def predict(input_sms):
    tfidf = pd.read_pickle('application/vectorizer.pkl')
    model = pd.read_pickle('application/model.pkl')

    # 1. preprocess
    transformed_sms = transform_text(input_sms)

    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3. predict
    result = model.predict(vector_input)[0]

    # 4. Display
    if result == 1:
        return "Spam"
    else:
        return "Not Spam"



app = Flask(__name__)

@app.route('/')
def spam():
	return render_template("index.html")

@app.route('/submit',methods=["POST"])
def submit():
    input_sms = request.form['input_sms']
    return render_template("index.html",data=predict(input_sms))

if __name__ == '__main__':
    app.run(debug=True)
