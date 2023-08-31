import urllib.request
from html.parser import HTMLParser
from urllib import request
import csv
infor = []
photo = []
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_div = False
    def handle_starttag(self, tag, attrs):
        if attrs != [] and attrs[0] == ('class', 'col-md-1-5 col-sm-1-5  col-xs-6'):
            self.in_div = True
        if tag == "img":
            for i in attrs:
                if i[0] == 'src':
                    photo.append(i[1])
    def handle_data(self, data):
        if self.in_div == True and 1<len(data)<=6 and self.lasttag != "a" and self.lasttag != "h5":
            infor.append(data.strip())




url = "https://sdmda.bupt.edu.cn/szdw/js.htm"
my_request = request.Request(url)
response = request.urlopen(my_request)
result = response.read().decode('utf-8')


par = MyHTMLParser()
par.feed(result)

for i in range(0,21):
    infor.remove('')
del photo[0:2]
del photo[10:16]

filenames = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg"]
for i in range(len(filenames)):
    filenames[i] = infor[i*2] + ".jpg"
for i in range(len(photo)):
    photo[i] = "https://sdmda.bupt.edu.cn" + photo[i]
    downer = urllib.request.urlretrieve(photo[i], filename=filenames[i])

csvfile = open("professor.csv", mode = "w", newline = "")
fieldnames = ["Department", "Name", "Title", "Photo"]
write = csv.DictWriter(csvfile, fieldnames=fieldnames)
write.writeheader()
for i in range(0, len(infor), 2):
    write.writerow({"Department":infor[i+1], "Name":infor[i], "Title":"教授", "Photo":filenames[int(i/2)]})

