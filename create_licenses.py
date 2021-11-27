from datetime import datetime, timedelta
import jwt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--client", help="Name of the client", type=str)
parser.add_argument("-d", "--days_to_expire", help="Expiration days", type=int)
args = parser.parse_args()

SECRET = 'gGt6HhfF@Mn%LpLe'

if args.client is None:
    print(f"Client name is not specified. Example: \"python3 create_licenses.py --client Client_name --days_to_expire 30\"")
    exit()

if args.days_to_expire is None:
    print(f"Days to expire is not specified. Example: \"python3 create_licenses.py --client Client_name --days_to_expire 30\"")
    exit()


def create_lic():
    dt = datetime.now() + timedelta(days=args.days_to_expire)
    encoded_token = jwt.encode({'client_name': args.client, 'exp': dt}, SECRET, algorithm='HS256')
    print(encoded_token)


create_lic()
