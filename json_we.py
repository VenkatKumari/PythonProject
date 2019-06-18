from urllib.request import urlopen
from bs4 import BeautifulSoup
from pathlib import Path
from IPython.core.display import clear_output
import pandas as pd


#note: this code runs with the output given by webscrapping data, variables used from webscrapping code


TopRating = pd.DataFrame({'Name': finname,
                             'Number of ratings': finrating})
print(TopRating.info())
TopRating.head(10)

output_jsonfile = 'movie_ratings.json'
output_jsondir = Path('json_output')
output_jsondir.mkdir(parents=True, exist_ok=True)

#toconvertfile(output_dir / output_file) 
TopRating.to_json(output_jsondir / output_jsonfile,orient="records",date_format="iso")
#topratingsconvertedtojsonfile




 


