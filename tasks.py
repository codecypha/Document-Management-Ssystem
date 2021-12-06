import schedule
from dms.models import Department
import time

def job():
    print("I am working ...")
    
schedule.every(10).seconds.do(job)
#schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().monday.at("10:30").do(job)
# schedule.every().minute.at(":17").do(job)
depart = Department.objects.all()
for i in depart:
    print(i)

while 1:
    schedule.run_pending()
    time.sleep(1)