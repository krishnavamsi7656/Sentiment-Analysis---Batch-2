import nltk
import os
from flask import Flask, render_template, request
 
app = Flask(__name__)

picFolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def home():
    pic10=os.path.join(app.config['UPLOAD_FOLDER'],'senti1.jpg')
    return render_template('home2.html',bgImage=pic10)

@app.route('/predictor')
def predictor():
    pic11=os.path.join(app.config['UPLOAD_FOLDER'],'try4.jpg')
    return render_template('predictor1.html',bgIm=pic11)

@app.route('/visualizer')
def visualizer():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'trainDataset.png')
    pic2=os.path.join(app.config['UPLOAD_FOLDER'],'trainSentiments.png')
    pic3=os.path.join(app.config['UPLOAD_FOLDER'],'trainSentiRating.png')
    pic4=os.path.join(app.config['UPLOAD_FOLDER'],'testDataset.png')
    pic5=os.path.join(app.config['UPLOAD_FOLDER'],'testSentiments.png')
    pic6=os.path.join(app.config['UPLOAD_FOLDER'],'testSentiPercent.png')
    pic7=os.path.join(app.config['UPLOAD_FOLDER'],'testSentiPie.png') 
    pic8=os.path.join(app.config['UPLOAD_FOLDER'],'try3.webp') 

    return render_template('visualizer.html',trainDs=pic1,trainSenti=pic2,trainSentiRating=pic3,testDs=pic4,testSenti=pic5,testPercent=pic6,testPie=pic7,bgImg=pic8)

@app.route('/predictor', methods=['POST'])
def predict():
    pic12=os.path.join(app.config['UPLOAD_FOLDER'],'try4.jpg')
    text = request.form['text']
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text))))['compound']

    if(score > 0):
        label = 'This sentence is positive 😊'
    elif(score == 0):
        label = 'This sentence is neutral 😐'
    else:
        label = 'This sentence is negative ☹️'

    return render_template('predictor1.html', variable=label,bgIm=pic12)

if __name__ == "__main__":
    app.run(port='8089', threaded=False, debug=True)
    