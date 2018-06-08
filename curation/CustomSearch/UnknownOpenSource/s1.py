from googleapiclient.discovery import build
import csv
import sys

def main():
    service = build('customsearch', 'v1', developerKey="AIzaSyAJ4QECIkkSFzq3oCpLNflo_0smpGW0l5M")

#    file = open("./data.csv", "r")
    filename = sys.argv[1]
    file = open(filename, "r")
    keys = []

    for key in file.readlines():
        keys.append(key)
    keys.sort()

    for keyword in keys:
        print(u"\nRESULTS SEARCH FOR: %s" % str(keyword))

        res = service.cse().list(
            q=keyword,
            cx='006187454826874335284:4jf25u-lylc',
            num=10,
            safe= 'off',
        ).execute()

        if not 'items' in res:
            print (u"No result !!\n")
        else:
            with open("results_data.csv", "a", newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                for item in res['items']:
                    data=[item['title'], item['link'], keyword]
                    writer.writerow(data)

if __name__ == '__main__':
    main()
