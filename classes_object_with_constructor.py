"""
**Create a Class with a Constructor**:
   - Write a class `Movie` with attributes `title` and `rating` using the `__init__()` constructor.
   - Define a method to display the movie’s title and rating.
"""
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
    def display(self):
        print(f"{self.title} Movie has {self.rating} Ratings") 

movie1 = Movie("KGF",9.7)
movie2 = Movie("RRR",9.5)

movie1.display()
movie2.display()