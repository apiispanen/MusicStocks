# MusicalStocks
NOTE: DO NOT EDIT 'HISTORY.TXT' OR ANY CODES, THEY ARE ESSENTIAL TO THE PROGRAM'S STABILITY.


####MusicalStocks - The web app designed to bring back money into a starving industry.

The main purpose of the project is a musical trading platform in which regular, everyday users can invest in a share of a band’s net worth. Not net worth, but band popularity, which can be calculated by pulling information off of famous music-streaming platforms such as Spotify. Band popularity can be calculated Spotify's artist API endpoint, the product would be more similar to a gambling platform that would bet on new and emerging artists, depending on the amount of work required to do either. The topics I will explore will be the music industry (Spotify API), financial trading platforms (or one’s similar to kickstarter or Bloomberg), and will need to pull API and live data in order to generate estimated payouts based on initial investments. Data for the app is stored in a .txt file (called 'history.txt'), and is formatted in a system that store.py and write.py know how to store and analyze. (note: every function in this webapp were made by me, so they may be fairly unconventional or inefficient.) 

STEPS FOR IMPLEMENTATION:
1.  Run app.py (or go to https://musicalstocks.herokuapp.com/ if set up yet.)
2.  Go to 'http://127.0.0.1:5000/' on browser.
3.  Enter the initial value you wish to invest and the artist name. Press submit and enjoy!


API's Used for App:

Spotify Artists API Endpoint = This was to search and to give back popularity information on a particular artist, based on Spotify's API and auto-calculated popularity scores.

Pixabay API = Pulls a picture from Pixabay to give a picture (not always correct, intentionally) under the query term that the user had inputted.  

NECESSARY LIBRARIES FOR INSTALLATION:

-flask = configures the local server for webpage display
 
    Functions of flask:
    -->Flask = initializes flask, which creates the local server. 
    -->render_template =  Create an HTML template for the website, putting together the templates with the Python functions. 
    -->request = Pulls input from the application HTML interface. 

-Requests = creates the api requests and receives the JSON data

-OS (Operating System Interfaces) = Allows cmd-type controls

-pprint = for testing JSON requests in an easy-to-read format


FILES AND THEIR FUNCTIONS :

-App.py = This is the central file that puts the entire app together.
    -->Index = This is the initial interface function. It pulls together all the input, every variable into the template, and returns a result if the search is queried correctly. If the API query does not work through Spotify, it redirects the user to the page and displays an error message. If the pic URL receives an error, it displays a man shrugging to show that we cannot provide a picture for this artist in results.html. 
     (variables: input = investment amount and the queried artist name, output = results of the artist search in the API, details to pull analysis of the information from results, picurl to provide a picture URL from their API for HTML use on related artists, and history to show users other artists they have "invested" in.)
    -->Hello = As made from flask, this contains the option to manually enter in an artist name using the url '/results/{artist_name}' to search an artist without having to use the interface.

-auth.py = This is the request function that generates an API key each time it is called. Since Spotify's access tokens only last for a few hours, this simplifies the process of having to receive new keys each time for the code to work. 
    -->req_token() = generates the token by asking the API for a temporary token which it uses to pass along to other functions.
    
-artist.py = This file is dedicated to searching the artists, and pulling relevant info. 
    -->Search = Searches an artist through Spotify's API, pulling the token from auth.py and returning popularity scores.
    -Popularity = Like Search, this returns popularity scores with the input being artist ID's from Spotify. Used in initial testing. 
    -->History = This function performs an intricate textual analysis of the history data stored locally under 'history.txt'.

-write.py = This file works with 'history.txt' (creating it if not present) and does this (due to countless trials) inefficiently by creating another file called 'history2.txt' and giving it the updated version of 'history.txt''s data, and then deletes 'history.txt' so that 'history2.txt' can obtain that file name (using os).
    -->store = Opens or creates 'history.txt' and puts in the most recent entry into the sheet. It first checks if a user has already searched this artist (updating the popularity score if so), or adds a new line if it is a new artist.
    -->rewrite = writes the data in 'history2.txt', which becomes an updated copy of 'history1.txt', making the file essentially "rewritten".
    -->detail = detail is the textual analysis function that breaks down the parts of 'history.txt' and returns the necessary details about the app.

-invcalc.py = Calculates the investment, based on the popularity and some fairly arbitrary values.
    -->investment_calculator = (( % Change of popularity * 2 ) + 1 ) * investment

-imagesearch.py = Goes through pixabay's API to pull a related picture from the user's artist query. 
    -->get_image = returns a URL from the pixabay's API (for a cool visual)

-cache-auth.py = (Auto-generated) stores the access token.

-hello.html = main page, provides the input form as well as a sidebar of history related to the user's past history.

-results.html = results page, displays calculated amounts and provides a related picture. 

FILES NOT IN THE FINISHED PRODUCT:
-->Spotify.py = prototype for authorization
-->success_scores.py = initial ways of calculating the investment values.
-->toptrackresponse.txt = A guideline for how the Spotify API JSON responses look like. 
-->index.html = initial template for the interface.