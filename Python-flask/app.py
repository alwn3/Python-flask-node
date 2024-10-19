from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

    # Run the application
if __name__ == '__main__':
            # Make the application accessible from any IP (0.0.0.0)
    app.run(debug=True, host='0.0.0.0')

