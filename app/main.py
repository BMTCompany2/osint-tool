# imports
from app.document_fetcher import DocumentFetcher
from app.generate_report import GenerateReport
from app.describe_image import DescribeImage

# main
def main():
    # initialize classes:
    document_fetcher = DocumentFetcher()
    describe_image = DescribeImage()
    # ...intialize more moduels here
    generate_report = GenerateReport()
    try:
        # Grab report data
        report_data = document_fetcher.invoke()

        # Grab images
        # ...grab and analyze image module here
        image_path = '/Users/rishimadhok/Desktop/aircraft_carrier.png'
        img_description = describe_image.invoke(image_path)

        print (img_description)

        # Grab aircraft data
        # ...grab aircraft data here

        # Produce Content
        # ...produce the report here
        generate_report(report_data)

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()