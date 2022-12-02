# Project 5: Strømpris

Only task 1, 2, 3 and 5 is implemented. Links on the plot webpage to the documentation for the implementation has been produced, but the help page is not fully implemented.

## This project is created with:
* Python version: 3.7.6
  * altair
  * fastapi
  * pandas
  * requests
  * numpy
  * matplotlib

## How to run the different codes from the assignment 5 folder:
```
# Fetch data from https:/www.hvakosterstrommen.no/strompris-apiand visualize it (task 1):
python3 strompris.py
```
You will then get a url code with port = 8000. Copy this web address and paste into your
preferred web browser. 

```
# Generate a plot of energy prices by date and display it on a web page with help page (task 2 and 3):
python3 app.py

# Open the documentation home page for strompris.py (task 5)
open docs/build/html/index.html

# To test all the above implementations at once:
pytest
```




