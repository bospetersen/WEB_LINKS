import os
import time

today =format(time.strftime("%Y/%m/%d %H:%M:%S"))

os.system(f'cd {os.path.dirname(__file__)}../')

print('\n-- git add . -----------------------------------------------------------------------------\n')
os.system(f'git add . ') 
print(f'git add .')
print(f'\n-- git commit -m"Updated files: {today}" ------------------------------------------------\n')
os.system(f'git commit -m"Updated files: {today}"')
print('\n-- git push origin main ------------------------------------------------------------------\n')
os.system(f'git push origin main')
print('\n------------------------------------------------------------------------------------------\n')
