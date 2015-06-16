# -*- coding: utf-8 -*- 
import urllib, urllib2, json
from time import sleep
DISTRICT1 = u'中正區'
DISTRICT2 = u'大同區'
DISTRICT3 = u'中山區'
DISTRICT4 = u'松山區'
DISTRICT5 = u'大安區'
DISTRICT6 = u'萬華區'
DISTRICT7 = u'信義區'
DISTRICT8 = u'士林區'
DISTRICT9 = u'北投區'
DISTRICT10 = u'內湖區'
DISTRICT11 = u'南港區'
DISTRICT12 = u'文山區'

TARGET1 = u'土地'
TARGET2 = u'車位'
TARGET3 = u'建物'
TARGET4 = u'房地(土地+建物)'
TARGET5 = u'房地(土地+建物)+車位'

USAGE1 = u'住'
USAGE2 = u'商'
USAGE3 = u'工'
USAGE4 = u'農'
USAGE5 = u'其他'

TYPE1 = u'套房(1房1廳1衛)'
TYPE2 = u'公寓(5樓含以下無電梯)'
TYPE3 = u'華廈(10層含以下有電梯)'
TYPE4 = u'住宅大樓(11層含以上有電梯)'
TYPE5 = u'透天厝'
TYPE6 = u'其他'
TYPE7 = u'店面(店鋪)'
TYPE8 = u'廠辦'
TYPE9 = u'辦公商業大樓'

USE_TYPE = u'住家用'










def preprocess(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    lines.pop(0) # remove colunm title

    dataset = []

    for line in lines:
        dataArr = line.decode('big5').strip().split(',')

        # district
        if dataArr[0] == DISTRICT1:
            district = 1
        elif dataArr[0] == DISTRICT2:
            district = 2
        elif dataArr[0] == DISTRICT3:
            district = 3
        elif dataArr[0] == DISTRICT4:
            district = 4
        elif dataArr[0] == DISTRICT5:
            district = 5
        elif dataArr[0] == DISTRICT6:
            district = 6
        elif dataArr[0] == DISTRICT7:
            district = 7
        elif dataArr[0] == DISTRICT8:
            district = 8
        elif dataArr[0] == DISTRICT9:
            district = 9
        elif dataArr[0] == DISTRICT10:
            district = 10
        elif dataArr[0] == DISTRICT11:
            district = 11
        elif dataArr[0] == DISTRICT12:
            district = 12
        else:
            district = -1;
        assert district != -1

        # target
        if dataArr[1] == TARGET1:
            target = 1
        elif dataArr[1] == TARGET2:
            target = 2
        elif dataArr[1] == TARGET3:
            target = 3
        elif dataArr[1] == TARGET4:
            target = 4
        elif dataArr[1] == TARGET5:
            target = 5
        else:
            target = -1
        assert target != -1

        # area
        #area = dataArr[3]

        # usage
        if dataArr[4] == USAGE1:
            usage = 1
        elif dataArr[4] == USAGE2:
            usage = 2
        elif dataArr[4] == USAGE3:
            usage = 3
        elif dataArr[4] == USAGE4:
            usage = 4
        elif dataArr[4] == USAGE5:
            usage = 5
        elif dataArr[4] == '': #車位
            usage = 0
        else:
            usage = -1
        assert usage != -1

        # type
        if dataArr[11] == TYPE1:
            type = 1
        elif dataArr[11] == TYPE2:
            type = 2
        elif dataArr[11] == TYPE3:
            type = 3
        elif dataArr[11] == TYPE4:
            type = 4
        elif dataArr[11] == TYPE5:
            type = 5
        elif dataArr[11] == TYPE6:
            type = 6
        elif dataArr[11] == TYPE7:
            type = 7
        elif dataArr[11] == TYPE8:
            type = 8
        elif dataArr[11] == TYPE9:
            type = 9
        else:
            print dataArr[11]
            type = -1
        assert type != -1

        # age
        #if target != 1:
            #print dataArr[14]

        # scale
        scale = dataArr[15]

        # bedroom
        bedroom = dataArr[16]

        # living room
        living_room = dataArr[17]

        #restroom
        restroom = dataArr[18]

        #price
        price = dataArr[22]

        if dataArr[12] == USE_TYPE:
            # lat lng
            latlng = getLatLng(dataArr[2].encode('utf-8'))
            sleep(0.2)
            print latlng
            dataset.append([float(latlng[0]), float(latlng[1]), float(scale), int(bedroom), 
                int(living_room), int(restroom), int(price)])
    #print lines[0].decode('big5')
    print dataset
    print mat(dataset)
    return dataset



def getLatLng(address):
    #print address
    url = 'http://maps.googleapis.com/maps/api/geocode/json'
    data = {}
    data['address'] = address
    data['sensor'] = 'false'
    url_value = urllib.urlencode(data)
    full_url = url + '?' + url_value
    response = urllib2.urlopen(full_url)
    the_page = response.read()
    #print the_page
    lat = json.loads(the_page)['results'][0]['geometry']['location']['lat']
    lng = json.loads(the_page)['results'][0]['geometry']['location']['lng']
    return lat, lng
