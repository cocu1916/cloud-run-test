import os
from flask import Flask

app = Flask(__name__)

def load_model():
    with open('cloud.pickle', 'rb') as f:
        clf_loaded = pickle.load(f)
    return clf_loaded

@app.route('/predict', methods=['POST'])
def url():
    """Expects a list of urls. """
    url = request.get_json()
    rev_url_list = re.split(r"://", url).str[-1]
    for i, url in enumerate(url_list):
        if url[len(url)-1] != "/":
            url_list[i] = url + "/"
    print(url_list)
    prediction = model.predict([[url_list]])
    print
    response_object['prediction'] = prediction.tolist()[0][1]
    return jsonify(url_list)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors. """
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

{
  timestamp: int(datetime.datetime.now().timestamp()),
  predictions: [
    {
      url: url_list[0],
      prediction: predictions[0]
    },
    {
      url: url_list[1],
      prediction: predictions[1]
    },
    # ... one for each posted URL
    {
      url: url_list[2],
      prediction: predictions[2]
    },
  ]
}
