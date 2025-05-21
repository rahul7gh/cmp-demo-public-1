import argparse
import json
parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--ipaddress", type=str, help="ipaddress")
parser.add_argument("--machine_name", type=str, help="machine_name")

args = parser.parse_args()
output={"ipaddress":args.ipaddress,"machine_name":args.machine_name,"cpu":"16","memory":"16384MB","disk":"131072MB"}
print(json.dumps({"output":output}))


#python3 test.py --ipaddress=10.25.10.20 --machine_name=YOSH
