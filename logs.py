#!/usr/bin/env python

import psycopg2
DB_NAME = "news"


# Question 1) What are the most popular 3 articles of all time?
queryq1 = "SELECT title, views from article_view limit 3"

# Question 2) Who are the most popular article authors of all time?
queryq2 = """
			SELECT authors.name, sum(article_view.views) AS views
			FROM article_view, authors WHERE authors.id = article_view.author
			GROUP BY authors.name
			ORDER BY views DESC
			"""

# Question 3) On which days did more than 1% of requests lead to errors?
queryq3 = "SELECT * FROM error_log_views WHERE \"Percent Error\" > 1"

# Results
queryq1_result = dict()
queryq1_result['title'] = "\n1. The 3 most popular articles of all time are:\n"

queryq2_result = dict()
queryq2_result['title'] = """
						\n2. 
						The most popular article authors of all time are:\n
						"""

queryq3_result = dict()
queryq3_result['title'] = """
						\n3. 
						Days with more than 1% of request 
						that lead to an error:\n
						"""

def connect(query):
	try:
		db = psycopg2.connect(database=DB_NAME)
		c = db.cursor()
		c.execute(query)
		results = c.fetchall()
		db.close()
		return results
	except:
		print("<Error: Unable to communicate with database.>")

def queryResults(query_result):
	print (query_result['title'])
	for result in query_result['results']:
		print ('\t' + str(result[0]) + ' (' + str(result[1]) + ' views)')

def errorQueryResults(query_result):
	print (query_result['title'])
	for result in query_result['results']:
		print ('\t' + str(result[0]) + ' (' + str(result[1]) + ' %)')

queryq1_result['results'] = connect(queryq1)
queryq2_result['results'] = connect(queryq2)
queryq3_result['results'] = connect(queryq3)

queryResults(queryq1_result)
queryResults(queryq2_result)
errorQueryResults(queryq3_result)