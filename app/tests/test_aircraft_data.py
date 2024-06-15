from app.aircraft_data import AircraftData

def main():
    # Create class instances
    aircraft_data = AircraftData()

    # TESTING ENTIRE COMPONENT
    # Open feed

    aircraft_data.invoke()

    # TESTING INDIVIDUAL COMPONENTS
    # Open up rss docs test dataset
    # file_path = "app/tests/test_datasets/rss_docs_small_2024-06-04.pkl"
    # with open(file_path, 'rb') as f:
    #     rss_docs = pickle.load(f)
    
    # # Open up rss titles test dataset
    # file_path = "./app/tests/test_datasets/rss_titles_small_2024-06-04.pkl"
    # with open(file_path, 'rb') as f:
    #     rss_titles = pickle.load(f)

    # # prepare the rss content
    # new_docs = data_prepper._remove_used_rss_docs(rss_docs=rss_docs)
    # data_prepper._normalize_rss_docs(rss_docs=new_docs)

    # # prepare the rss titles
    # new_titles = data_prepper._remove_used_rss_titles(rss_titles=rss_titles)
    # data_prepper._normalize_rss_titles(rss_titles=new_titles)

if __name__ == "__main__":
    main()