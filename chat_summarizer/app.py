from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
app.secret_key="This_secret_key"
POSTS_PER_PAGE=5
    

@app.route("/home",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/RD",methods=['GET','POST'])
def RD():
    data_in_flask = request.get_json()
    print(data_in_flask)

    summary=summarizer(data_in_flask)
    print(summary)

    data={
        'data': f"{summary}"
    }
    print(data)
    return jsonify(data)    


@app.route("/news_feed/<int:page_num>", methods=['GET', 'POST'])
def news_feed(page_num):
    with open('unsummarized_news3.json', 'r') as fp:
        posts_data = json.load(fp)
        # Get the page number from the request, default to 1 if not provided
        #page_num = request.args.get('page', 1, type=int)
        
        # Calculate the starting and ending index for the posts on the requested page
        start_idx = (page_num - 1) * POSTS_PER_PAGE
        end_idx = start_idx + POSTS_PER_PAGE

        
        # Get the posts for the requested page
        news = posts_data[start_idx:end_idx]
        
        # Return the paginated posts as JSON or render the template with paginated data
        if request.method == 'GET':
            return render_template('news_feed.html', news=news, page_num=page_num,POSTS_PER_PAGE=POSTS_PER_PAGE)
        elif request.method == 'POST':
            return jsonify(news)


if __name__ == "__main__":

    def summarizer(input):
        output="This is a summary of the input text.\n" + str(input)
        return output
    app.run(debug=True)
    CORS(app)    
