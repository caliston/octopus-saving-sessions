# Octopus Energy Saving Sessions API

This is a Python script to fetch data from the Octopus Energy UK API for
'Saving Sessions', where customers are paid for reducing their usage at
times of peak demand.  It's intended to be a starting point for hooking into
various load reduction techniques.

You still need to sign up to each Saving Session individually, but the API
allows automatic detection of the start and end times of the session.

Fill in your Octopus email, password and account number in the script to get
started.  Then run it:

```
$ python3 octopus-saving-sessions.py 
{
    "data": {
        "savingSessions": {
            "account": {
                "hasJoinedCampaign": true,
                "joinedEvents": [
                    {
                        "eventId": 628,
                        "startAt": "2022-11-22T17:30:00+00:00",
                        "endAt": "2022-11-22T18:30:00+00:00"
                    },
                    {
                        "eventId": 727,
                        "startAt": "2022-11-30T17:30:00+00:00",
                        "endAt": "2022-11-30T18:30:00+00:00"
                    }
                ]
            }
        },
        "octoPoints": {
            "account": {
                "currentPointsInWallet": 1234
            }
        }
    }
}
```

## Credit

Idea based on some code in:
https://github.com/BottlecapDave/HomeAssistant-OctopusEnergy/blob/develop/custom_components/octopus_energy/api_client.py

Apologies for my abuse of GraphQL.

## Licence

3-clause BSD
