from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect

app = Flask (__name__)

database_file ="sqlite:///movies.db"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app);


class Movie(db.Model):
    title = db.Column(db.String(80) ,
            unique=True ,
            nullable=False ,
            primary_key=True)
    
    def _repr_(self):
        return "<Title: {}>".format(self.title)
    
   
db.create_all()

@app.route( "/" , methods=["GET" , "POST" ] )
def home():
    if request.form :                
            movie = Movie(title=request.form.get("title"))
            db.session.add(movie)
            db.session.commit()
    movies = Movie.query.all()
    return render_template("home1.html", movies=movies)



@app.route("/search", methods=["GET", "POST"])
def search():
    if request.form:
        searchname = request.form.get("searchname")
        print(searchname)
        movies = Movie.query.filter_by(title=searchname).limit(50).all()
    return render_template("home1.html", movies=movies)        

        
    
@app.route( "/update" , methods=["POST" ] )
def update():
   
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        movie = Movie.query.filter_by(title=oldtitle).first()
        movie.title=newtitle
        db.session.commit()
        return redirect("/")
    
    
    
@app.route( "/delete" , methods=["POST" ] )
def delete( ) :
    title = request.form.get("title" )
    movie = Movie.query.filter_by(title=title).first( )
    db.session.delete(movie )
    db.session.commit( )
    return redirect("/")



if __name__ == "__main__" :
    app.run(debug=True)