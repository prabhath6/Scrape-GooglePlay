# Scrape-GooglePlay
Scrape GooglePlay store for messenger apps to get useful metrics.

## Initial Messenger apps
1. WhatsApp
2. Hike
3. Telegram
4. Viber
5. Skype
6. Messenger

## Working
These scripts will scrape through the GooglePlay's website in order to get useful metrics from it. Some of the metrics include url, title, last updated date, number of downloads, e.t.c. Requests is used to get the html file and then Beautifulsoup is used in order to parse the html content and access data based on the tags.

## Future Scope
1. Use SQLAlchemy to insert this data into postgres database.
2. Create a corn job to run these scripts every week or every 2 weeks.

