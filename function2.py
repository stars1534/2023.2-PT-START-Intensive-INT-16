import json

###Required function###

def vulners(report_f_name, vulners_f_name): #2 params for function, report file name and output file name

    with open(report_f_name, 'r') as f: #Open and read data from the report file
        output_info = json.load(f)

    vulners_list = [] #Empty list for adjusted vulners data

    alerts_list = output_info['site'][0]['alerts'] #Vulners data list of alerts key from the report file

    for alert in alerts_list:
        vulners_dict = {'name': alert['name'], 'count': alert['count']} #Read values of the needed keys from alerts dicts and add in the new dict
        vulners_list.append(vulners_dict) #Add dicts to the list

    vulners_info = {'vulnerabilities': vulners_list} #Template for the output file

    with open(vulners_f_name, 'w') as f:
        json.dump(vulners_info, f, indent = 4) #Add data to the output file

###Demo code###

report_f_name = '/home/kali/report.json'
vulners_f_name = '/home/kali/vulners.json'

#report_f_name = input('Type ZAP report file name: ')
#vulners_f_name = input('Type Vulners file name: ')

vulners(report_f_name, vulners_f_name)

with open(vulners_f_name, 'r') as f:
    output_info = json.load(f)

print(output_info) #Checking data from the output file