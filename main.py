import time
import os
import subprocess

SECOND_INTERVAL = 600
ATTACKING_TIME = 60

start_time = time.time()
last_attack = start_time

def attack():
	for exp in os.listdir('./exploits'):
		for i in range(1, 12):
			subprocess.Popen(['python', './exploits/' + exp, str(i)], stdout=open(exp+'.fwpganteng', 'a'))


while True:
	print 'Attacking {}'.format(time.time())
	attack()
	time.sleep(SECOND_INTERVAL - ATTACKING_TIME)
	while last_attack + SECOND_INTERVAL > time.time():
		pass
	last_attack += SECOND_INTERVAL
