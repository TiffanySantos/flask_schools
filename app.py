from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# URI is uniform resource identifier whereas URL is uniform resource locator (it is an unstance of a URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
db = SQLAlchemy(app)
# tell SQLAlchemy to reflect the columns that already exist in the table
db.Model.metadata.reflect(db.engine)

class School(db.Model):
    __tablename__ = 'schools-geocoded'
    __table_args__ = { 'extend_existing': True }
    LOC_CODE = db.Column(db.Text, primary_key=True) 


@app.route("/")
def index():
  # SQLAlchemy 'translates' your python to an SQL query
  school_count = School.query.count()   
  schools = School.query.all()
  return render_template("index.html", count=school_count, schools=schools, location="New York City")

@app.route('/schools/<slug>')
def detail(slug):
    school = School.query.filter_by(LOC_CODE=slug).first()
    return render_template("detail.html", school=school)

@app.route('/city')
def city_list():
  cities = School.query.with_entities(School.city).distinct().all()
  cities =[city[0].title() for city in cities]
  cities = sorted(list(set(cities)))
  return render_template("city.html", cities=cities)

@app.route('/city/<cityname>')
def city(cityname):
  cityname = cityname.replace("-", " ")
  schools = School.query.filter_by(city=cityname.upper()).all()
  return render_template("index.html", schools=schools, count=len(schools), location=cityname)

@app.route("/zip/<zipcode>")
def zip(zipcode):
  schools = School.query.filter_by(ZIP=zipcode).all()
  return render_template("index.html", schools=schools, count=len(schools), location=zipcode)


  if __name__ == '__main__':
    app.run(debug=True)

# to run the app in terminal type:
# $ python3 -m flask run
