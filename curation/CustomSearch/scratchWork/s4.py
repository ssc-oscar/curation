from googleapiclient.discovery import build
import numpy as np

def google_results_count(query):
    service = build("customsearch", "v1",
                    developerKey="AIzaSyAJ4QECIkkSFzq3oCpLNflo_0smpGW0l5M")

    result = service.cse().list(
            q=query,
            cx='006187454826874335284:4jf25u-lylc'
        ).execute()

    return result["Title"]["link"]

print google_results_count('Python is awesome')

def main():
    service = build('customsearch', 'v1', developerKey="AIzaSyAJ4QECIkkSFzq3oCpLNflo_0smpGW0l5M")

    resDict = {}
    file = open("./data.csv", "r")
    keys = []

    for key in file.readlines():
        keys.append(key)
    keys.sort()

    for keyword in keys:
        google_results_count(keyword)
        
        
        
        print(u"\nRESULTS SEARCH FOR: %s" % str(keyword))

        res = service.cse().list(
            q=keyword,
            cx='006187454826874335284:4jf25u-lylc',
            num=5,
            safe= 'off',
        ).execute()

        if not 'items' in res:
            print (u"No result !!\nres is: %s" % str(res))
        else:
            with open("results_data.txt", "w") as f:
                for item in res['items']:
                    print('\n%s:\n\t%s' % (item['title'], item['link']))
                    f.write(str(item))
                    

if __name__ == '__main__':
    main()