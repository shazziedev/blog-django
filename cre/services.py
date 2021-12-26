import os
import requests



def get_api_data():
	url = "http://amasample.herokuapp.com/api/products/"
	r = requests.get(url,headers={'Authorization':'Bearer %s' % 'access_token'})
	dr = r.json()
	d_li = []
	for i in dr:
		d_li.append(dr)
		print(i)
	return d_li