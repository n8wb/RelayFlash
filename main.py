from flask import Flask
import PiRelay


r1 = PiRelay.Relay("RELAY1")
r2 = PiRelay.Relay("RELAY2")
r3 = PiRelay.Relay("RELAY3")
r4 = PiRelay.Relay("RELAY4")
app = Flask(__name__)

@app.route('/off/<_id>')
def off(_id):
	PiRelay.Relay("RELAY"+_id).off()

@app.route('/on/<_id>')
def on(_id):
	PiRelay.Relay("RELAY"+_id).on()


if __name__ == '__main__':
    app.run()