import os
import re
from operator import itemgetter
from typing import Dict, List
from urllib.parse import urljoin
import unicodedata

import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

from requesting_urls import get_html
from filter_urls import find_urls
from time_planner import strip_text

## --- Task 8, 9 and 10 --- ##

try:
    import requests_cache
except ImportError:
    print("install requests_cache to improve performance")
    pass
else:
    requests_cache.install_cache()


base_url = "https://en.wikipedia.org"
project_path = '/Users/Kamilla/Documents/IN4110/IN3110-kisuleba/assignment4'


def find_best_players(url: str) -> None:
    """Find the best players in the semifinals of the nba.

    This is the top 3 scorers from every team in semifinals.
    Displays plot over points, assists, rebounds

    arguments:
        - html (str) : html string from wiki basketball
    returns:
        - None
    """
    teams = get_teams(url)
    all_players = {team['name']: get_players(team['url']) for team in teams}

    # get player statistics for each player
    all_players_w_stats = {}
    for team, players in all_players.items():
        team_list = []
        for player in players:
            stats = get_player_stats(player['url'], team)
            team_list.append({**player, **stats})
        all_players_w_stats[team] = team_list

    # Select top 3 for each team by points:
    best_PPG = {}
    best_RPG = {}
    best_APG = {}
    for team, players in all_players_w_stats.items():
        # Sort and extract top 3 players in each category
        best_PPG[team] = top_three_players(players, 'points')
        best_RPG[team] = top_three_players(players, 'rebounds')
        best_APG[team] = top_three_players(players, 'assists')

    plot_best(best_PPG, stat="points")
    plot_best(best_APG, stat="assists")
    plot_best(best_RPG, stat="rebounds")


def top_three_players(players: List[Dict], key: str) -> List[Dict]:
    players_sorted = sorted(players, key=lambda player: player[key])
    top_three = players[-3:]
    return top_three


def plot_best(best: Dict[str, List[Dict]], stat: str = "points") -> None:
    """Plots a single stat for the top 3 players from every team.

    Arguments:
        best (dict) : dict with the top 3 players from every team
            has the form:

            {
                "team name": [
                    {
                        "name": "player name",
                        "points": 5,
                        ...
                    },
                ],
            }

            where the _keys_ are the team name,
            and the _values_ are lists of length 3,
            containing dictionaries about each player,
            with their name and stats.

        stat (str) : [points | assists | rebounds] which stat to plot.
            Should be a key in the player info dictionary.
    """

    count_so_far = 0
    all_names = []

    for team, players in best.items():
        # collect the points and name of each player on the team
        stats = []
        names = []
        for player in players:
            names.append(player["name"])
            stats.append(player[stat])

        # record all the names, for use later in x label
        all_names.extend(names)

        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team's players points,
        # with the team name as the label
        bars = plt.bar(x, stats, label=team)

    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # turn off gridlines
    plt.grid(False)
    plt.title(f"{stat} for top 3 players in all teams")
    print(f"Creating plot of {stat} for top 3 players in all teams")

    plt.tight_layout()
    fname = os.path.join(project_path, f"NBA_player_statistics/{stat}")
    plt.savefig(fname)
    plt.close()


def get_teams(url: str) -> list:
    """Extracts all the teams that were in the semi finals in nba

    arguments:
        - url (str) : url of the nba finals wikipedia page
    returns:
        teams (list) : list with all teams
            Each team is a dictionary of {'name': team name, 'url': team page
    """
    # Get the table
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Bracket").find_next("table")

    # find all rows in table
    rows = table.find_all("tr")
    rows = rows[2:]
    # maybe useful: identify cells that look like 'E1' or 'W5', etc.
    seed_pattern = re.compile(r"^[EW][1-8]$")



    team_links = {}  # dict of team name: team url
    in_semifinal = set()  # set of teams in the semifinal

    # Loop over every row and extract teams from semi finals
    # also locate the links tot he team pages from the First Round column
    for row in rows:
        cols = row.find_all("td")

        # quarterfinal, E1/W8 is in column 1
        # team name, link is in column 2
        if len(cols) >= 3 and seed_pattern.match(cols[1].get_text(strip=True)):
            team_col = cols[2]
            a = team_col.find("a")
            team_links[team_col.get_text(strip=True)] = urljoin(base_url, a["href"])

        elif len(cols) >= 4 and seed_pattern.match(cols[2].get_text(strip=True)):
            team_col = cols[3]
            in_semifinal.add(team_col.get_text(strip=True))

        elif len(cols) >= 5 and seed_pattern.match(cols[3].get_text(strip=True)):
            team_col = cols[4]
            in_semifinal.add(team_col.get_text(strip=True))

    assert len(in_semifinal) == 8
    return [
        {
            "name": team_name.rstrip("*"),
            "url": team_links[team_name],
        }
        for team_name in in_semifinal
    ]


def get_players(team_url: str) -> list:
    """Gets all the players from a team that were in the roster for semi finals
    arguments:
        team_url (str) : the url for the team
    returns:
        player_infos (list) : list of player info dictionaries
            with form: {'name': player name, 'url': player wikipedia page url}
    """
    print(f"Finding players in {team_url}")

    # Get the table
    response = get_html(team_url)
    # parse the HTML
    soup = BeautifulSoup(response, "html.parser")

    roster = soup.find(id="Roster")
    table = roster.find_next("table", {"class": "toccolours"})

    players = []

    # Loop over every row and get the names from roster
    rows = table.find_all('tr')
    for row in rows[3:]:
        # Get the columns
        cols = row.find_all('td')

        player = cols[2]

        url = find_urls(str(player), base_url)
        assert len(url) == 1

        player_dict = {
            'name': unicodedata.normalize('NFKD', player.text.strip()),
            'url': list(url)[0]
        }
        players.append(player_dict)

    return players


def get_player_stats(player_url: str, team: str) -> dict:
    """Gets the player stats for a player in a given team
    arguments:
        player_url (str) : url for the wiki page of player
        team (str) : the name of the team the player plays for
    returns:
        stats (dict) : dictionary with the keys (at least): points, assists, and rebounds keys
    """
    print(f"Fetching stats for player in {player_url}")

    # Get the table with stats
    response = get_html(player_url)
    # parse the HTML
    soup = BeautifulSoup(response, "html.parser")

    NBA = soup.find(id="NBA")
    if NBA is None:
        NBA = soup.find(id="NBA_career_statistics")

    table = NBA.find_next("table", {"class": "wikitable"})
    rows = table.find_all('tr')
    stats = { key : 0.0 for key in ['points', 'rebounds', 'assists'] }
    # Loop over rows and extract the stats
    for row in rows[1:]:
        # Get the columns
        cols = row.find_all('td')
        col_year = cols[0]
        col_team = cols[1]

        # Check correct team (some players change team within season)
        if "2021–22" in col_year.text.strip() and col_team.text.strip() == team:
            # load stats from columns
            stats['points'] = float(cols[12].text.strip().replace('*', ''))
            stats['rebounds'] = float(cols[8].text.strip().replace('*', ''))
            stats['assists'] = float(cols[9].text.strip().replace('*', ''))
            break

    return stats


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2022_NBA_playoffs"
    find_best_players(url)

