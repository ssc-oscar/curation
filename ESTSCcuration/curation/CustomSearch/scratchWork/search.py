__author__ = 'wmacey@vols.utk.edu'

import pprint

from googleapiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyAJ4QECIkkSFzq3oCpLNflo_0smpGW0l5M")

  res = service.cse().list(
      q='audris mockus',
      cx='006187454826874335284:4jf25u-lylc',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()