import urllib2,cookielib
import re
import ow
tt=ow.myscripts()

for i in xrange(len(tt.script)):
		site= "http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol={0}".format(tt.script[i])

		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8', 'Connection':'keep-alive'}

		req = urllib2.Request(site, headers=hdr)

		try:
			page = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
			print e.fp.read()

		content = page.read()
		match=re.search(r'("lastPrice"):(("\d+[,]\d*[.?]\d*")|("\d*[.?]\d*"))',content)

# following strips both single quotes and double quotes
		strip_string=match.group(2).strip('\'"') 
		pat=re.compile(r'\d\,')
		if pat.findall(strip_string):
			strip_string=strip_string.replace(",", "")

		tt.d[i].append(("CurrentValue", float(strip_string)))
		d1=float(tt.d[i][1][1])
		d2=float(tt.d[i][4][1])
		invt=reduce(lambda x,y:x*y,[d1,d2])
		tt.d[i].append(("CurrentInvst",invt))
print tt.d
Returns = 0
for i in xrange(len(tt.d)):
	Returns = Returns + tt.d[i][5][1]

print "Current value of Investment = ", Returns
