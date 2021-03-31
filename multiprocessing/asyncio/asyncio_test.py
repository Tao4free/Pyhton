from google.cloud import bigquery
import time
import asyncio

client = bigquery.Client()

query1 = """
SELECT
  language.name,
  avg(language.bytes) as nihao
FROM `bigquery-public-data.github_repos.languages`
, UNNEST(language) AS language
GROUP BY language.name
"""

query2 = """
SELECT
  language.name,
  avg(language.bytes) as wohao
FROM `bigquery-public-data.github_repos.languages`
, UNNEST(language) AS language
GROUP BY language.name
"""

queries = [query1, query2]
job_config = bigquery.QueryJobConfig(use_query_cache=False)


def normal_run():
    for query in queries:
        job = client.query(query, job_config=job_config)
        job.result()


def run(q, job_config):
    job = client.query(q, job_config=job_config)
    job.result()


async def run_query(q):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, run, q, job_config)


def async_run():
    loop = asyncio.get_event_loop()
    gather = asyncio.gather(
        *[run_query(q)
          for q in queries],
    )
    loop.run_until_complete(gather)


def start():
    start_time = time.time()
    normal_run()
    print("--- normal run costs %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    async_run()
    print("--- async  run costs %s seconds ---" % (time.time() - start_time))


start()
