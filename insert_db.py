import messengers_scrape
from scrape import GooglePlay
from postgres_db import Models
from sqlalchemy.orm import sessionmaker

class ScrapeGooglePlay:

    def __init__(self):

        engine = Models.db_connect()
        Models.create_table(engine)

        # create a session
        self.Session = sessionmaker(bind=engine)

    def process(self):

        """ 
        get the metrics
        """

        session = self.Session()

        messengers_list = messengers_scrape.get_messengers()
        playstore = GooglePlay()
        final_data = messengers_scrape.get_data(messengers_list, playstore)

        for messenger, data in final_data.items():

            data = Models.App_metrics(**data)

            try:
                session.add(data)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

        return final_data


if __name__ == "__main__":

    a = ScrapeGooglePlay()
    p = a.process()
    print p


