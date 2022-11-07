# Projecy 4: Web scraping

## The project is created with:
* Python version: 3.7.6
  * requests (installation: python3 -m pip install requests)
  * beautifulsoup4 (installation: python3 -m pip install beautifulsoup4)
  * numpy
  * matplotlib


## How to run the code:
Open terminal window, these commands compile and execute the programs:
```
# To make a request for a url from a given website (Task 1):
python3 requesting_urls.py

# To find all url links and all wiki articles (only) in a html text (Task 2 and 3):
python3 filter_urls.py

# To find all dates in a text (Task 4):
python collect_dates.py

# To extract data from an already-found table tag and return a schedule (Task 5-7):
python time_planner.py

# To find the best players in the semifinals of the NBA and provide plots of the top 3 players in all teams (Task 8-10):
python fetch_player_statistics.py

# To test all the above implementations at once:
pytest

Specifications of urls, HTML text and other variables has to be done
directly in the differnt files.

NOTE:
# The test test_filter_urls.py has been modified so that it accepts paths that start with w
# For the implementation to pass the tests in test_fetch_player_statistics.py one has to
  change the variable 'project_path' in fetch_player_statistics to the current directory 



