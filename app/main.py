# imports
from app.document_fetcher import DocumentFetcher
from app.generate_report import GenerateReport


# main
def main():
    # initialize classes:
    document_fetcher = DocumentFetcher()
    # ...intialize more moduels here
    generate_report = GenerateReport()
    try:
        # Grab report data
        report_data = document_fetcher.invoke()

        # Grab images
        # ...grab and analyze image module here
        
        # Grab aircraft data
        # ...grab aircraft data here

        # Produce Content
        # ...produce the report here
        generate_report(report_data)

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()