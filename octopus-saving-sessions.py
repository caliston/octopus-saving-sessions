#!/usr/bin/env python3

import requests
import json
import sys

email = "your_octopus_email@example.com"
password = "your_password"
account = "A-AAAAAAAA" # Octopus account number

url = 'https://api.octopus.energy/v1/graphql/'
query = 'mutation krakenTokenAuthentication{ obtainKrakenToken(input: {email: "%s", password: "%s"}) { token } }' % (email, password)
r = requests.post(url, json={'query': query})
if r.status_code != 200:
    print("Failed")
    sys.exit(1)
auth = json.loads(r.text)
token = auth['data']['obtainKrakenToken']['token']
jwt = "JWT %s" % token


query = """query {
	savingSessions {
		account(accountNumber: "%s") {
			hasJoinedCampaign
			joinedEvents {
				eventId
				startAt
				endAt
			}
		}
	}
  octoPoints {
		account(accountNumber: "%s") {
			currentPointsInWallet
    }
  }
}""" % (account, account)

headers = {"Authorization": jwt}


r = requests.post(url, headers=headers, json={'query': query})
if r.status_code != 200:
	print("Failed")
	sys.exit(1)

sessions = json.loads(r.text)
print(json.dumps(sessions, indent=4))
