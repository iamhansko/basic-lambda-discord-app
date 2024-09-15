import json
from nacl.signing import VerifyKey
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

DISCORD_PUBLIC_KEY = os.getenv("DiscordPublicKey")

def lambda_handler(event, context):
    try:
        raw_body = event['body']
        auth_sig = event['headers'].get('x-signature-ed25519')
        auth_ts = event['headers'].get('x-signature-timestamp')

        verify_key = VerifyKey(bytes.fromhex(DISCORD_PUBLIC_KEY))
        verify_key.verify(f'{auth_ts}{raw_body}'.encode(), bytes.fromhex(auth_sig))
    except Exception as e:
        raise Exception(f"[UNAUTHORIZED] Invalid request signature: {e}")

    body = json.loads(raw_body)
    if body["type"] == 1:
        print("PONG")
        return {
            'statusCode': 200,
            'body': json.dumps(
                {
                    'type': 1
                }
            )
        }

    print(event)
    print(body)

    command = body['data']['name']
    if command == "cat":
        return {
            'statusCode': 200,
            'headers' : {'Content-Type': 'application/json'},
            'body': json.dumps({
                'type': 4,
                'data': {
                    'content': "🐱 Meow",
                }
            })
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unhandled Command')
        }