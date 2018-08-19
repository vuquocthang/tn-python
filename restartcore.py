import subprocess
import time

subprocess.run(['pkill', 'firefox'], stdout=subprocess.PIPE)
subprocess.run(['pkill', 'Xvfb'], stdout=subprocess.PIPE)
subprocess.run(['pkill', 'geckodriver'], stdout=subprocess.PIPE)

subprocess.run(['supervisorctl', 'stop', 'all'], stdout=subprocess.PIPE)

time.sleep(5)
subprocess.run(['supervisorctl', 'restart', 'all'], stdout=subprocess.PIPE)
<<<<<<< HEAD

=======
>>>>>>> fe45538839ec3ad19d0d3f68e6f16e124e7e4624
