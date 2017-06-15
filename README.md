# Log Analysis Project
Author: Rigoberto J Gort
Date: 06/14/2017

## Project Info
**Filename**

README.md

**Main Project File**

`logs.py`

**Connected Module Files**

`newsdata.sql`

### Configuration Instructions
`logs.py`

This is the primary file for answering the project questions.

The file utilizes queries in order to pull data from the database to answer the questions.

`newsdata.sql`

I configured the file to include the following SQL commands,

```
-- Drops news database if it exists
drop database if exits news;

-- Create news database
create database news;

-- Connect to the news database
\c news

-- Create Article Views
CREATE VIEW article_view AS
    SELECT title, author, count(*) AS views
    FROM articles, log WHERE log.path like concat('%', articles.slug)
    GROUP BY articles.title, articles.author
    ORDER BY views DESC;

-- Create Error Log Views
CREATE VIEW error_log_views AS
    SELECT date(time), round(100.0*sum(case log.status WHEN '200 OK' THEN 0 ELSE 1 END)/count(log.status), 2) as "Percent Error"
    FROM log
    GROUP BY date(time)
    ORDER BY "Percent Error" DESC;
```

### Operating Instructions
Please confirm that you have the following installed on your machine:

- Vagrant
- Virtual Box
- Python
- PostgreSQL

For example, if you are using the standard Python IDLE  (GUI) then you would open the file in that environment. 

1. Verify that you have the required files installed in a directory of your choosing.
2. Verify that you are in that directory and run `vagrant up` in the CMD or Terminal.
3. Enter `vagrant ssh`.
4. Change directories until you reach the logs-analysis-project directory.
5. Once there make sure to run the `psql` command.
6. After that just run the `\i newsdata.sql`. This will import the database for usage.
7. Exit the `psql` terminal and run the `python logs.py` command next.
8. Once it has completed running it will display the desired results that pertain to the project questions.