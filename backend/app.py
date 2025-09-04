from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        event_type = request.form['event']
        print(f"Booking received: {name} - {event_type}")
        return "Booking received!"
    return render_template('booking_form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
