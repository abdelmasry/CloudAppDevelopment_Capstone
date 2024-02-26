from cloudant.client import Cloudant
from cloudant.query import Query
from flask import Flask, abort, jsonify, request
from utils import load_credentials
import atexit

# Add your Cloudant service credentials here
credentials: dict = load_credentials("./Config/Cloudant.json")
cloudant_username = credentials["cloudant_username"]
cloudant_api_key = credentials["apiKey"]
cloudant_url = credentials["url"]
client = Cloudant.iam(cloudant_username, cloudant_api_key, connect=True, url=cloudant_url)

session = client.session()
print('Databases:', client.all_dbs())

db = client['reviews']

app = Flask(__name__)
gen_id = 1000


@app.route('/api/get_reviews', methods=['GET'])
def get_reviews():
    dealership_id = request.args.get('id')

    # Check if "id" parameter is missing
    if dealership_id is None:
        return jsonify({"error": "Missing 'id' parameter in the URL"}), 400

    # Convert the "id" parameter to an integer (assuming "id" should be an integer)
    try:
        dealership_id = int(dealership_id)
    except ValueError:
        return jsonify({"error": "'id' parameter must be an integer"}), 400

    # Define the query based on the 'dealership' ID
    selector = {
        'dealership': dealership_id
    }

    # Execute the query using the query method
    result = db.get_query_result(selector)

    # Create a list to store the documents
    data_list = []

    # Iterate through the results and add documents to the list
    for doc in result:
        data_list.append(doc)

    # Return the data as JSON
    return jsonify(data_list)


@app.route('/api/post_review', methods=['POST'])
def post_review():
    if not request.json:
        return 'Invalid JSON data'

    # Extract review data from the request JSON
    review_data = request.json

    # Validate that the required fields are present in the review data
    required_fields = ['name', 'dealership', 'review', 'purchase']
    for field in required_fields:
        if field not in review_data:
            return f'Missing required field: {field}'
    
    # this actually fucking worked
    idd = gen_id + 1
    review_data["id"] = idd
    review_data["purchase_date"] = None
    review_data["car_make"] = "None"
    review_data["car_year"] = "None"
    review_data["car_model"] = "None"
    
    # Save the review data as a new document in the Cloudant database
    db.create_document(review_data)

    return jsonify({"message": "Review posted successfully"}), 201


if __name__ == '__main__':
    app.run(port=5000, debug=True)