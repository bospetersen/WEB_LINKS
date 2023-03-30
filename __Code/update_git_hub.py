import os
import time
# str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
today =format(time.strftime("%Y/%m/%d %H:%M:%S"))
print(today)

os.system(f'cd {os.path.dirname(__file__)}../')
os.system(f'git add . && git commit -m"Updated files: {today}" && git push origin main')

#  git add . && git commit -m"Update files" && git push origin main
# os.system(f'cd  && git add . && git commit -m"Update files" && git push origin main')