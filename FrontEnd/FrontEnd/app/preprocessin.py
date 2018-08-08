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

import sqlite3
from pandas.io import sql
from app.models import *
from django.db import IntegrityError


# Create your connection.

def ConvertIptoNum(ip):
    try:
        #convert decimal dotted quad string to long integer
        return struct.unpack('>L',socket.inet_aton(ip))[0]
    except Exception:
        return int(hexlify(socket.inet_pton(socket.AF_INET6, ip)), 16)

def standardize():  
    print("********************************************")
    print("chiryo")
    print("********************************************")      
    #read the csv file        
    df = pd.read_csv('firewall2.csv', dtype=object )
    print(df)
    #drop the column if any value is missing
    #df= df.dropna(axis= "columns", how = "all", inplace=True)
    #drop unnecessary files
    df.drop(['tcpflags','size','tcpsyn','tcpack','tcpwin','icmptype','icmpcode','info'], axis =1, inplace = True)
    #drop any duplicate files
    #df.drop_duplicates(keep="first", inplace=True)

    print("dropped")

    #standardize action
    unique_action = df['action'].unique()
    for action in unique_action:
        if action == "ALLOW":
            df['action'] = df['action'].replace('ALLOW',0)
        if action == "DENY":
            df['action']=df['action'].replace("DENY",1)
        else:
            df['action']=df['action'].replace(action,-9999)
    print("action")
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
    print("protocol")
    #standardize path
    unique_path = df['path'].unique()
    for path in unique_path:
        if path == "RECEIVE":
            df['path'] = df['path'].replace('RECEIVE', 0)
        if path == "SEND":
            df["path"]=df['path'].replace('SEND',1)
        else:
            df["path"]=df['path'].replace(path,-9999)

    df['dst_port'] = df['dst_port'].replace('-', -99999)
    df['dst_port'] = df['dst_port'].apply(pd.to_numeric)
    df['src_port'] = df['src_port'].replace('-',-9999)
    df['src_port'] = df['src_port'].apply(pd.to_numeric)
    
    df['src_ip']=df['src_ip'].replace('-','0.0.0.0')
    df['dst_ip']=df['dst_ip'].replace('-','0.0.0.0')

    #check and find the risk factors first
    #use the convert ip to convert the IP to neumeric value
    

    df.dropna(inplace=True)
    #df.to_csv("firewall_standard.csv", index=False)
    cnx = sqlite3.connect("/home/shradha/virtualenvironment/ML/bin/Major project/FrontEnd/FrontEnd/db.sqlite3")

    df.to_sql(name="app_data_set", con = cnx, if_exists = "append", index=False)

  
def ip_to_num(latest_id):
    #convert IP to Num
    cnx = sqlite3.connect("/home/shradha/virtualenvironment/ML/bin/Major project/FrontEnd/FrontEnd/db.sqlite3")
    sql_ = """SELECT * FROM app_data_set WHERE id > (?)"""
    df = pd.read_sql(sql_,params = (latest_id,), con=cnx)
    
   # print(df)
    for ip in df["src_ip"]:
        ip_convert = ConvertIptoNum(ip)
        df["src_ip"]=df["src_ip"].replace(ip,ip_convert)

    for ip in df["dst_ip"]:
        ip_convert = ConvertIptoNum(ip)
        df["dst_ip"]=df["dst_ip"].replace(ip,ip_convert)

    df.drop(['date','time','src_port','dst_port'], axis =1, inplace = True)
     #normalize the values
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(df.drop("id", axis=1))
    df2 = pd.DataFrame(np_scaled)
    df2["data_set_id"] = df["id"]

    df2.columns = ["action_normal","protocol_normal","src_ip_normal","dst_ip_normal","path_normal","data_set_id"]
    df2.to_sql(name="app_data_set_normalized",if_exists = "append", con =cnx, index=False)
    
def convert_to_csv(filename_add, latest_id):
    #Convert the raw file to a csv file
    with open(filename_add, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(" ") for line in stripped if not line.startswith("#"))
        with open('firewall2.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('date','time','action', 'protocol' ,'src_ip', 'dst_ip', 'src_port', 'dst_port' ,'size' ,'tcpflags' ,'tcpsyn','tcpack', 'tcpwin', 'icmptype', 'icmpcode', 'info','path'
    ))
            writer.writerows(lines)
    standardize()  
    ip_to_num(latest_id)
    print("converted ip to num")
           
            



                    
                    
    
                
            



        







