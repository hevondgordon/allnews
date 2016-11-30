from flask import Flask,render_template
from bs4 import BeautifulSoup
import urllib
app = Flask(__name__)



# def getContent(url):
#     fetchurl=urllib.urlopen(url)
#     content=fetchurl.read()
#     fetchurl.close()
#     soup=BeautifulSoup(content,'html.parser')
#     for i in soup.find_all('div',{'class': lambda x: x and 'showcase-content' in x.split()}):
#         print i.a.img['src']
#     return soup


@app.route('/',methods=['POST','GET'])
def hello_world():
    return render_template('app.html')


# app.run(host="0.0.0.0")
app.run(debug=True,host="0.0.0.0")
