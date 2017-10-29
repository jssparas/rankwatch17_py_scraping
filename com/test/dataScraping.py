'''
Created on 29-Oct-2017

@author: linux
'''
from urllib2 import urlopen
from bs4 import BeautifulSoup
import csv
print "hello"

web_url = "https://www.babynamesdirect.com/"
soup = ""
data = []
path = "names.csv"

def get_web_page(web_url):
    return urlopen(web_url)

def write_csv_file(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter= ",")
        for row in data:
            writer.writerow([row])


if __name__ == "__main__":
    web_page = get_web_page(web_url)
    soup = BeautifulSoup(web_page)
#     print soup.prettify()
    names = soup.find_all("a", attrs = {"class": ["girl", "boy"]})
#     print "number of  names %d" % len(names)
    for name in names:
            print "name: %s, gender: %s" % (name.string, name.get("class")[0])
            data.append(name.string + "," + name.get("class")[0])
           
    write_csv_file(data, path)
    

