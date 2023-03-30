import os
import time
# str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
# os.system(f'git add . && git commit -m"Updated files: {today}" && git push origin main')
today =format(time.strftime("%Y/%m/%d %H:%M:%S"))
print(today)

os.system(f'cd {os.path.dirname(__file__)}../')

print(' ')
print('-- git add . -----------------------------------------------------------------------------')
print(' ')
os.system(f'git add . ')
print(f'git add . run')
print(' ')
print('-- git commit -m"" -----------------------------------------------------------------------')
print(' ')
os.system(f'git commit -m"Updated files: {today}"')
print(' ')
print('-- git push origin main ------------------------------------------------------------------')
print(' ')
os.system(f'git push origin main')
print(' ')
print('------------------------------------------------------------------------------------------')

#  git add . && git commit -m"Update files" && git push origin main
# os.system(f'cd  && git add . && git commit -m"Update files" && git push origin main')