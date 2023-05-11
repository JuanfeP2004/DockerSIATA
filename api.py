import flask
import pandas as pd

app = flask.Flask(__name__)

@app.route('/mostrarEstacionesNivel')
def mostrarEstacionesNivel():
	data = flask.request.args
	url = "http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json"
	capturaWeb = pd.read_json(url, convert_dates=True)
	if data['pass'] == 'orlios':
		print(capturaWeb)
		return capturaWeb.to_dict()
	else:
		return "no puede ver el json parce"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
