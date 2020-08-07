import requests

# function to download talk's metadata and transcript from url
def download_data(url):

    # instantiate empty dict to save downloaded data
    downloaded_data = {}

    downloaded_data['url'] = url

    # talk url to make request from
    url = url

    # make request for metadata
    metadata_dl = requests.get(url, headers = {'User-agent': 'S bot 1.0'}).text
    downloaded_data['metadata_dl'] = metadata_dl

    # to get transcript_url,
    # modify talk url by inserting '/transcript/ before '?language=en'
    transcript_url = url[:-12] + '/transcript' + url[-12:]

    # make request for transcript
    transcript_dl = requests.get(transcript_url, headers = {'User-agent': 'S bot 1.0'}).text
    downloaded_data['transcript_dl'] = transcript_dl

    return downloaded_data
