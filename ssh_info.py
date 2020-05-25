ssh_info = [
    {   "hostname": "10.197.104.150",
        "port": 22,
        "username": "ubuntu",
        "password": "ubuntu@123",
        "commands": [
            "uptime",
            "uname -a",
            "date" ]
    },

    {   "hostname": "10.197.104.151",
        "port": 22,
        "username": "ubuntu",
        "password": "ubuntu@123",
        "commands": [
            "cat /etc/passwd",
            "cat /proc/loadavg",
            "uptime" ]
    },
]

def ssh_run(ssh_info):
    import paramiko
    from paramiko import SSHClient
    hosts = []
    
    for item in ssh_info:
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #client.invoke_shell()
        client.connect(item['hostname'],username=item['username'], password=item['password'], port=22)
        hosts.append(client)
    
    print("running command on host")
    stdin,stdout,stderr = hosts[0].exec_command('ls /etc')
    for line in stdout:
        print('... ' + line.strip('\n'))
    hosts[0].close()
    
if __name__ == '__main__':
    '''
    for host, result in ssh_run(ssh_info):
        for command, stdin, stdout, stderr in result:
            print(f"host: {host}, command: {command}")
            for line in stdout:
                print(line)
            print("-" * 60)
    '''
    ssh_run(ssh_info)