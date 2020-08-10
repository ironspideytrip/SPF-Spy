import optparse
import sys
import checkspf
import sendfakemail
def parsing():
	parser=optparse.OptionParser()
	parser.add_option("-d","--domain",dest="domain",help="domain to test on")
	parser.add_option("-l","--list",dest="domainlist",help="domains to test on")
	parser.add_option("-f","--file",dest="details",help="file containing details in order in separate lines namely api,gmail address to,password")
	(options,arguments)=parser.parse_args()
	return options
spf=parsing()
if not(spf.domain) and not(spf.domainlist):
	print("[!]Please specify a domain name or domain list")
	sys.exit()
if spf.domain and spf.domainlist:
	print("[!]You need only one , please specify only one switch")
	sys.exit()
if not(spf.details):
	print("[!]It seems you haven't specified details, so we can only check whether spf records exists or not but not send emails")
if spf.domain:
		check_spf_record=checkspf.Spfcheck(spf.domain)
		c=check_spf_record.checkspfdomain()
		if c and spf.details:
			print("[+]Now trying to send mail from the details given above")
			print("[+]If it fails , please cross check your details ")
			print("[+]Sending mail.....")
			with open(spf.details,"r") as details:
				data=details.read()
				details_list=list(data.split('\n'))
				print(details_list[0])
				print(details_list[1])
				print(details_list[2])
if spf.domainlist:
		with open(spf.domainlist,"r") as domainlist:
			for domain in domainlist:
				check_spf_record=checkspf.Spfcheck(domain.strip())
				c=check_spf_record.checkspfdomain()
					
		domainlist.close()
