import requests,random


## function that gets the random quote
def get_random_quote():
	try:
		## making the get request
		response = requests.get("https://animechan.vercel.app/api/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['quote'];character=json_data['character'];anime=json_data['anime']

			## getting the quote from the data
			data=(data+'\n-'+character+'['+anime+']')
			print(data)
			return(data)
		else:
			return("Error while getting quote")
	except:
		return("Something went wrong! Try Again!")
