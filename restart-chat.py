import subprocess

subprocess.run(['supervisorctl', 'restart', 'chat'], stdout=subprocess.PIPE)
