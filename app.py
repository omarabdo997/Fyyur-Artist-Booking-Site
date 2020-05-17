#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from forms import *
from sqlalchemy.sql import func
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate=Migrate(app,db)

# TODO: connect to a local postgresql database
# app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://omar:917356oo@localhost:5432/fyyurapp"

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60),nullable=False,unique=True)
    city = db.Column(db.String(120),nullable=False)
    state = db.Column(db.String(120),nullable=False)
    address = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(120),nullable=False)
    genres = db.Column(db.String(500),nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website=db.Column(db.String(120))
    seeking_talent=db.Column(db.Boolean,default=False)
    seeking_description=db.Column(db.String(500))
    shows=db.relationship("Show",backref="venue",lazy=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60),nullable=False,unique=True)
    city = db.Column(db.String(120),nullable=False)
    state = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(120),nullable=False)
    genres = db.Column(db.String(500),nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website=db.Column(db.String(120))
    seeking_venue=db.Column(db.Boolean,default=False)
    seeking_description=db.Column(db.String(500))
    shows=db.relationship("Show",backref="artist",lazy=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
  __tablename__="Show"

  id = db.Column(db.Integer, primary_key=True)
  date=db.Column(db.DateTime)
  artist_id=db.Column(db.Integer,db.ForeignKey("Artist.id",ondelete="CASCADE"),nullable=False)
  venue_id=db.Column(db.Integer,db.ForeignKey("Venue.id",ondelete="CASCADE"),nullable=False)

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  try:

    query=Venue.query.all()
    data=[]
    for q in query:
      num_upcoming_shows=0
      time=datetime.now()
      for show in q.shows:
        if(time<show.date):
          num_upcoming_shows+=1
      viewed=False
      for d in data:
        if(d["city"]== q.city and d["state"]==q.state):
          d["venues"].append({"id":q.id,"name":q.name,"num_upcoming_shows":num_upcoming_shows})
          viewed=True
          break
      if(viewed==False):
        data.append({"city":q.city,"state":q.state,"venues":[{"id":q.id,"name":q.name,"num_upcoming_shows":num_upcoming_shows}]})  
  
    return render_template('pages/venues.html', areas=data)
  except:
    flash("An error has occured!")
    return render('pages/home.html')  


@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  search=request.form.get("search_term")
  query=Venue.query.filter(Venue.name.ilike("%"+search+"%"))
  response={"count":query.count(),"data":[]}
  for q in query:
    num_upcoming_shows=0
    time=datetime.now()
    for show in q.shows:
      if(time<show.date):
        num_upcoming_shows+=1
    response["data"].append({"id":q.id,"name":q.name,"num_upcoming_shows":num_upcoming_shows})
  # response={
  #   "count": 1,
  #   "data": [{
  #     "id": 2,
  #     "name": "The Dueling Pianos Bar",
  #     "num_upcoming_shows": 0,
  #   }]
  # }
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id

  try:

    query=Venue.query.get(venue_id)
    shows=query.shows
    past_shows=[]
    upcoming_shows=[]
    time=datetime.now()
    print(time)
    for show in shows:
      if(time>show.date):
        past_shows.append({
          "artist_id":show.artist.id,
          "artist_name":show.artist.name,
          "artist_image_link":show.artist.image_link,
          "start_time":str(show.date)
        })
      else:
        upcoming_shows.append({
          "artist_id":show.artist.id,
          "artist_name":show.artist.name,
          "artist_image_link":show.artist.image_link,
          "start_time":str(show.date)
        })


    data={
      "id": query.id,
      "name": query.name,
      "genres": query.genres.split(","),
      "address": query.address,
      "city": query.city,
      "state": query.state,
      "phone": query.phone,
      "website": query.website,
      "facebook_link": query.facebook_link,
      "seeking_talent": query.seeking_talent,
      "seeking_description": query.seeking_description,
      "image_link": query.image_link,
      "past_shows": past_shows,
      "upcoming_shows": upcoming_shows,
      "past_shows_count": len(past_shows),
      "upcoming_shows_count": len(upcoming_shows),
    }
    return render_template('pages/show_venue.html', venue=data)
  except:
    return render_template('errors/404.html')

  
  
  

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueFormNew()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  form = VenueFormNew()
  if(form.validate_on_submit()):
    
    error=False
    try:
      venue=Venue(
      name=request.form["name"],
      city=request.form["city"],
      state=request.form["state"],
      address=request.form["address"],
      image_link=request.form["image_link"],
      phone=request.form["phone"],
      genres=",".join(request.form.getlist("genres")),
      website=request.form["website"],
      facebook_link=request.form["facebook_link"],
      seeking_talent=(form.seeking_talent.data),
      seeking_description=request.form["seeking_description"]
      )
      db.session.add(venue)
      db.session.commit()
    except:
      db.session.rollback()
      error=True
    finally:
      if(error==False):
        # TODO: modify data to be the data object returned from db insertion
        db.session.refresh(venue)
        # on successful db insert, flash success
        flash('Venue ' + venue.name + ' was successfully listed '+'with ID: '+str(venue.id)+"!")
      else:
        # TODO: on unsuccessful db insert, flash an error instead.
        # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
        # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
        flash('An error occurred. Venue ' + venue.name + ' could not be listed.')
      return render_template('pages/home.html')
  
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/<venue_id>/delete', methods=['GET'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  venue=Venue()
  name=""
  error=False
  try:
    venue=Venue.query.get(venue_id)
    name=venue.name
    Venue.query.filter_by(id=venue_id).delete()
    db.session.commit()
  except:
    db.session.rollback()
    error=True
  finally:
    if(error==False):
      flash("Venue "+name+" was successfully deleted!")
    else:
      flash("An error occured. Venue "+name+" could not be deleted!")
    return render_template('pages/home.html')       
    

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  try:

    query=Artist.query.all()
    data=[]
    for q in query:
      data.append({"id":q.id,"name":q.name})
    return render_template('pages/artists.html', artists=data)
  except:
    flash("An error has occured!")
    return render_template('pages/home.html')  

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  search=request.form.get('search_term')
  query=Artist.query.filter(Artist.name.ilike("%"+search+"%"))
  
  response={"count":query.count() ,"data": []}
  for q in query.all():
    num_upcoming_shows=0
    time=datetime.now()
    for show in q.shows:
      if(time<show.date):
        num_upcoming_shows+=1
    response["data"].append({"id":q.id,"name":q.name,"num_upcoming_shows":num_upcoming_shows})
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  try:
    query=Artist.query.get(artist_id)
    shows=query.shows
    past_shows=[]
    upcoming_shows=[]
    time=datetime.now()
    print(time)
    for show in shows:
      if(time>show.date):
        past_shows.append({
          "venue_id":show.venue.id,
          "venue_name":show.venue.name,
          "venue_image_link":show.venue.image_link,
          "start_time":str(show.date)
        })
      else:
        upcoming_shows.append({
          "venue_id":show.venue.id,
          "venue_name":show.venue.name,
          "venue_image_link":show.venue.image_link,
          "start_time":str(show.date)
        })
    data={
      "id": query.id,
      "name": query.name,
      "genres": query.genres.split(","),
      "city": query.city,
      "state": query.state,
      "phone": query.phone,
      "website": query.website,
      "facebook_link": query.facebook_link,
      "seeking_venue": query.seeking_venue,
      "seeking_description": query.seeking_description,
      "image_link": query.image_link,
      "past_shows": past_shows,
      "upcoming_shows": upcoming_shows,
      "past_shows_count": len(past_shows),
      "upcoming_shows_count": len(upcoming_shows),
    }
    
    return render_template('pages/show_artist.html', artist=data)
  except:
    return render_template('errors/404.html')  

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistFormEdit()
  try:

    artist=Artist.query.get(artist_id)
    
    # TODO: populate form with fields from artist with ID <artist_id>
    form.name.data=artist.name
    form.city.data=artist.city
    form.state.data=artist.state
    form.genres.data=artist.genres.split(",")
    form.phone.data=artist.phone
    form.website.data=artist.website
    form.facebook_link.data=artist.facebook_link
    form.seeking_venue.data=artist.seeking_venue
    form.seeking_description.data=artist.seeking_description
    form.image_link.data=artist.image_link
    return render_template('forms/edit_artist.html', form=form, artist=artist)
  except:
    return render_template('errors/404.html')  

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
  form = ArtistFormEdit()
  artist=Artist.query.get(artist_id)
  if(form.validate_on_submit()):
    print(form.state.errors)
    error=False
    try:
      
      artist.name=request.form["name"]
      artist.city=request.form["city"]
      artist.state=request.form["state"]
      artist.image_link=request.form["image_link"]
      artist.phone=request.form["phone"]
      artist.genres=",".join(request.form.getlist("genres"))
      artist.website=request.form["website"]
      artist.facebook_link=request.form["facebook_link"]
      artist.seeking_venue=(form.seeking_venue.data)
      artist.seeking_description=request.form["seeking_description"]
      
      db.session.commit()
    except:
      db.session.rollback()
      error=True
    finally:
      if(error==False):
        
        flash('Artist ' + artist.name + ' was successfully edited!')
      else:
        print(artist.genres)
        flash('An error occurred. Artist ' + artist.name + ' could not be edited.')
      return redirect(url_for('show_artist', artist_id=artist_id))

    
    
  return render_template('forms/edit_artist.html', form=form, artist=artist)  

  

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueFormEdit()
  try:

    venue=Venue.query.get(venue_id)
    
    # TODO: populate form with values from venue with ID <venue_id>
    form.name.data=venue.name
    form.city.data=venue.city
    form.state.data=venue.state
    form.address.data=venue.address
    form.genres.data=venue.genres.split(",")
    form.phone.data=venue.phone
    form.website.data=venue.website
    form.facebook_link.data=venue.facebook_link
    form.seeking_talent.data=venue.seeking_talent
    form.seeking_description.data=venue.seeking_description
    form.image_link.data=venue.image_link
    return render_template('forms/edit_venue.html', form=form, venue=venue)
  except:
    return render_template('errors/404.html')  

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
 
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  form = VenueFormEdit()
  venue=Venue.query.get(venue_id)
  if(form.validate_on_submit()):
    print(form.state.errors)
    error=False
    try:
      
      venue.name=request.form["name"]
      venue.city=request.form["city"]
      venue.state=request.form["state"]
      venue.address=request.form["address"]
      venue.image_link=request.form["image_link"]
      venue.phone=request.form["phone"]
      venue.genres=",".join(request.form.getlist("genres"))
      venue.website=request.form["website"]
      venue.facebook_link=request.form["facebook_link"]
      venue.seeking_talent=(form.seeking_talent.data)
      venue.seeking_description=request.form["seeking_description"]
      
      db.session.commit()
    except:
      db.session.rollback()
      error=True
    finally:
      if(error==False):
        
        flash('Venue ' + venue.name + ' was successfully edited!')
      else:
        
        flash('An error occurred. Venue ' + venue.name + ' could not be edited.')
      return redirect(url_for('show_venue', venue_id=venue_id))


  return render_template('forms/edit_venue.html', form=form, venue=venue)      


#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistFormNew()

  print("failed")
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():

  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Artist record in the db, instead
  
  form = ArtistFormNew()
  if(form.validate_on_submit()):
    print(form.state.errors)
    error=False
    try:
      artist=Artist(
      name=request.form["name"],
      city=request.form["city"],
      state=request.form["state"],
      image_link=request.form["image_link"],
      phone=request.form["phone"],
      genres=",".join(request.form.getlist("genres")),
      website=request.form["website"],
      facebook_link=request.form["facebook_link"],
      seeking_venue=(form.seeking_venue.data),
      seeking_description=request.form["seeking_description"]
      )
      db.session.add(artist)
      db.session.commit()
    except:
      db.session.rollback()
      error=True
    finally:
      if(error==False):
        # TODO: modify data to be the data object returned from db insertion
        db.session.refresh(artist)
        # on successful db insert, flash success
        flash('Artist ' + artist.name + ' was successfully listed '+'with ID: '+str(artist.id)+"!")
      else:
        print(artist.genres)
        # TODO: on unsuccessful db insert, flash an error instead.
        # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
        flash('An error occurred. Artist ' + artist.name + ' could not be listed.')
      return render_template('pages/home.html')

    
    
    
    
  return render_template('forms/new_artist.html', form=form)  


  


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  try:

    data=[]
    query=Show.query.all()
    for q in query:
      print(q.date)
      data.append({
        "venue_id":q.venue.id,
        "venue_name":q.venue.name,
        "artist_id":q.artist.id,
        "artist_name":q.artist.name,
        "artist_image_link": q.artist.image_link,
        "start_time":str(q.date)

      })
    return render_template('pages/shows.html', shows=data)
  except:
    flash("An error has occured!")
    return render_template('pages/home.html')  

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowFormNew()
  #ShowFormNew handels wrong id inputs
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  # on successful db insert, flash success
  
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  form = ShowFormNew()
  if(form.validate_on_submit()):
    error=False
    try:

      show=Show(date=request.form["start_time"])
      artist=Artist.query.get(request.form["artist_id"])
      venue=Venue.query.get(request.form["venue_id"])
      show.artist=artist
      show.venue=venue
      db.session.add(show)
      db.session.commit()
    except:
      db.session.rollback()
      error=True
    finally:
      if(error==False):
        flash('Show was successfully listed!')
      else:
         flash('An error occurred. Show could not be listed.')
      return render_template('pages/home.html')

  return render_template('forms/new_show.html', form=form)
  
  

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
