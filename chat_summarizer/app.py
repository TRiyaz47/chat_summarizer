from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from flask_cors import CORS

app = Flask(__name__)
app.secret_key="This_secret_key"


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


if __name__ == "__main__":

    def summarizer(input):
        output="This is a summary of the input text.\n" + str(input)
        return output


    app.run(debug=True)
    CORS(app)    
