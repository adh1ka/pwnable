import requests
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor

BACKEND_URI = "" # add backend uri here
FLAG_COLLECTOR_URI = "" # add flag collector uri here
USER_FLAG_GATEWAYS = [] # add user flag gateways here
ROOT_FLAG_GATEWAYS = [] # add root flag gateways here
Token = ""
AUTH_HEADER = {
    "Authorization": f"Bearer {Token}",
    "Content-Type": "application/json"
}

def get_ips():
    response = requests.get(f"{BACKEND_URI}/api/v1/teams/")
    return [team['server']['host'] for team in response.json()['data']]

def submit_flag(flag):
    response = requests.post(f"{BACKEND_URI}/api/v1/submit", headers=AUTH_HEADER, json={"flags": [flag]})
    pprint(response.text)

def exploit(ip, gateways):
    # Exploit Goes Here
    pass

def exploit_ips(ips, gateways):
    with ThreadPoolExecutor() as executor:
        executor.map(exploit, ips, [gateways] * len(ips))

if __name__ == "__main__":
    ips = get_ips()
    pprint(ips)
    requests.get(f"{FLAG_COLLECTOR_URI}/reset")
    exploit_ips(ips, USER_FLAG_GATEWAYS)
    exploit_ips(ips, ROOT_FLAG_GATEWAYS)
    flags = requests.get(f"{FLAG_COLLECTOR_URI}/flags").text.strip().split('\n')
    pprint(flags)
    response = requests.post(f"{BACKEND_URI}/api/v1/submit", headers=AUTH_HEADER, json={"flags": flags})
    pprint(response.json())

