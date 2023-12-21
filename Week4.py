import requests

class TheMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = ""

    def getPopulars(self):
        response = requests.get(
            f"{self.api_url}/discover/movie?api_key={self.api_key}&include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc")
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Instantiate the class outside the class definition
movieApi = TheMovieDb()
while True:
    secim = input("1- Popular Movies\n2- Exit\nChoice: ")
    if secim == "2":
        break
    elif secim == "1":
        result = movieApi.getPopulars()
        if result and "results" in result:
            for movie in result["results"]:
                print(f"Title: {movie['title']}")
                print(f"Release Date: {movie['release_date']}")
                print("="*30)
        else:
            print("Failed to fetch popular movies.")
