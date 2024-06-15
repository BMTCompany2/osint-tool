# imports
from app.document_fetcher import DocumentFetcher

# main
def main():
    # initialize classes:
    document_fetcher = DocumentFetcher()

    try:
        # Grab report data
        report_data = document_fetcher.invoke()

        # Grab images

        # Write Reports

        # Grab aircraft data

        # Produce Content
        

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()