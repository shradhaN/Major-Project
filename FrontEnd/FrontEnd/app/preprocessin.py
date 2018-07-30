#preprocessing script from raw_data to normalized text
# Log Features to neumeric
# Action

#     ALLOW = 0
#     DENY = 1
#     INFO-EVENTS-LOST = -9999

# Protocol

# Unique items ('UDP', 'TCP', 'ICMP', '2', '-')
# LET US SUPPOSE THAT THE 2 AND - ARE ANOMALIES AND TO BE IGNORED

#     UDP = 0
#     TCP = 1
#     ICMP = 2
#     2, - = -9999

# Path

#  Unique items were ('RECEIVE','SEND','-')
#  LET US SUPPOSE - IS ANNOMALY AND IGNORE IT 

#     RECEIVE = 0
#     SEND = 1
#     '-' = -9999

# Src-port and dst-port

# The values were left as it is but convert to neumeric

#     '-' was converted to -99999

# Src-ip and dst-ip

# Converted to integer value using the ipaddress module
# the Ipv4 converted from Quad value and Ipv6 convertes using the IPv6 converter


import numpy as np
import pandas as pd
import csv
import socket, struct
from binascii import hexlify
from sklearn import preprocessing


def ConvertIptoNum(ip):
    try:
        #convert decimal dotted quad string to long integer
        return struct.unpack('>L',socket.inet_aton(ip))[0]
    except Exception:
        return int(hexlify(socket.inet_pton(socket.AF_INET6, ip)), 16)


    
def convert_to_csv():
    #Convert the raw file to a csv file
    with open('firewall.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(" ") for line in stripped if line)
        with open('firewall2.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('date','time','action', 'protocol' ,'src-ip', 'dst-ip', 'src-port', 'dst-port' ,'size' ,'tcpflags' ,'tcpsyn','tcpack', 'tcpwin', 'icmptype', 'icmpcode', 'info','path'
    ))
            writer.writerows(lines)
            
            
def standardize():        
    #read the csv file        
    df = pd.read_csv('firewall2.csv', dtype=object )
    #drop the column if any value is missing
    #df= df.dropna(axis= "columns", how = "all", inplace=True)
    #drop unnecessary files
    df.drop(['tcpflags','size','tcpsyn','tcpack','tcpwin','icmptype','icmpcode','info'], axis =1, inplace = True)
    #drop any duplicate files
    df.drop_duplicates(keep="first", inplace=True)

    #standardize action
    unique_action = df['action'].unique()
    for action in unique_action:
        if action == "ALLOW":
            df['action'] = df['action'].replace('ALLOW',0)
        if action == "DENY":
            df['action']=df['action'].replace("DENY",1)
        else:
            df['action']=df['action'].replace(action,-9999)

    #standardize protocol
    unique_protocol = df['protocol'].unique()
    for protocol in unique_protocol:
        if protocol == "UDP":
            df['protocol'] =  df['protocol'].replace('UDP', 0)
        if protocol == "TCP":
            df['protocol'] =  df['protocol'].replace('TCP', 1)
        if protocol == "ICMP":
            df['protocol'] =  df['protocol'].replace('ICMP', 2)
        else:
            df['protocol'] =  df['protocol'].replace(protocol, -9999)

    #standardize path
    unique_path = df['path'].unique()
    for path in unique_path:
        if path == "RECEIVE":
            df['path'] = df['path'].replace('RECEIVE', 0)
        if path == "SEND":
            df["path"]=df['path'].replace('SEND',1)
        else:
            df["path"]=df['path'].replace(path,-9999)

    df['dst-port'] = df['dst-port'].replace('-', -99999)
    df['dst-port'] = df['dst-port'].apply(pd.to_numeric)
    df['src-port'] = df['src-port'].replace('-',-9999)
    df['src-port'] = df['src-port'].apply(pd.to_numeric)
    
    df['src-ip']=df['src-ip'].replace('-','0.0.0.0')
    df['dst-ip']=df['dst-ip'].replace('-','0.0.0.0')

    #check and find the risk factors first
    #use the convert ip to convert the IP to neumeric value
    
    df.dropna(inplace=True)
    df.to_csv("firewall2.csv",index=False)


def ip_to_num():
    #convert IP to Num
    with open('firewall2.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        i = 1
        naya_ip=[]

        counter = 0
        print(len(your_list))
        print("**************")
        for i in range(1,len(your_list)):
            #your_list[i][0]    
            
            new_ip_src=ConvertIptoNum(your_list[i][4])
            new_ip_dst=ConvertIptoNum(your_list[i][5])

            #naya_ip.append(new_ip)
            with open('firewall_neumeric.csv','a') as w:
                counter = counter + 1
                c = csv.writer(w) 
                #change this as the csv file is different due to the presence of date and time
                #uta check garera halne yeta
                #does not include the risk-factors---- must
                value = [your_list[i][0],your_list[i][1],your_list[i][2],your_list[i][3],new_ip_src,new_ip_dst,your_list[i][6],your_list[i][7],your_list[i][8]]
                #c.writerow(('date','time','action','protocol','src-ip','dst-ip','src-port','dst-port'))
                c.writerow(value)
        print("rows")
        print(counter)

def normalixe():
    df2=pd.read_csv("firewall_neumeric.csv", names =['date','time','action','protocol','src-ip','dst-ip','src-port','dst-port','path'])
    
    print(list(df2))
    #df2['src-ip-risk-factor'] = df2['src-ip-risk-factor'].apply(pd.to_numeric)
    #df2['dst-ip-risk-factor'] = df2['dst-ip-risk-factor'].apply(pd.to_numeric)
    #df2['total-risk-factor']=df2['totoal-risk-factor'].apply(pd.to_neumeric)
    df2['src-port']=df2['src-port'].apply(pd.to_numeric)
    df2['dst-port']=df2['dst-port'].apply(pd.to_numeric)
    df2.drop(['date','time'], axis =1, inplace = True)

    #normalize the values
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(df2)
    df = pd.DataFrame(np_scaled)
    
    df['src-ip-risk-factor']=""
    df['dst-ip-risk-factor']=""
    df['total-risk-factor']=""
    df.to_csv("final_data_set.csv",index=False)
                    
                    
convert_to_csv()
print("converted to csv")
standardize()
print("standardized")
ip_to_num()
print("converted ip to num")
normalixe()
print("completed")
                    
        

                    
                    
    
                
            



        







