from apscheduler.schedulers.blocking import BlockingScheduler
from image_edit import render_image
def final_call():
    render_image()

scheduler = BlockingScheduler()
scheduler.add_job(final_call, 'interval', seconds=10)
scheduler.start()