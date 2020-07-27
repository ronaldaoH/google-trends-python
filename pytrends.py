from pytrends.request import TrendReq
import time
pytrend = TrendReq(hl='es-PE', tz=-300)

lista_keywords = [Sodimac','Nestlé','Gloria']

kw_list = [ 'Logo','marcas',' e commerce','Publicidad ']

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list= kw_list, cat=0, timeframe='now 1-d', geo='PE', gprop='')

#Interest Over Time
def interest_over_time_df(pytrend):
	interest_over_time_df = pytrend.interest_over_time()
	print(interest_over_time_df.head())

def related_queries_dict(pytrend):
	related_queries_dict = pytrend.related_queries()
	#print(related_queries_dict['Marketing Digital'])
	print("###INFO###")
	#print(related_queries_dict)
	print("### VALUES ###")
	#print(related_queries_dict.values())
	
	string_rpta = ''

	for item in related_queries_dict.items():
		print("ITEM####")

		print("CONSULTA :" + str(item[0]))
		string_rpta = string_rpta + '\n' + "CONSULTA :" + str(item[0]) + '\n'
		print("TOPP ##")
		print(item[1]["top"])
		string_rpta = string_rpta + '\n' + "TOP QUERIES: " + '\n'
		string_rpta = string_rpta + '\n' + str(item[1]["top"]) + '\n' 
		print("RISING ##")
		print(item[1]["rising"])
		string_rpta = string_rpta + '\n' + "RISING QUERIES : " + '\n'
		string_rpta = string_rpta + '\n' + str(item[1]["rising"]) + '\n'

	file = open('testfile.txt','w') 
	file.write(string_rpta)  
	file.close()
	return string_rpta

#NO HAY PERU
def trending_searches_df(pytrend, pais):
	# Get Google Hot Trends data
	trending_searches_df = pytrend.trending_searches(pn = pais)
	print(trending_searches_df.head())

#NO HAY PERU
def today_searches_df(pytrend):
	# Get Google Hot Trends data
	today_searches_df = pytrend.today_searches(pn = 'PE')
	print(today_searches_df)

def related_topics_dict(pytrend, kw):
	pytrend.build_payload(kw_list = kw, cat=0, timeframe='now 1-d', geo='PE', gprop='')
	related_topics = pytrend.related_topics()
	print("#RISING")
	print(related_topics)
	print("#TOPS")
	print(related_topics)
	

def top_charts(pytrend):
	# Get Google Top Charts
	top_charts_df = pytrend.top_charts(2018, hl='es-PE', tz=-300, geo='GLOBAL')
	print(top_charts_df.head())

def interest_by_region_df(pytrend):
	# Interest by Region
	interest_by_region_df = pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True)
	print(interest_by_region_df)

def suggestions_dict(pytrend, kw):
	# Get Google Keyword Suggestions
	suggestions_dict = pytrend.suggestions(keyword=kw)
	print(suggestions_dict)


def busqueda_tendencias(pytrend, kw):
	tendencia = pytrend.trending_searches(pn=False)
	print(tendencia)
