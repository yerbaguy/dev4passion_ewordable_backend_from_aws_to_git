from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_articles():
 return jsonify({"Hello":"World"})


 if __name__ == "__main__":

  # app.run(debug=True)
  # app.run(host='0.0.0.0', port=5000)
   app.run(host='0.0.0.0', port=5000)
