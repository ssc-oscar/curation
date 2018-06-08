__author__ = 'wmacey@vols.utk.edu'

# Import the api module for the results class
import search_google.api

# Define buildargs for cse api
buildargs = {
  'serviceName': 'customsearch',
  'version': 'v1',
  'developerKey': 'AIzaSyAJ4QECIkkSFzq3oCpLNflo_0smpGW0l5M'
}

# Define cseargs for search
cseargs = {
  'q': 'nerd',
  'cx': '006187454826874335284:4jf25u-lylc',
  'num': 3
}

# Create a results object
results = search_google.api.results(buildargs, cseargs)

# Download the search results to a directory
results.download_links('downloads')
