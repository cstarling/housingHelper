import sched, time
import faceBookPoller
from apscheduler.schedulers.background import BlockingScheduler
import emailSender


import atexit

def exit_handler():
    print 'My application is ending!'
    emailSender.shutDown()

atexit.register(exit_handler)

scheduler = BlockingScheduler()




POLLING_INTERVAL = 60

task_to_do = faceBookPoller.poll()
lambda_poller = lambda :faceBookPoller.poll()

#job = sched.add_interval_job(task_to_do, minutes=1, args=['text'])
job = scheduler.add_job(lambda_poller, trigger='interval', seconds=POLLING_INTERVAL)
scheduler.start()

