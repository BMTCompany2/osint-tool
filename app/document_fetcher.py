# imports
import json
from datetime import datetime, timedelta, timezone
from langchain_community.document_loaders import RSSFeedLoader, PyPDFLoader


class DocumentFetcher:

    def __init__(self):
        return

    def invoke(self):
        gov_feeds = self._grab_gov_comms()
        pdf_docs = self._grab_maritime_reports()
        news_feeds = self._grab_news()

        comined_docs = gov_feeds + pdf_docs + news_feeds
        

        print()
        print('Combined Feed Length')
        print(len(comined_docs))

        return comined_docs
    

    def _grab_gov_comms(self):
        # Grab the RSS feed data
        print('Fetching gov docs...')
        RSS_CONFIG_PATH = "app/document_sources/gov_feeds.json"
        feeds = []

        with open(RSS_CONFIG_PATH, 'r') as file:
            config_data = json.load(file)
            feeds = config_data.get('gov_feeds', [])

        RSSLoader = RSSFeedLoader(urls=feeds, show_progress_bar=True)
        rss_docs = RSSLoader.load()

        current_time = datetime.now(timezone.utc)
        twenty_four_hours_ago = current_time - timedelta(hours=72)

        new_rss_docs = []
        for doc in rss_docs:
            published_date = doc.metadata.get('publish_date')
            if published_date is not None:
                published_date = published_date.replace(tzinfo=timezone.utc)  # Make published_date offset-aware
                if published_date > twenty_four_hours_ago:
                    print('PUBLISHED DATE: ', published_date)
                    new_rss_docs.append(doc)
            else :
                new_rss_docs.append(doc) 
        
        print('Number of Gov Docs')
        print(len(new_rss_docs))
        print()

        return new_rss_docs
    
    def _grab_maritime_reports(self):
        # Grab the RSS feed data
        print('Fetching gov docs...')
        PDF_PATH = "app/document_sources/ukmto_6-15.pdf"

        PDFloader = PyPDFLoader(PDF_PATH)
        pdfs = PDFloader.load()
        pdf_docs = [pdfs]
        
        print('Number of DPF Docs')
        print(len(pdf_docs))
        print()

        return pdf_docs
       
    def _grab_news(self):
        # Grab the RSS feed data
        print('Fetching news feeds...')
        RSS_CONFIG_PATH = "app/document_sources/news_feeds.json"
        feeds = []

        with open(RSS_CONFIG_PATH, 'r') as file:
            config_data = json.load(file)
            feeds = config_data.get('news_feeds', [])

        RSSLoader = RSSFeedLoader(urls=feeds, show_progress_bar=True)
        rss_docs = RSSLoader.load()

        current_time = datetime.now(timezone.utc)
        twenty_four_hours_ago = current_time - timedelta(hours=72)

        new_rss_docs = []
        for doc in rss_docs:
            published_date = doc.metadata.get('publish_date')
            if published_date is not None:
                published_date = published_date.replace(tzinfo=timezone.utc)  # Make published_date offset-aware
                if published_date > twenty_four_hours_ago:
                    print('PUBLISHED DATE: ', published_date)
                    new_rss_docs.append(doc)
        
        print("Number of news docs:")
        print(len(new_rss_docs))

        return new_rss_docs