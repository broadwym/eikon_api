# eikon_api
Tutorial: How to pull data via Eikon API 

## Steps
1. Prior to installing the Eikon proxy, you will need to download [Python](https://www.python.org/downloads/). Also download a Python IDE (e.g. [Spyder](https://anaconda.org/anaconda/anaconda-navigator), [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)). 
2. Once you have Python and an IDE installed, download [Eikon's proxy](https://developers.thomsonreuters.com/eikon-data-apis/downloads). You have to use the proxy to access Eikon API. 
3. Log in to Eikon API Proxy using your assigned username (Owen email) and password. 
4. Click on Get an AppID:

![Alt Text](http://i64.tinypic.com/331dpoh.png)

5. Name your app. For testing purposes, I named my app **"test."** This will generate a unique alphanumeric token that you will later use to access Ekion API. Do not share this token. Copy paste the token into a text editor. 
6. Open up the command line. Install the eikon library:
```
py -m pip install eikon
```
![Alt Text](https://media.giphy.com/media/l1IBjYjZsFJMfWJig/giphy.gif)

7. Pull up your IDE of choice. Copy paste these three lines of code into a new file. Copy paste your unique alphanumeric token from the text editor as indicated. Run the code, including the ek.get_news_headlines function. 
```
import eikon as ek
ek.set_app_id('your unique alphanumeric AppID')
ek.get_news_headlines('R:LHAG.DE', date_from='2017-04-05T09:00:00', date_to='2017-04-05T18:00:00')
```
![Alt Text](https://media.giphy.com/media/3oFzmiH7vMzbFEQOpG/giphy.gif)

8. Your output should be a table: **LHAG.DE** represents the quote of Lufthansa's shares (LHAG) traded on Xetra (DE). The timestamp indicates a timespan from April 5th, 2017 9:00am to 6:00pm. 
9. Eikon API utilizes a different set of paramters than the .NET and Excel options. To create a unique call you must use Ekion's Data Item Browser (DIB). Locate DIB via the Eikon API Proxy app. 

![Alt Text](https://media.giphy.com/media/d3OG1zusIRPrmROM/giphy.gif)

10. For example, if you were interested in the **Solactive German Mergers & Acquistions Performance Index**, you would search for the index in **"Instrument."** DIB would tell your instrument parameter is **".SOLDMA"**. If you wanted to pull .SOLDMA's highest and lowest bid price for the day, you would search in **"Find Data Item."** DIB would tell you your parameters are **"CF_High"** and **"CF_Low"**, as seen under Data Item Code.  
```
ek.get_data(['.SOLDMA'], ['CF_High', 'CF_Low'])
( Instrument CF_HIGH CF_LOW
0 .SOLDMA 355.79 353.45, None)
```
10. An extensive list of Eikon API parameters and example calls can be found [here](https://docs-developers.thomsonreuters.com/1513187148816/14684/book/en/eikon/index.html#get_data). 
