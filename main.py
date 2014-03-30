import mechanize
import re
import time

browser = mechanize.Browser()
browser.set_handle_robots(False)

browser.addheaders = [('User-agent', 'Firefox')]
start = 0
search = "mail+list"
continuar = True
totalmails = 0;
links = []

print "Searching: \"" + search.replace("+", " ") + "\""

while continuar:
	
	browser.open("http://www.google.com/custom?q="+search+"&num=50&client=google-coop&cof=FORID:10%3BAH:left%3BCX:Pastebin%2520Active%3BL:http://www.google.com/intl/en/images/logos/custom_search_logo_sm.gif%3BLH:30%3BLP:1%3BKMBOC:%23336699%3B&cx=013305635491195529773:0ufpuq-fpt0&ad=n9&adkw=AELymgVBPYHfZ4WcVCYFfLq5clervq1_HY7Ez0uEwDzhZnk6zoQWyCOYOxP9p8JZwUPewRPIgg1SFZfYtHEktKv__e8TwMZExRwmm7QeHWN6EHsrbjGHFCY&hl=en&boostcse=0&prmd=ivns&ei=q9I1U8_qCtSa0gHo44DoAQ&start="+str(start)+"&sa=N")
	html = browser.response().get_data()


	for link in browser.links():
		if not "pastebin" in link.url:
			continue
		if link.url in links: 
			continuar = False
			break
		links.insert(0, link.url)

		try:
			resp = browser.follow_link( link )
			content = resp.get_data()
			match = re.findall(r'[\w\.-]+@[\w\.-]+', content)
			totalmails += len(match) 
			print str(totalmails);
			#print link.url
			#print match
			with open("list.txt", "a") as myfile:
		    		myfile.writelines(x+'\n' for x in match)
		except: 
  			pass
		with open("control.txt", "a") as myfile:
	    		myfile.write(str(link.url)+'\n')
			#myfile.write("\n")

	start += 50

	time.sleep(5)

print "Finished"

