import requests
from datetime import datetime
from bs4 import BeautifulSoup


class GooglePlay:

    def get_stars(self, soup):

        # get each star ratting
        one = int(str(soup.find("div", {"class": "rating-bar-container one"}).text).split(" ")[5].replace(',', ""))
        two = int(str(soup.find("div", {"class": "rating-bar-container two"}).text).split(" ")[5].replace(',', ""))
        three = int(str(soup.find("div", {"class": "rating-bar-container three"}).text).split(" ")[5].replace(',', ""))
        four = int(str(soup.find("div", {"class": "rating-bar-container four"}).text).split(" ")[5].replace(',', ""))
        five = int(str(soup.find("div", {"class": "rating-bar-container five"}).text).split(" ")[5].replace(',', ""))

        return (one, two, three, four, five)



    def get_playstore_info(self, url):
        """
        Get all the details from web page.
        """
        app_page = requests.get(url)

        # parse the content of the web page
        soup = BeautifulSoup(app_page.content, 'html.parser')

        # get the title of the page
        title = str(soup.select("div.id-app-title")[0].text)

        # get starts
        stars = self.get_stars(soup)

        # get url
        page_url = str(soup.find("meta", {"itemprop": "url"})['content'])

         # Get value from meta tag rating
        ratingsValue = float(str(soup.find("meta", {"itemprop": "ratingValue"})['content']))
        ratingsCount = int(str(soup.find("meta", {"itemprop": "ratingCount"})['content']))

        # Get value by attribute
        num_downloads = str(soup.find("div", {"itemprop": "numDownloads"}).text)

        # get last updated date
        last_updated = datetime.strptime(str(soup.find("div", {"itemprop": "datePublished"}).text).replace(',', ''), '%b %d %Y').strftime('%Y-%m-%d')

        # number of downloads
        num_downloads_abs = num_downloads.split("-")[1]

        app_details = dict()
        
        app_details['title'] = title
        app_details['url'] = url
        app_details['rating'] = ratingsValue
        app_details['rated_by'] = ratingsCount
        app_details['downloads'] = int(num_downloads_abs.replace(" ", "").replace(",", ""))
        app_details['download_range_min'] = int(num_downloads.split("-")[0].strip(" ").replace(",", ""))
        app_details['download_range_max'] = int(num_downloads.split("-")[1].strip(" ").replace(",", ""))
        app_details['last_updated'] = last_updated
        app_details['rating_one'] = stars[0]
        app_details['rating_two'] = stars[1]
        app_details['rating_three'] = stars[2]
        app_details['rating_four'] = stars[3]
        app_details['rating_five'] = stars[4]
                                        
        
        return app_details
