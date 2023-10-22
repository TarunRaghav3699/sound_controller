from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize song state
current_volume = 50

@app.route('/')
def index():
    return render_template('index.html', volume=current_volume)

@app.route('/update_volume', methods=['POST'])
def update_volume():
    global current_volume
    new_volume = int(request.form['volume'])
    current_volume = new_volume
    return 'Volume updated successfully'

if __name__ == '__main__':
    app.run(debug=True)
