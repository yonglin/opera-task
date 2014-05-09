def get_top10_domain(filename):
	'''return us the top-10 frequent domains from a file which stores
		email addresses'''

	import re

	def top10_domains(count_dict):
		'''return us the top-10 domains'''

		count_list = count_dict.items()
		count_list = sorted(count_list, key=lambda counts: counts[1], reverse = True)
		## sort the count_list
		
		nbr = len(count_list)
		n = min(nbr,10)
		## get how many domains we need to return

		return count_list[0:n]

	def count_domains(domain_list):
		'''we use a dictionary to store the counts,
		key is each domain and value is the counts'''

		domain_set = list(set(domain_list))
		## at first we transform the domain list as
		## a set and then we turn this set back to a list
		## for the coding convenience

		keys = domain_set
		values = [0]*len(domain_set)
		count_dict = dict(zip(keys, values))

		for domain in domain_list:
			count_dict[domain] += 1

		return count_dict


	def get_domain_list(address_list):
		'''get domain list from a email address list'''

		return [get_domain(address) for address in address_list]

	def get_domain(address):
		'''get domain from a email address'''

		#import re
		address = re.findall(r'\@(.*)', address)
		return address[0]

	def file_to_list(file_name):
		'''convert the file to a list'''

		with open(file_name,'rw') as f:
			emails = f.readlines()
		f.close()
		return emails

################# output ######################
	address_list = file_to_list(filename)
	domain_list = get_domain_list(address_list)
	count_dict = count_domains(domain_list)
	#return top10_domains(count_dict) or

	for item in top10_domains(count_dict):
		print item[0],item[1]
################# output ######################








