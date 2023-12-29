<video src='Demo SMS Spam Classifier.mov' width=180/>

To run the project:

step 1: Download the project

git clone https://github.com/ANUSHRUTHIKAE/SMS-Spam-Classifier.git

step 2: Install all the requirements
pip install -r application/requirements.txt

step 3: Download stopwords and punkt
(add the below statements to app.y)
nltk.download('punkt)
nltk.download('stopwords')

step4: Run application
python application/app.py
