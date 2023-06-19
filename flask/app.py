from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = ''
SEARCH_ENGINE_ID = ''

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'dorks' not in data:
            return {"error": "Missing 'dorks' in JSON data"}, 400

        start_index = data.get('start', 1)
        url = 'https://www.googleapis.com/customsearch/v1'
        all_results = []

        for term in data['dorks']:
            params = {
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID,
                'q': term,
                'start': start_index
            }
            response = requests.get(url, params=params)
            results = response.json().get('items', [])
            all_results.extend(results)

        return jsonify({"results": all_results})  # Returns a JSON response

    return render_template('index.html')  # Initial page load

if __name__ == "__main__":
    app.run(debug=True)
