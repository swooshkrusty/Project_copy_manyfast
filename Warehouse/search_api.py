import boto3
from flask import Flask, request, render_template, jsonify, jsonify, redirect
import os

# Initialize AWS Rekognition client
rekognition_client = boto3.client(
    "rekognition",
    aws_access_key_id="AKIA4YKSACLLQX7DS5QH",
    aws_secret_access_key="KKF2YrnW9t6yC3XfU2FkSnilKo4pwAmUGxhfAin+",
    region_name="us-west-2",  # Replace with your actual region
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("search.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" in request.files:
        image = request.files["image"]
        image_path = os.path.join(os.getcwd(), image.filename)
        image.save(image_path)

        # Now that we have the image saved, let's send it to Rekognition
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        # Call AWS Rekognition to analyze the image
        response = rekognition_client.detect_labels(Image={"Bytes": image_bytes})

        # Process the response to extract information
        labels = response["Labels"]

        # Return the JSON response received from Rekognition
        return jsonify(labels)
        if labels:
            # Assume the first label is the primary one
            primary_label = labels[0]["Name"]
            # Replace spaces with '+' for URL encoding
            search_query = primary_label.replace(" ", "+")
            # Construct the search URL for Amazon
            search_url = f"https://www.amazon.com/s?k={search_query}"
            return redirect(search_url)

        return jsonify({"error": "No labels detected"})

    return "No image found to upload."


if __name__ == "__main__":
    app.run(debug=True)
