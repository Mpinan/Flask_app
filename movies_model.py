class Movies(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(80), unique=True)
    # email = db.Column(db.String(120), unique=True)

    def __init__(self, film_name, img_url, release_year, summary, director, genre, rating, film_runtime, meta_score):
        self.film_name = film_name
        self.img_url = img_url
        self.release_year = release_year
        self.summary = summary
        self.director = director
        self.genre = genre
        self.rating = rating
        self.film_runtime = film_runtime
        self.meta_score = meta_score


    # def __repr__(self):
    #     return '<User %r>' % self.username

    @property
    def get_movies(self):
        return {
        'film_id' : self.film_id, 
        'film_name' : self.film_name, 
        'img_url' : self.img_url, 
        'release_year' : self.release_year, 
        'summary' : self.summary, 
        'director' : self.director, 
        'genre' : self.genre, 
        'rating' : self.rating, 
        'film_runtime' : self.film_runtime, 
        'meta_score' : self.meta_score
       }
