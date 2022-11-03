import re
from typing import Tuple

## -- Task 3 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

#month names short?


def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"\d{4}"

    # month should accept month names or month numbers

    months_individually = [
        r"\b[jJ]an(?:uary)?\b",
        r"\b[fF]eb(?:ruary)?\b",
        r"\b[mM]ar(?:ch)?\b",
        r"\b[aA]pr(?:il)?\b",
        r"\b[mM]ay\b",
        r"\b[jJ]un(?:e)?\b",
        r"\b[jJ]ul(?:y)?\b",
        r"\b[aA]ug(?:ust)?\b",
        r"\b[sS]ep(?:tember)?\b",
        r"\b[oO]ct(?:ober)?\b",
        r"\b[nN]ov(?:ember)?\b",
        r"\b[dD]ec(?:ember)?\b"
    ]
    # months = rf"(?:{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{oct}|{nov}|{dec})"
    months_str = r"(?:" + "|".join(months_individually) + ")"

    # day should be a number, which may or may not be zero-padded
    day = r"\d{1,2}"

    return year, months_str, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    d = {
        "january": "01", "jan": "01",
        "february": "02", "feb": "02",
        "march": "03", "mar": "03",
        "april": "04", "apr": "04",
        "may": "05",
        "june": "06", "jun": "06",
        "july": "07", "jul": "07",
        "august": "08", "aug": "08",
        "september": "09", "sep": "09",
        "october": "10", "oct": "10",
        "november": "11", "nov": "11",
        "december": "12", "dec": "12"
    }

    # Convert to number as string
    if not s.isdigit():
        s = d[s.lower()]
    return s


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    """
    return f'{int(n):02d}'


def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """
    # find all dates in any format in text
    year, month_str, day = get_date_patterns()

    # Date on format DD/MM/YYYY - DYM, 13 October 2020
    DMY = rf"{day}\s{month_str}\s{year}"
    dmy_list = re.findall(rf"{DMY}", text)

    for i, elem in enumerate(dmy_list):
        elem = re.sub(rf"({day})\s({month_str})\s({year})", r"\3/\2/\1", elem)
        elem = re.sub(month_str, lambda s: convert_month(s.group()), elem)
        elem = re.sub(day, lambda n: zero_pad(n.group()), elem)
        dmy_list[i] = elem


    # Date on format MM/DD/YYYY - MDY, October 13, 2020
    MDY = rf"{month_str}\s{day},?\s{year}"
    mdy_list = re.findall(rf"{MDY}", text)

    for i, elem in enumerate(mdy_list):
        elem = re.sub(rf"({month_str})\s({day}),?\s({year})", r"\3/\1/\2", elem)
        elem = re.sub(month_str, lambda s: convert_month(s.group()), elem)
        elem = re.sub(day, lambda n: zero_pad(n.group()), elem)
        mdy_list[i] = elem


    # Date on format YYYY/MM/DD - YMD, 2020 October 13
    YMD = rf"{year}\s{month_str}\s{day}"
    ymd_list = re.findall(rf"{YMD}", text)

    for i, elem in enumerate(ymd_list):
        elem = re.sub(rf"({year})\s({month_str})\s({day})", r"\1/\2/\3", elem)
        elem = re.sub(month_str, lambda s: convert_month(s.group()), elem)
        elem = re.sub(day, lambda n: zero_pad(n.group()), elem)
        ymd_list[i] = elem


    # Date on format YYYY/MM/DD - ISO, 2020-10-13
    # ISO = rf"{year}-?\s{month_int}-?\s{day}"
    ISO = r'(?:\d{4})-\b(?:0\d|1[0-2])\b-(?:\d\d?)'
    iso_list = re.findall(ISO, text)

    for i, elem in enumerate(iso_list):
        iso_list[i] = elem.replace("-", "/")


    dates = dmy_list + mdy_list + ymd_list + iso_list

    # Write to file if wanted
    if output:
        print(f"Writing to: {output}")
        with open(f'{output}', 'w') as f:
            f.write('\n'.join(dates))

    return dates

if __name__ == '__main__':
    # date_str = ("DMY: 2 January 2020, MDY: February 12, 1954, YMD: 2015 March 31, ISO: 2022-04-15, DMY: 22 June 2020, MDY: October 13, 2025, YMD: 2019 December 2")
    date_str = ("1900-01-01,  2025-03-15, 2022-04-15, 1000-06-12")
    find_dates(date_str)