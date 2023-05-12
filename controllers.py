from flask import render_template, request

from app import app
from models import *
from forms import *


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    all_data = request.form
    print(all_data)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = all_data)
        print(form.validate_on_submit())
        if form.validate_on_submit():
            contactinfo = ContactUs(full_name = form.full_name.data, email = form.email.data, phone = form.phone.data, comment = form.comment.data)
            contactinfo.save()
    return render_template('contact.html', form = form)


@app.route('/recmovie', methods = ['GET', 'POST'])
def recmovie():
    all_data = request.form
    print(all_data)
    form = RecMovieForm()
    if request.method == 'POST':
        form = RecMovieForm(data = all_data)
        print(form.validate_on_submit())
        if form.validate_on_submit():
            recmovie1 = RecMovie(movie_name = form.movie_name.data, producer = form.producer.data, year = form.year.data, your_point = form.your_point.data)
            recmovie1.save()
    return render_template('recmovie.html', form = form)


@app.route('/movie/<int:id>')
def movie(id):
    movie = Movie.query.filter_by(id=id).first()
    if movie:
        producer = Producer.query.filter_by(id=movie.producer_id).first()
        return render_template('movie.html', movie=movie, producer=producer)
    else:
        return 'Film yoxdur!'


@app.route('/movies/')
def movies():
    movies = Movie.query.filter_by(status=True).all()
    if movies:
        return render_template('movies.html', movies=movies)
    else:
        return 'Filmler yoxdur!'
