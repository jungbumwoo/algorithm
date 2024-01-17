import html

from urllib.parse import parse_qsl, urlsplit
from django.test import RequestFactory
allocation_url = "ad.buzzvil.com/api/v2/ads?accountId=285386093&birthday=1987-12-31&clientIp=106.102.11.89&country=KR&creativeSize=0&cursor=&deviceId=285386093&deviceName=SM-A235N&gender=F&ifa=e8d96d2d-d9aa-4a3b-b2d9-bb56ad5291ae&ifv=&language=ko&mcc=450&membershipDays=130&mnc=06&networkType=4G&osVersion=33&platform=A&relationship=&revenueTypes=%5B%22cpm%22%2C%22cpc%22%2C%22cpi%22%2C%22cpa%22%2C%22cpq%22%2C%22cpe%22%2C%22cpqlite%22%2C%22cpcquiz%22%2C%22cpy%22%2C%22cpk%22%2C%22cpl%22%2C%22cpinsta%22%2C%22cpyoutube%22%2C%22cpylike%22%2C%22cptiktok%22%2C%22cpnstore%22%5D&sdkVersion=41913&timezone=Asia%2FSeoul&types=%7B%22NATIVE%22%3A%5B%5D%2C+%22HTML%22%3A%5B%5D%2C+%22VAST%22%3A%5B%5D%2C+%22IMAGE%22%3A%5B%22FULLSCREEN%22%2C+%22INTERSTITIAL%22%2C+%22VERTICAL%22%5D%7D&unitId=131135271739720&userAgent=Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+13%3B+SM-A235N+Build%2FTP1A.220624.014%29&userId=uZEBRAe6vf0a_VWTxouTrzBtcMXmLpgQgwqIjRnXfH8"

unescpaed_url = html.unescape(allocation_url)
final_url = unescpaed_url[1:-1]


url_split_result = urlsplit(allocation_url)
print(f"url_split_result.path: {url_split_result.path}")
print(f"url_split_result.query: {parse_qsl(url_split_result.query)}")