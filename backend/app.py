from flask import Flask, render_template, request, redirect
from models import Booking, engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, template_folder='../templates', static_folder='../static')
Session = sessionmaker(bind=engine)

@app.route('/')
def home():
    session = Session()
    all_bookings = session.query(Booking).all()
    return render_template('index.html', bookings=all_bookings)

@app.route('/book', methods=['GET', 'POST'])
def book():
    session = Session()
    if request.method == 'POST':
        name = request.form['name']
        event_type = request.form['event']
        booking = Booking(name=name, event_type=event_type)
        session.add(booking)
        session.commit()
        return redirect('/bookings')  # 👈 Redirect after saving
    return render_template('booking_form.html')

@app.route('/bookings')
def view_bookings():
    session = Session()
    all_bookings = session.query(Booking).all()
    return render_template('bookings.html', bookings=all_bookings)

@app.route('/delete/<int:id>')
def delete_booking(id):
    session = Session()
    booking = session.query(Booking).get(id)
    if booking:
        session.delete(booking)
        session.commit()
    return redirect('/bookings')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_booking(id):
    session = Session()
    booking = session.query(Booking).get(id)
    if request.method == 'POST':
        booking.name = request.form['name']
        booking.event_type = request.form['event']
        session.commit()
        return redirect('/bookings')
    return render_template('edit_form.html', booking=booking)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
