import subprocess
import time

subprocess.run(['pkill', 'firefox'], stdout=subprocess.PIPE)
subprocess.run(['pkill', 'Xvfb'], stdout=subprocess.PIPE)
subprocess.run(['pkill', 'geckodriver'], stdout=subprocess.PIPE)

subprocess.run(['supervisorctl', 'stop', 'all'], stdout=subprocess.PIPE)

time.sleep(5)
subprocess.run(['supervisorctl', 'restart', 'all'], stdout=subprocess.PIPE)
