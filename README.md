# marketSentiment

This program handled the natural language processing portion of my LSTM Bitcoin project.

data scraped by the webscraper program is processed by this program to generate some quantifiable values for the LSTM program to parse and combine with other historical data to make predictions 

This is accomplished by using the default Vader lexicon which I attempted to intensly customize in order to better adapt to bitcoin news reporting. 
In addition to this, input data was also screened to remove adds, and then valued by quantities of Irrlevant data, and length of article. 

The ouput of this program would be sent to the LSTM project for computation. 
