import requests

import json

from urllib.request import urlopen

# from json2table import convert

import html2text



class Rewriter:

    def __init__(self, text):

        self.text = text

    def req(self, text):

        self.headers = {'content-type': 'application/json'}

        self.unftext = requests.post('https://rewritingtools.com/rewritearticle.php?action=rewrite&range=100', data={'data': self.text})

        if self.unftext.status_code == 200:

            self.text_str = self.unftext.text

        else:

            self.text_str = "API IS DOWN"

        return self.text_str

    # print(ress.text)

    def filter(self, text):

        self.txt = text

        self.sub1 = "#@@#@@#"

        self.sub2 = "#@@#@@#"

        # getting index of substrings

        self.txt=self.txt.replace(self.sub1,"*")

        self.txt=self.txt.replace(self.sub2,"*")

        self.re=self.txt.split("*")

        self.txt=self.re[1]

        return self.txt

        

    def main(self, engine):
        self.engine = engine
        if self.engine == None:
            self.engine = 1
        if self.engine == 1:

            self.retext = self.req(self.text)

            self.changed = self.filter(self.retext)

            self.rewrittentxt = self.retext.replace(self.sub1, "")

            self.rewrittentxt = self.rewrittentxt.replace(self.changed, "")

            self.rewrittentxt = html2text.html2text(self.rewrittentxt)

            self.rewrittentxt = self.rewrittentxt.replace("**", "")

            self.list = [self.rewrittentxt, self.changed]
        elif self.engine == 2:
            self.unftext = requests.post("https://rewritertools.com/article-spinner-tool/php/process.php", data={'data': self.text})
            self.ntext = self.unftext.text
            self.changed = None
            self.list = [self.ntext, self.changed]
        return self.list

    

   





#build_direction = "LEFT_TO_RIGHT"

#table_attributes = {"style" : "width:100%"}

#html = convert(res, build_direction=build_direction, table_attributes=table_attributes)

# print(html)

  







