import faceBookPoller
from apscheduler.schedulers.background import BlockingScheduler

scheduler = BlockingScheduler()

POLLING_INTERVAL = 60

task_to_do = faceBookPoller.poll()
lambda_poller = lambda :faceBookPoller.poll()

job = scheduler.add_job(lambda_poller, trigger='interval', seconds=POLLING_INTERVAL)
scheduler.start()

