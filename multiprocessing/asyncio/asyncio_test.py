from google.cloud import bigquery
import time
import asyncio
from google.cloud.exceptions import NotFound

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
FROM `bigquery-public-data.github_repos.languages3`
, UNNEST(language) AS language
GROUP BY language.name
"""

queries = [query1, query2]
job_config = bigquery.QueryJobConfig(use_query_cache=False)

awaiting_jobs = set()

def callback(future):
    try:
        future.result()
    except NotFound as e:
        print('Catch not found succeeded!')
    except Exception as e:
        print(repr(e))
    awaiting_jobs.discard(future.job_id)


def normal_run():
    for query in queries:
        job = client.query(query, job_config=job_config)
        job.result()

def normal_run_no_result():
    for query in queries:
        job = client.query(query, job_config=job_config)
        awaiting_jobs.add(job.job_id)
        job.add_done_callback(callback)

    while awaiting_jobs:
        # print('waiting for jobs to finish ... sleeping for 1s')
        time.sleep(0.1)

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
    # start_time = time.time()
    # normal_run()
    # print("--- normal run costs %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    normal_run_no_result()
    print("--- normal without result run costs %s seconds ---" % (time.time() - start_time))
    # start_time = time.time()
    # async_run()
    # print("--- async  run costs %s seconds ---" % (time.time() - start_time))


start()
