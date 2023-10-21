from flask import Flask, render_template

app = Flask(__name__)

# Define the route that will serve the image
@app.route('/')
def show_image():
    return render_template('image.html')

if __name__ == '__main__':
    app.run()

