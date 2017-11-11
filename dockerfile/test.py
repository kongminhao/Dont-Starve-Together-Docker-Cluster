import re
server_conf = 'ServerModSetup("{}")'
pattern = re.compile('workshop-(\d+)')
server_conf_filecontent = ''
with open('modoverrides.lua','r') as f:
    file = f.read()
    mod_id_list = pattern.findall(file)
    for each in mod_id_list:
        server_conf_filecontent= server_conf_filecontent + server_conf.format(each) +'\n'

with open("dedicated_server_mods_setup.lua", 'w') as f:
    f.write(server_conf_filecontent)


