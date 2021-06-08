import json
import urllib
#import urllib2
import datetime
import random

def facet_count(query, field):
    query = urllib.parse.quote(query)
    inurl = 'http://3.139.99.229:8983/solr/IRF20P1/select?facet.field=' + \
        field + '&facet=on&fl=' + field + '&indent=on&wt=json&q=text_translate%3A%20' + query
    print(inurl)
    data = urllib.request.urlopen(inurl)

    docs = json.load(data)['facet_counts']['facet_fields'][field]
    # print(docs)
    values = []
    labels = []
    dateset = {}
    size = len(docs)
    i = 0
    while i < size:
        if field == 'tweet_date':
            dateset[docs[i][0: 10]] = dateset.get(
                docs[i][0: 10], 0) + int(docs[i + 1])
            i = i + 2
        else:
            if int(docs[i + 1]) > 0:
                labels.append(docs[i])
                i = i + 1
                values.append(int(docs[i]))
                i = i + 1
            else:
                i = i + 2

    if field == 'tweet_date':
        for date in dateset.keys():
            labels.append(date)
            values.append(dateset[date])
        sort(labels, values)

    result = {}
    result['values'] = values
    result['labels'] = labels
    result['type'] = 'pie'
    return result


def sort(labels, values):
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            if labels[i] > labels[j]:
                temp = labels[i]
                labels[i] = labels[j]
                labels[j] = temp
                temp = values[i]
                values[i] = values[j]
                values[j] = temp

def facet_count_json(query, field):
    query = urllib.parse.quote(query)
    inurl = 'http://3.139.99.229:8983/solr/IRF20P1/select?facet.field=' + \
        field + '&facet=on&fl=' + field + '&indent=on&wt=json&q=*%3A' + query
    print(inurl)
    data = urllib.request.urlopen(inurl)

    docs = json.load(data)['facet_counts']['facet_fields'][field]
    # print(docs)
    values = []
    
    
    # size = len(docs)
    for i in range(0,len(docs),2):
        dataset = {}
        if docs[i] == 'none':
            continue
        dataset["label"] = docs[i]
        dataset["values"] = docs[i+1]
        values.append(dataset)
    # i = 0
    # while i < size:
    #     if field == 'tweet_date':
    #         dateset[docs[i][0: 10]] = dateset.get(
    #             docs[i][0: 10], 0) + int(docs[i + 1])
    #         i = i + 2
    #     else:
    #         if int(docs[i + 1]) > 0:
    #             labels.append(docs[i])
    #             i = i + 1
    #             values.append(int(docs[i]))
    #             i = i + 1
    #         else:

    #             i = i + 2

    # if field == 'tweet_date':
    #     for date in dateset.keys():
    #         labels.append(date)
    #         values.append(dateset[date])
    #     sort(labels, values)
    print(dataset)
    result = values
    return result

def facet_count_poi(query, field):
    query = urllib.parse.quote(query)
    inurl = 'http://3.139.99.229:8983/solr/IRF20P1/select?facet.field=' + \
        field + '&facet=on&fl=' + field + '&indent=on&wt=json&q=poi_name%3A' + query
    print(inurl)
    data = urllib.request.urlopen(inurl)

    docs = json.load(data)['facet_counts']['facet_fields'][field]
    # print(docs)
    
    
    
    # size = len(docs)
    dataset={}
    if len(docs)>0:
        dataset["poi"] = query
        dataset["non_covid"]=docs[1]//8
        dataset["covid"] = docs[3]
        

    # print(dataset)
    
    return dataset

def facet_count_date(field):
    query='tweet_date'
    query = urllib.parse.quote(query)
    dates=['2020-09-14','2020-09-15','2020-09-16','2020-09-17','2020-09-18','2020-09-19']
    values=[]
    for i in range(len(dates)-1):
        startdate =dates[i]
        enddate = dates[i+1]
        inurl = 'http://3.139.99.229:8983/solr/IRF20P1/select?facet.field='+\
            field+'&facet=on&fq=covid%3A%22covid%22&fq='+\
            query+'%3A%5B'+startdate+'T00%3A00%3A00Z%20TO%20'+\
            enddate+'T00%3A00%3A00Z%7D&q=*&sort='+query+'%20desc&wt=json'
        print(inurl)
        data = urllib.request.urlopen(inurl)

        docs = json.load(data)['facet_counts']['facet_fields'][field]
        print(docs)
        dataset = {}
        dataset['date']  = enddate
        for i in range(0,len(docs),2):
            if docs[i] == 'none':
                
                continue
            if docs[i+1]==0:
                #dataset[docs[i]] = random.randint(0,5)
                # dataset['date']  = startdate
                dataset[docs[i]] =  docs[i+1]
            else:
                dataset[docs[i]]=docs[i+1]
                
        values.append(dataset)

    # print(dataset)
    
    return values