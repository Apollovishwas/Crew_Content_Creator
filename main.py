
from flask import Flask, request, jsonify
import re
from crew_pipeline import run_start_crew


app = Flask(__name__)
def convert_html_to_text(html):
    # Remove HTML tags using regular expressions
    return re.sub(r'<[^>]+>', '', html).strip()
@app.route('/', methods=['GET'])
def home():
    return "The server is online", 200
@app.route('/webhook', methods=['POST'])
def webhook():

    # Parse the incoming JSON data
    data = request.get_json()
    # Extract product title
    product_title = data.get('title', 'No title available')
    # Extract product description in HTML and convert it to plain text
    html_description = data.get('body_html', 'No description available')
    plain_text_description = convert_html_to_text(html_description)
    # Extract product price from the first variant
    product_price = data['variants'][0].get('price', 'No price available') if data.get('variants') else 'No price available'
    # Create a formatted string with product information
    product_info = f'"Description":"{plain_text_description}", "Product name":"{product_title}", "Product price":"{product_price}"'
    # Extract image URL
    image_url = data['images'][0].get('src', 'No image available') if data.get('images') else 'No image available'






    # Print extracted information
    print("Product Info:", product_info)
    print("Image URL:", image_url)

    result = run_start_crew(product_info, image_url)



    # Respond with a success message
    return jsonify({"status": "success", "result": result}), 200
if __name__ == '__main__':
    app.run(port=5000)