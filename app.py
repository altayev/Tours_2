from flask import Flask, render_template
from data import title, subtitle, description, departures, tours


app = Flask(__name__)


@app.route('/')
def render_index():
	return render_template(
		'index.html',
		title=title,
		subtitle=subtitle,
		description=description,
		departures=departures,
		tours=tours,
	)


@app.route('/departures/<departure>/')
def render_departures(departure):
	dep_city = departures[departure].replace("Из", "из")
	tours_from_departure = []
	for num, tour in tours.items():
		if tour["departure"] == departure:
			tour["id"] = num
			tours_from_departure.append(tour)
	return render_template(
		'departure.html',
		title=title,
		departures=departures,
		dep_city=dep_city,
		tours=tours_from_departure,
	)


@app.route('/tours/<id>/')
def render_tours(id):
	tour = tours[int(id)]
	hotel_stars = int(tour['stars'])*'★'
	subtitle = f'{tour["country"]} {departures[tour["departure"]]} {tour["nights"]} ночей'
	return render_template(
		'tour.html',
		title=title,
		departures=departures,
		tour=tour,
		hotel_stars=hotel_stars,
		subtitle=subtitle,
	)


if __name__ == '__main__':
    app.run()
