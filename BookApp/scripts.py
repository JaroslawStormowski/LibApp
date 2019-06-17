import os
import django
from .models import Book

import urllib.request
import json


class Script:

    list_d = []

    def parse_json(self, url):
        #self.list_d = []
        response = urllib.request.urlopen(url)
        data_all = json.loads(response.read())
        data = data_all["items"]
        i = 0

        for item in data:
            dic = {}
            try:
                dic["title"] = item["volumeInfo"]["title"]
                dic["authors"] = item["volumeInfo"]["authors"]
                dic["publishedDate"] = item["volumeInfo"]["publishedDate"]
                dic["industryIdentifiers"] = item["volumeInfo"]["industryIdentifiers"]
                dic["pageCount"] = item["volumeInfo"]["pageCount"]
                dic["imageLinks"] = item["volumeInfo"]["imageLinks"]
                dic["language"] = item["volumeInfo"]["language"]
            except:
                pass
            if len(self.list_d) < (i+1):
                self.list_d.append(dic)
            else:
                self.list_d[i] = dic
            i += 1
        return self.list_d

    @staticmethod
    def transfer_data(dic):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibApp.settings')
        django.setup()
        try:
            d, created = Book.objects.get_or_create(title=dic["title"],
                                                    authors=dic["authors"],
                                                    publishedDate=dic["publishedDate"],
                                                    industryIdentifiers=dic["industryIdentifiers"],
                                                    pageCount=dic["pageCount"],
                                                    imageLinks=dic["imageLinks"],
                                                    language=dic["language"])
        except:
            created = False
            return created
        print("- Book: {0}, Created: {1}".format(str(d), str(created)))
        d.save()
        return created


