from flask import Flask,request,render_template,jsonify
import json_to_trec
import datetime
import QueryFormer
import FacetCount

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods= ['POST'])
def process():
    query = QueryFormer.queryformer(request)
    if query:
        tweets = json_to_trec.functionName(query)
        field = request.form['analysis']
        count = FacetCount.facet_count(query, field)
        #print(tweets)
        print(count,query,field)
        result = {}
        result['tweets'] = tweets
        result['count'] = count
        
        return result
    return jsonify({'error' : 'Missing data!'})

@app.route('/overview', methods = ['GET'])
def overview_get():
    return render_template('overview.html')

@app.route('/overview',methods= ['POST'])
def overview():
    # query = QueryFormer.queryformer(request)
    query ='*'
    
    results = {}
    fields = ['poi_name','lang','Topic','country','sentiment']
    for field in fields:
        # tweets = json_to_trec.overviewall(query)
        count = FacetCount.facet_count_json(query, field)
        #print(tweets)
        #print(count,query,field)
        # result={}
        #result['tweets'] = tweets
        # result['count'] = count
        results[field] = count
    poi = results['poi_name']
    poi_covid_tweets = []
    datax = FacetCount.facet_count_date('poi_name')
    poi_USA =['joebiden','kamalaharris','realdonaldtrump','statedept','cdcgov']
    poi_India=['jagrannews','hindinews18','rahulgandhi','narendramodi','pibhindi','piyushgoyal','navbharattimes','mib_hindi']
    poi_Italy =['matteosalvinimi','berlusconi','giorgiameloni','corriere','ministerosalute','matteorenzi','cottarellicpi']
    count_USA = 0
    count_India =0
    count_Italy =0
    count_covid_USA =0
    count_covid_India=0
    count_covid_Italy=0
    covid_c =[]
    covid_c1 ={}
    covid_c2 ={}
    covid_c3 ={}
    for i in range(len(poi)):
        poi_name=poi[i]['label']
        countx = poi[i]['values']
        

        count1 = FacetCount.facet_count_poi(poi_name, 'covid')
        if poi_name in poi_USA:
            count_USA+=countx
            count_covid_USA+=count1['covid']
        elif poi_name in poi_India:
            count_India+=countx
            count_covid_India+=count1['covid']
        elif poi_name in poi_Italy:
            count_Italy+=countx
            count_covid_Italy+=count1['covid']
        poi_covid_tweets.append(count1)
    covid_c1['country'] ="USA"
    covid_c1['covid'] =6*count_covid_USA
    covid_c1['non_covid'] =2*count_USA - count_covid_USA
    covid_c2['country'] ="India"
    covid_c2['covid'] =5*count_covid_India
    covid_c2['non_covid'] =count_India - count_covid_India
    covid_c3['country'] ="Italy"
    covid_c3['covid'] =8*count_covid_Italy
    covid_c3['non_covid'] =count_Italy - count_covid_Italy
    covid_c.append(covid_c1)
    covid_c.append(covid_c2)
    covid_c.append(covid_c3)
    
    results['covid'] = poi_covid_tweets
    results['covid_country']=covid_c
    results['covid_date'] = datax
    print('results ------')
    print(results['covid_date'])
    print('results ------')
    return results
    # return jsonify({'error' : 'Missing data!'})


if __name__ == '__main__':
    app.run(debug=True)
