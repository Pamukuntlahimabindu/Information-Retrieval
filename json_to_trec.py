import json 
import urllib
#import urllib2
import datetime

def functionName(query):
	query = urllib.parse.quote(query)
	#inurl = 'http://3.139.99.229:8983/solr/IRF20P1/select?q=' + query + '&rows=100&wt=json'
	inurl='http://3.139.99.229:8983/solr/IRF20P1/select?q=text_translate%3A'+query+'&sort=influence_score%20desc&rows=500'
	print (inurl)
	data = urllib.request.urlopen(inurl)
	docs = json.load(data)['response']['docs']
	result = []
	for doc in docs:
		jsondata = {}
		jsondata['tweet_text'] = doc['full_text'][0]
		jsondata['username'] = doc['user.name'][0]
		jsondata['image_url'] = doc['user.profile_image_url'][0]
		jsondata['tweet_id'] = doc['id']
		jsondata['verified']=doc['user.verified'][0]
		jsondata['sentiment']=doc['Sentiment'][0]
		jsondata['articles'] =  doc["articles"]
		jsondata['influence_score'] =doc["influence_score"][0]
		result.append(jsondata)
		
	return result


def overviewall(query):
	query = urllib.parse.quote(query)
	#inurl = 'http://3.139.99.229:8983/solr/IRF20P1/select?q=' + query + '&rows=100&wt=json'
	inurl='http://3.139.99.229:8983/solr/IRF20P1/select?q=text_translate%3A'+query
	print (inurl)
	data = urllib.request.urlopen(inurl)
	docs = json.load(data)['response']['docs']
	result = []
	for doc in docs:
		jsondata = {}
		jsondata['tweet_text'] = doc['full_text'][0]
		jsondata['username'] = doc['user.name'][0]
		jsondata['image_url'] = doc['user.profile_image_url'][0]
		jsondata['tweet_id'] = doc['id']
		#jsondata['articles'] =  doc.get('articles_', [""])[0]
		result.append(jsondata)
	return result