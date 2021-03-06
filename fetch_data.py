import requests
import json
import logging
import datetime


urls = {
    "data.json": "https://api.covid19india.org/data.json",
    "data_district.json": "https://api.covid19india.org/v2/state_district_wise.json",
}

def get_urls():
    return urls

def fetch_url(url, filename):
    data = requests.get(url)
    if data.status_code == 200:
        try:
            s = json.dumps(data.json())
            open(filename, "w").write(s)
        except Exception:
            logging.error("Exception occured", exc_info=True)
    else:
        logging.info("API response status was " +  str(data.status_code) + " for url " + url)

if __name__ == "__main__":
    logging.basicConfig(filename='fetch.log', filemode='a+', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    try:
        fetch_url(urls['data.json'], 'data.json')
        fetch_url(urls['data_district.json'], 'data_district.json')

        dt = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print("{timestamp} - Ran".format(timestamp=dt))
    except Exception:
        logging.error("Exception occured", exc_info=True)
