import csv
import requests
from bs4 import BeautifulSoup

def scrape_pamgolding():
    url = "https://www.pamgolding.co.za/property-search/residential-properties-to-rent-long-term-zambia/2656"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Debugging: Print HTML content for inspection
    print(soup.prettify())

    # Extract data (replace with actual HTML structure of the website)
    Property_to_rent = soup.find('a', class_='Property to rent')
    propertyDetails = soup.find('article', class_='propertyDetails')
    location_text = soup.find('span', class_='location-text')
    Rent = soup.find('span', class_='totalVal')
    propertyContact = soup.find('div', class_='propertyContact')

    # Debugging: Print extracted data for inspection
    print("Property to rent:", Property_to_rent)
    print("propertyDetails:", propertyDetails)
    print("location-text:", location_text)
    print("totalVal:", Rent)
    print("propertyContact:", propertyContact)

    # Handle None values
    Property_to_rent = Property_to_rent.get_text(strip=True) if Property_to_rent else None
    propertyDetails = propertyDetails.get_text(strip=True) if propertyDetails else None
    location_text = location_text.get_text(strip=True) if location_text else None
    Rent = Rent.get_text(strip=True) if Rent else None
    propertyContact = propertyContact.get_text(strip=True) if propertyContact else None

    return {
        'Property to rent': Property_to_rent,
        'propertyDetails': propertyDetails,
        'location-text': location_text,
        'totalVal': Rent,
        'propertyContact': propertyContact
    }

def write_to_csv(data_list):
    header = ['Property to rent', 'propertyDetails', 'location-text', 'totalVal', 'propertyContact']
    with open('property_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for data in data_list:
            # Handle None values with an empty string
            row_data = [data.get(key, '') for key in header]
            writer.writerow(row_data)

def main():
    data_list = []

    # Scraping data from pamgolding
    pamgolding_data = scrape_pamgolding()
    data_list.append(pamgolding_data)

    # Debugging: Print data_list for inspection
    print(data_list)

    # Writing data to CSV
    write_to_csv(data_list)

if __name__ == "__main__":
    main()
