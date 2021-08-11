import pandas as pd
from flask import Flask,jsonify,request
from flask_ngrok import run_with_ngrok

df = pd.read_csv('articles.csv')
df.rename( columns={'Unnamed: 0':'id'}, inplace=True )

all_articles  = df.values.tolist()

liked = []
not_liked = []

app = Flask(__name__)

run_with_ngrok(app)

@app.route('/articles')
def get_articles():
  return jsonify({
      'data'   : all_articles[0],
      'status' : 'success'
  })

@app.route('/liked',methods=['POST'])
def get_liked_movies():
  article = all_articles[0]
  data = all_articles[1:]
  liked.append(article)
  return jsonify({
      'status' : 'success'
  })

@app.route('/not_liked',methods=['POST'])
def get_not_liked_movies():
  article = all_articles[0]
  data = all_articles[1:]
  not_liked.append(article)
  return jsonify({
      'status' : 'success'
  })  

if __name__ == '__main__':
    app.run()
   