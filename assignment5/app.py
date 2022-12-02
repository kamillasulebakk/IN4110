import datetime
from typing import List, Optional

import uvicorn

import altair as alt
from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from strompris import (
    ACTIVITIES,
    LOCATION_CODES,
    fetch_day_prices,
    fetch_prices,
    plot_activity_prices,
    plot_daily_prices,
    plot_prices,
)

from IPython.display import HTML

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def strompris(
    request: Request,
    location_codes = tuple(LOCATION_CODES.keys()),
    today: datetime.date = datetime.date.today()
) -> templates.TemplateResponse:

    return templates.TemplateResponse(
        "strompris.html",
        {
            "request": request,
            "location_codes": location_codes,
            "today": today
        }
    )


@app.get("/plot_prices.json")
def plot_strompris(
    locations: Optional[List[str]] = Query(default = list(LOCATION_CODES.keys())),
    end: Optional[str] = '2022-11-30',
    days: int = 7
):
    end_date = datetime.datetime.strptime(end, r'%Y-%m-%d').date()

    df = fetch_prices(end_date, days, locations)
    c = plot_prices(df)

    return c.to_dict()

uvicorn.run(app, port=8000)


# GET /plot_prices.json should take ts:
# - locations (list from Query)
# - end (date)
# - days (int, default=7)
# all inputs should be optional
# return should be a vega-lite JSON chart (alt.Chart.to_dict())
# produced by `plot_prices`
# (task 5.6: return chart stacked with plot_daily_prices)

...

# Task 5.6:
# `GET /activity` should render the `activity.html` template
# activity.html template must be adapted from `strompris.html`
# with inputs:
# - request
# - location_codes: location code dict
# - activities: activity energy dict
# - today: current date

...

# Task 5.6:
# `GET /plot_activity.json` should return vega-lite chart JSON (alt.Chart.to_dict())
# from `plot_activity_prices`
# with inputs:
# - location (single, default=NO1)
# - activity (str, default=shower)
# - minutes (int, default=10)

...


# mount your docs directory as static files at `/help`

...

if __name__ == "__main__":
    # use uvicorn to launch your application on port 5000

    ...
