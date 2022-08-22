from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.job import Job
from pytz import utc

from foo.foo import fooFunc



def main():
    jobstores = {
        'default': SQLAlchemyJobStore(url='postgresql+psycopg2://admin:password@localhost:5432/jira_metrics'),
        'postgres': SQLAlchemyJobStore(url='postgresql+psycopg2://admin:password@localhost:5432/jira_metrics_2')
    }
    executors = {
        'default': ThreadPoolExecutor(20)
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 1
    }
    scheduler = BlockingScheduler(jobstores=jobstores, job_defaults=job_defaults, executors=executors, timezone=utc)

    job = scheduler.add_job(fooFunc, 'interval', seconds=5, id='interval_5', jobstore='default')
    # job = scheduler.get_job(job_id='interval_5', jobstore='postgres')
    print(job)

    # print('Job is ' + 'None' if not job else job)
    print(scheduler.get_jobs(jobstore='default'))

    scheduler.start()

if __name__ == "__main__":
    main()

