"""Get hex colour codes from website"""

import json
import requests
URL = "https://www.color-hex.com/color-names.html"
#URL = "https://www.color-hex.com"
response = requests.get(URL)
print(response.text)



#print(color_codes)


















