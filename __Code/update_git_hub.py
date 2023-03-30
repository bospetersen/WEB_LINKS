import os

import datetime
today = datetime.date.today()
print(today)

os.system(f'cd {os.path.dirname(__file__)}../')
os.system(f'git add . && git commit -m"Update files: {today}" && git push origin main')

#  git add . && git commit -m"Update files" && git push origin main
# os.system(f'cd  && git add . && git commit -m"Update files" && git push origin main')