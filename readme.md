# Quick Coding Challenge from Augmento

Coding Challeng from Augmento. The main task involves showing the relationship 
between basic market sentiment and market price.

### Dependencies

Main packages used are numpy, pandas, matplotlib.pyplot, requests, and sklearn.
A bitmexData was created to pull data from bitmex API. The final project with 
visualisations is stored in a jupyter-notebook.

### Running the code

To get data from API, specify end date, start date, and a symbol of interest. [Click here for more info on symbols](https://www.bitmex.com/)

```python
bitmexData.Hourly('2016-11-01','2018-03-07','XBTUSD')
```
The example above, is for a price of bitcoin in USD from 2016-11-01 until 2018-03-07.

The rest of the project that show calculations and graphs is in a jupter-notebook file.


**Comments**
- Amount spent: about 3 hours
- Chose XBTUSD as data
- Wasn't sure about stationarity of the return data (assumed percentage change)
- Data not uploaded

**Comments ver2**
-  I spent another 2-3 hours to play with data
-  Used close price this time and did a correlation with another ratio
-  Better outcome
