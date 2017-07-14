import urllib
import json

class search:
    """ Return a new search instance given a phone number.

    """
    def __init__(self, number):
        URL = 'https://search5.truecaller.com/v2/search?'

        raw_params = {
            'q': number,
            'countryCode': 'IN',
            'type': '4',
            'locAddr': '',
            'placement': 'SEARCHRESULTS,HISTORY,DETAILS',
            'clientId': '1',
            'myNumber': 'lS5757de85c2804a87d452c139OpYeO6gR6qlj0QFJJQMpo1',
            'registerId': '285661581',
            'encoding': 'json',
        }

        params = urllib.urlencode(raw_params)
        url_params = URL + params
        response = urllib.urlopen(url_params).read()
        parsed = json.loads(response)

        basic = parsed['data'][0]
        phone_parsed = parsed['data'][0]['phones'][0]
        address_parsed = parsed['data'][0]['addresses'][0]

        self.id = basic['id']
        """ Truecaller id """
        self.name = basic['name']
        """ Truecaller name """
        self.score = basic['score']
        """ Truecaller score """
        self.access = basic['access']
        self.enhanced = basic['enhanced']
        self.internet_address = basic['internetAddresses']
        self.badges = basic['badges']
        self.tags = basic['tags']
        self.sources = basic['sources']

        self.phone = phone(phone_parsed)
        self.address = address(address_parsed)

        self.provider = parsed['provider']
        self.trace = parsed['trace']
        self.sourcestats = parsed['stats']['sourceStats']

class phone:
    """ Returns information about phone number. """
    def __init__(self, phone):
        self.phone = phone['e164Format']
        self.numbertype= phone['numberType']
        self.national = phone['nationalFormat']
        self.dialcode = phone['dialingCode']
        self.countrycode = phone['countryCode']
        self.carrier = phone['carrier']
        try:
            self.spamscore = phone['spamScore']
            self.spamtype = phone['spamType']
        except KeyError:
            self.spamscore = None
            self.spamtype = None
        self.phonetype = phone['type']

class address:
    """ Returns information about location. """
    def __init__(self, address):
        self.area = address['area']
        self.city = address['city']
        self.countrycode = address['city']
        self.timezone = address['timeZone']
        self.type = address['type']
