import subprocess


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         shell=True)
    return iter(p.stdout.readline, b'')


command = "echo -e 'GET' | openssl s_client -connect www.google.bg:443 -reconnect -no_ticket -tls1_2".split()
# for line in run_command(command):
#     print(line)

out = filter(lambda x: "Session-ID:" in x, run_command(command))
result = {}
for e in out:
    stripped = e.strip(b' \r\n')
    key, value = stripped.split(b':')
    result[key] = value

print(result)

# import re
# result = re.search(pattern="abcd", string="abc")
# print(result)

# import os
# os.system('echo -e "GET" | openssl s_client -connect www.google.bg:443 > tmp')
# print(open('tmp', 'r').read())