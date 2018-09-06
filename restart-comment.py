import subprocess

subprocess.run(['supervisorctl', 'restart', 'comment'], stdout=subprocess.PIPE)