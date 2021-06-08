def queryformer(request):
    searchtext = request.form['searchtext']
    kamalaharris = request.form['kamalaharris']
    realdonaldtrump = request.form['realdonaldtrump']
    narendramodi = request.form['narendramodi']
    joebiden = request.form['joebiden']
    piyushgoyal = request.form['piyushgoyal']
    rahulgandhi = request.form['rahulgandhi']
    matteosalvinimi = request.form['matteosalvinimi']
    berlusconi = request.form['berlusconi']
    giorgiameloni = request.form['giorgiameloni']
    corriere = request.form['corriere']
    matteorenzi = request.form['matteorenzi']
    cottarellicpi = request.form['cottarellicpi']
   
    english = request.form['english']
    hindi = request.form['hindi']
    italian = request.form['italian']
    India = request.form['India']
    USA = request.form['USA']
    Italy = request.form['Italy']
    poilist = []
    if kamalaharris == 'true':
        poilist.append('kamalaharris')
    if realdonaldtrump == 'true':
        poilist.append('realdonaldtrump')
    if rahulgandhi == 'true':
        poilist.append('rahulgandhi')
    if joebiden == 'true':
        poilist.append('joebiden')
    if matteorenzi == 'true':
        poilist.append('matteorenzi')
    
    if  matteosalvinimi== 'true':
      poilist.append('matteosalvinimi')
    if piyushgoyal == 'true':
      poilist.append('piyushgoyal')
    if corriere == 'true':
      poilist.append('corriere')
    if cottarellicpi == 'true':
      poilist.append('cottarellicpi')
    if giorgiameloni == 'true':
      poilist.append('giorgiameloni')
    if berlusconi == 'true':
      poilist.append('berlusconi')
    if narendramodi =='true':
        poilist.append('narendramodi')

    langlist = []
    if english == 'true':
        langlist.append('en')
    if hindi == 'true':
        langlist.append('hi')
    if italian == 'true':
        langlist.append('it')

    countrylist = []
    if India == 'true':
        countrylist.append('India')
    if USA == 'true':
        countrylist.append('USA')
    if Italy == 'true':
        countrylist.append('Italy')

    poicount = len(poilist)
    langcount = len(langlist)
    countrycount = len(countrylist)
    totalCount = poicount + langcount + countrycount

    query = ''

    if searchtext:
        #query += '(articles_:('
        query += searchtext 
        #+ '))'

    if totalCount > 0:
        count = 0
        if poicount > 0:
            query += ' AND(poi_name:('
        for poiname in poilist:
            query += poiname
            count += 1
            if count != poicount:
                query += ' OR '

        if poicount > 0:
            query += '))'
        totalCount -= poicount

    if totalCount > 0:
        count = 0
        if countrycount > 0:
            query += ' AND(country:('
        for country in countrylist:
            query += country
            count += 1
            if count != countrycount:
                query += ' OR '

        if countrycount > 0:
            query += '))'
        totalCount -= countrycount

    if totalCount > 0:
        count = 0
        if langcount > 0:
            query += ' AND(lang:('
        for lang in langlist:
            query += lang
            count += 1
            if count != langcount:
                query += ' OR '

        if langcount > 0:
            query += '))'
        totalCount -= langcount

    return query



      