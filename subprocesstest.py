import subprocess

print('$ nslookup www.liuxv.cn')

r=subprocess.call(['nslookup','www.liuxv.cn'])
print('Exit code:',r)

