from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BackgroundScheduler
first = True
#def timedTask(x=''):
#    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
#
#if __name__ == '__main__':
#    print('77')
#    try:# 创建后台执行的 schedulers
#        scheduler = BackgroundScheduler()
#        print('77777')  
#    # 添加调度任务
#    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 6 小时
#        scheduler .add_job(timedTask, 'date', run_date='2021-1-25 22:17:00',args=['text'])
#        scheduler.add_job(timedTask, 'interval', seconds =3,args=['text'])
#    # 启动调度任务
#        scheduler.start()
#        print('77777')  
#    except (KeyboardInterrupt):
#        raise from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
import time
def job_func(text):
    first = False
    print(text)
if __name__ == '__main__':
    print(time.time())
    try:
        scheduler = BackgroundScheduler()
# 在 2017-12-13 时刻运行一次 job_func 方法
    #scheduler .add_job(job_func, 'date', run_date=date(2021, 1, 27), args=['text'])
# 在 2017-12-13 14:00:00 时刻运行一次 job_func 方法
#scheduler .add_job(job_func, 'date', run_date=datetime(2017, 12, 13, 14, 0, 0), args=['text'])
# 在 2017-12-13 14:00:01 时刻运行一次 job_func 方法
        
        if first:
            scheduler .add_job(job_func, 'date', run_date='2021-1-27 15:33:30', args=['text'])
            scheduler.start()
        else:
            scheduler.add_job(job_func, 'interval', seconds=15,args=['777'])
            scheduler.start()
        while True:
            time.sleep(60)
    except (KeyboardInterrupt):
        raise 