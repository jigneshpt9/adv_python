from pssh.config import HostConfig
from pssh.clients import ParallelSSHClient
from gevent import joinall

hosts = ['10.197.104.150',
         '10.197.104.151',
         '10.197.104.152',
         '10.197.104.153',
            '10.197.104.154',
            '10.197.104.155',
            '10.197.104.156',
            '10.197.104.158',
            '10.197.104.159',
            '10.197.104.160',
            '10.197.104.161',
            '10.197.104.162',
            '10.197.104.163',
            '10.197.104.165',
            '10.197.104.166',
            '10.197.104.168',
            '10.197.104.169',
            '10.197.104.170',
            '10.197.104.171',
            '10.197.104.172',
            '10.197.104.173',
            '10.197.104.174',
            '10.197.104.175',
            '10.197.104.176',
            '10.197.104.177',
            '10.197.104.178',
            '10.197.104.179',
            '10.197.104.180',
            '10.197.104.182',
            '10.197.104.184',
            '10.197.104.185',
            '10.197.104.186',
            '10.197.104.187',
            '10.197.104.188',
            '10.197.104.189',
  ]

host_config = [ HostConfig(port=22, user='pnpscale',
               password='pnpscale') ]*len(hosts)
client = ParallelSSHClient(hosts, host_config=host_config)
output=client.run_command('docker rm -f `docker ps -qa`;pkill pnp_scale;docker network prune -f;rm -rf /tmp/*')
'''
output=client.run_command('reboot')
output = client.run_command('reboot', sudo=True)
for host_out in output:
    host_out.stdin.write('pnpscale\n')
    host_out.stdin.flush()
client.join(output)
'''
for host_out in output:
    for line in host_out.stdout:
      print(line)
    exit_code = host_out.exit_code

#output=client.run_command('')
