import khaiii
from flask import Flask, jsonify, request

app = Flask(__name__)
api = khaiii.KhaiiiApi()
api.open()


def get_nouns(s):
    words = api.analyze(s)
    nouns = [m.lex for word in words
             for m in word.morphs
             if "NN" in m.tag]
    return nouns


@app.route("/nouns", methods=['GET', 'POST'])
def nouns():
    if request.method == 'POST':
        payload = request.get_json()
        query = payload['query']
    else:
        query = request.args.get('query')
    results = get_nouns(query)
    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
