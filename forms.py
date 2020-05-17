from datetime import datetime
from flask_wtf import Form,FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired, AnyOf, URL,ValidationError,InputRequired,Length
import urllib.request
from urllib.parse import urlparse


from app import *
class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
        
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
    )

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
class ShowFormNew(Form):
    artist_id = StringField(
        'artist_id',validators=[DataRequired()]
    )
    venue_id = StringField(
        'venue_id',validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )
    def validate_artist_id(self,artist_id):
        if not(Artist.query.get(artist_id.data)):
            raise ValidationError("Invalid artist ID")
        
    def validate_venue_id(self,venue_id):
        if not(Venue.query.get(venue_id.data)):
            raise ValidationError("Invalid venue ID")


class ArtistFormNew(Form):
    name = StringField(
        'name', validators=[DataRequired(),Length(max=60)]
    )
    city = StringField(
        'city', validators=[DataRequired(),Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            (None,'Select a state'),
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link',
        validators=[Length(max=500)]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    website=StringField(
        'website',
        validators=[Length(max=120)]
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link',
        validators=[Length(max=120)]
    )
    seeking_venue=BooleanField(
        "seeking_venue",
        
    )
    seeking_description=TextAreaField(
        "seeking_description",
        validators=[Length(max=500)]

    )
    submit_button=SubmitField("List Artist")
    def validate_phone(self,phone):
        
        if (len(phone.data)!=12):
            raise ValidationError("Invalid phone number")
            
        for i in range(len(phone.data)):
            if i in [3,7]:
                if (phone.data[i]!="-"):
                    raise ValidationError("Invalid phone number")
            else:
                if not(phone.data[i].isdigit()):
                    raise ValidationError("Invalid phone number")
    def validate_facebook_link(self,facebook_link):
        if facebook_link.data=="":
            return
        parse=urlparse(facebook_link.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")        
    def validate_image_link(self,image_link):
        if image_link.data=="":
            return
        parse=urlparse(image_link.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")
    def validate_website(self,website):
        if website.data=="":
            return
        parse=urlparse(website.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")                     
    def validate_seeking_description(self,seeking_description):
        if(self.seeking_venue.data):
            if(seeking_description.data.strip()==""):
                raise ValidationError("Invalid description")
    def validate_name(self,name):
        query=Artist.query.filter_by(name=name.data).all()
        if(query):
            raise ValidationError("This name already exists")

class ArtistFormEdit(Form):
    name = StringField(
        'name', validators=[DataRequired(),Length(max=60)]
    )
    city = StringField(
        'city', validators=[DataRequired(),Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            (None,'Select a state'),
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link',
        validators=[Length(max=500)]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    website=StringField(
        'website',
        validators=[Length(max=120)]
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link',
        validators=[Length(max=120)]
    )
    seeking_venue=BooleanField(
        "seeking_venue",
        
    )
    seeking_description=TextAreaField(
        "seeking_description",
        validators=[Length(max=500)]

    )
    submit_button=SubmitField("List Artist")
    def validate_phone(self,phone):
        
        if (len(phone.data)!=12):
            raise ValidationError("Invalid phone number")
            
        for i in range(len(phone.data)):
            if i in [3,7]:
                if (phone.data[i]!="-"):
                    raise ValidationError("Invalid phone number")
            else:
                if not(phone.data[i].isdigit()):
                    raise ValidationError("Invalid phone number")
    def validate_facebook_link(self,facebook_link):
        if facebook_link.data=="":
            return
        parse=urlparse(facebook_link.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")            
    def validate_image_link(self,image_link):
        if image_link.data=="":
            return
        parse=urlparse(image_link.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")
    def validate_website(self,website):
        if website.data=="":
            return
        parse=urlparse(website.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")                      
    def validate_seeking_description(self,seeking_description):
        if(self.seeking_venue.data):
            if(seeking_description.data.strip()==""):
                raise ValidationError("Invalid description")


class VenueFormNew(Form):
    name = StringField(
        'name', validators=[DataRequired(),Length(max=60)]
    )
    city = StringField(
        'city', validators=[DataRequired(),Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            (None,'Select a state'),
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    address = StringField(
        'address', validators=[DataRequired(),Length(max=120)]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link',
        validators=[Length(max=500)]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    website=StringField(
        'website',
        validators=[Length(max=120)]
    )
    facebook_link = StringField(
        'facebook_link',
        validators=[Length(max=120)]
    )
    seeking_talent=BooleanField(
        "seeking_talent",
        
    )
    seeking_description=TextAreaField(
        "seeking_description",
        validators=[Length(max=500)]

    )
    def validate_phone(self,phone):
        
        if (len(phone.data)!=12):
            raise ValidationError("Invalid phone number")
            
        for i in range(len(phone.data)):
            if i in [3,7]:
                if (phone.data[i]!="-"):
                    raise ValidationError("Invalid phone number")
            else:
                if not(phone.data[i].isdigit()):
                    raise ValidationError("Invalid phone number")
    def validate_facebook_link(self,facebook_link):
        if facebook_link.data=="":
            return
        parse=urlparse(facebook_link.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")
        
            
    def validate_image_link(self,image_link):
        if image_link.data=="":
            return
        parse=urlparse(image_link.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")
    def validate_website(self,website):
        if website.data=="":
            return
        parse=urlparse(website.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")                     
    def validate_seeking_description(self,seeking_description):
        if(self.seeking_talent.data):
            if(seeking_description.data.strip()==""):
                raise ValidationError("Invalid description")
    def validate_name(self,name):
        query=Artist.query.filter_by(name=name.data).all()
        if(query):
            raise ValidationError("This name already exists")        

class VenueFormEdit(Form):
    name = StringField(
        'name', validators=[DataRequired(),Length(max=60)]
    )
    city = StringField(
        'city', validators=[DataRequired(),Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            (None,'Select a state'),
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    address = StringField(
        'address', validators=[DataRequired(),Length(max=120)]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link',
        validators=[Length(max=500)]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    website=StringField(
        'website',
        validators=[Length(max=120)]
    )
    facebook_link = StringField(
        'facebook_link',
        validators=[Length(max=120)]
    )
    seeking_talent=BooleanField(
        "seeking_talent",
        
    )
    seeking_description=TextAreaField(
        "seeking_description",
        validators=[Length(max=500)]

    )
    def validate_phone(self,phone):
        
        if (len(phone.data)!=12):
            raise ValidationError("Invalid phone number")
            
        for i in range(len(phone.data)):
            if i in [3,7]:
                if (phone.data[i]!="-"):
                    raise ValidationError("Invalid phone number")
            else:
                if not(phone.data[i].isdigit()):
                    raise ValidationError("Invalid phone number")
    def validate_facebook_link(self,facebook_link):
        if facebook_link.data=="":
            return
        parse=urlparse(facebook_link.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")        
    def validate_image_link(self,image_link):
        if image_link.data=="":
            return
        parse=urlparse(image_link.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")
    def validate_website(self,website):
        if website.data=="":
            return
        parse=urlparse(website.data)    
        if(parse.scheme=="" or parse.netloc==""):
            raise ValidationError("Invalid URL")                     
    def validate_seeking_description(self,seeking_description):
        if(self.seeking_talent.data):
            if(seeking_description.data.strip()==""):
                raise ValidationError("Invalid description")

                
    
    
