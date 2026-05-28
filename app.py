from flask import Flask,render_template,jsonify
app = Flask(__name__)

JOBS = [
    {
        "id":1,
        "title":"Data Analyst",
        "location":"Banglore India",
        "salary":"Rs 10,0000"
    },
    {
        "id":2,
        "title":"Data Scientist",
        "location":"Delhi India",
        "salary":"Rs 15,00000"
    },
    {
        "id":3,
        "title":"Ai Engineer",
        "location":"Remote",
        "salary":"Rs 15,00000"
    },
    {
        "id":4,
        "title":"Fronted Engineer",
        "location":"San Francisco USA",
        "salary":"$ 12,000"
    }

]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)