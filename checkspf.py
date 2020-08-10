import requests
import re
import sys
class Spfcheck:

	def __init__(self,domain):
		self.domain=domain
	def checkspfdomain(self):
		try:
			entry={"serial":"fred12","domain":self.domain}
	    		response=requests.post("https://www.kitterman.com/spf/getspf2.py",data=entry,timeout=3)
		except requests.exceptions.ConnectTimeout:
			print("[!]Connection timed out, please check connection")
			sys.exit()
		if re.search("Found v=spf1 record",response.content)==None:
			print("[+]There doesn't seem to be a spf record for "+self.domain)
			return 0	
		else:
			print("[!]Oops,there seems to be a spf record for "+self.domain)	
			return 1


