#Solution of Metadata extraction of EC2 using Boto3 module of Python
#Will be printing instance details in JSON formatted output and extracting individual meta data of EC2 instance and upload them to a CSV

import boto3
import pprint
import csv

session = boto3.Session(profile_name='profile_value', region_name="us-east-1")
ec2 = session.client(service_name='ec2')

#Will print the json formatted output for all the instances on AWS cloud
pprint(ec2.describe_instances())

#Header for writing all instance meta data into once CSV file
header_csv = ['S_No', 'Instance_ID','EC2 Name','env','Instance Type', 'IP Address', 'Availability Zone', 'EBS Volume','Security Groups']

fo = open("CSV_file_path_where_it_needs to be saved","w")
csv_w = csv.writer(fo)
csv_w.writerow(header_csv)

SN = 0

for each in ec2.describe_instances()['Reservations']:  
   
   for each_instance in each['Instances']:
      
      
#Fetch Image ID of EC2      
      Image_Id = each_instance['ImageId']
      
#Fetch Instance ID of EC2    
      Instance_Id = each_instance['InstanceId']
      
#Fetch Instance type of EC2      
      Instance_Type = each_instance['InstanceType']
      
#Fetch state of EC2      
      State = each_instance['State']['Name']
      
#Fetch Private IP address of EC2 
      IP_addr = each_instance['PrivateIpAddress']
      
#Fetch Subnet ID of EC2 
      Subnet_Id = each_instance['SubnetId']
      
#Fetch Availability Zone of EC2 
      Availability_Zone = each_instance['Placement']['AvailabilityZone']
      
#Fetch the values of EC2 tags

      EC2_Name_Tag = [each_tag['Value'] for each_tag in each_instance['Tags'] if each_tag['Key']=='Name']
      env_type = [each_tag['Value'] for each_tag in each_instance['Tags'] if each_tag['Key']=='environment-type']
      
#Fetch all the security groups

      SecurityGroups = []
      
      for each_SecurityGroup in each_in['SecurityGroups']:
        SecurityGroups.append(each_SecurityGroup['GroupName'])
        
#Fetch all the Volume details attached to EC2  
 
      Volumes = []
      
      for each_Volume in each_in['BlockDeviceMappings']:
        Volumes.append((each_Volume['DeviceName'],each_Volume['Ebs']['VolumeId']))

#Will insert the row into CSV file    
  
      SN = SN+1
      csv_w.writerow([SN, Instance_Id , EC2_Name_Tag , env_type , Instance_Type , IP_addr, Availability_Zone, Volumes,SecurityGroups])
      
