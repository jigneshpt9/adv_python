import yaml 
with open("telnet_session.yml") as infile: 
    d = yaml.load(infile, Loader=yaml.CLoader) 
    
    
    