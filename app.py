from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY_HERE'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    data = request.get_json()
    message = data['message']
    
    try:
        # Send the message to OpenAI's API and receive the response using the new API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        # Assuming the structure of the response object fits this; adjust as necessary.
        response_text = response['choices'][0]['message']['content'] if response['choices'] else 'Failed to generate response.'
        
        # Return the response as JSON
        return jsonify({"content": response_text})
    except Exception as e:
        return jsonify({"error": str(e), "content": "An error occurred processing your request."})

if __name__ == '__main__':
    app.run(debug=True)
