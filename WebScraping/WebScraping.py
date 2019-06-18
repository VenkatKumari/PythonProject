from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

url = "https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=T37FEYMZGES115PEZPYK&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3"
url1 = "https://www.imdb.com/search/name?gender=male,female&ref_=nv_cel_m"
# Opening URL and managing errors
try:
    html = urlopen(url)
    html1 = urlopen(url1)
except HTTPError as e:
    print("The Server Returned an Error")
except URLError as e:
    print("The Server can't be found")

bs = BeautifulSoup(html.read(), "html.parser")
bs1 = BeautifulSoup(html1.read(), "html.parser")


def TopName(bs):
    TopRatedMovies = bs.find_all("td", "titleColumn", limit=20)
    for name in TopRatedMovies:
        finname = name.find("a")
        print(finname.get_text())

def TopYear(bs):
    TopRatedMoviesYears = bs.find_all("td", "titleColumn", limit=20)
    for year in TopRatedMoviesYears:
        finyear = year.find("span")
        print(finyear.get_text())

def TopRating(bs):
    TopRatedMoviesRatings = bs.find_all("td", "ratingColumn imdbRating",limit=20)
    for rating in TopRatedMoviesRatings:
        finrating = rating.find("strong")
        print(finrating.get_text())

def TopPosters(bs):
    TopRatedMoviesPosters = bs.find_all("td", "posterColumn", limit=20)
    for poster in TopRatedMoviesPosters:
        finposter = poster.a.img
        print (finposter.get("src"))

def TopCelebname(bs1):
    TopCelebName = bs1.find_all("h3", "lister-item-header", limit=20)
    for celebs in TopCelebName:
        celebname = celebs.a
        print(celebname.get_text())

def TopCelebDescription(bs1):
    TopCelebDescription = bs1.find_all("div", "lister-item-content", limit=20)
    for descr in TopCelebDescription:
        descriptions = descr.p
        print(descriptions.get_text())

def TopCelebImage(bs1):
    TopCelebImage = bs1.find_all("div", "lister-item-image", limit=20)
    for image in TopCelebImage:
        finimage = image.a.img
        print(finimage.get("src"))




