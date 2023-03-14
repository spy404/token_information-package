# token information library for python ~ github.com/spy404
# token information tool created for looking up discord account data with the use of an account

# ------ libs ------ #
import requests
import datetime
from pystyle import Center

cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}

def help():
    banner = Center.XCenter("\033[94m" + """
                 ___ ___ ___ 
    ___ ___ _ _ | | |   | | |
    |_ -| . | | |_  | | |_  |
    |___|  _|_  | |_|___| |_|
        |_| |___|                 
    \n\n""")
    print(banner)
    print(Center.XCenter("[+] Welcome to token info project | Tool for discord token information\n"))
    print(Center.XCenter("Developed with love by spy404 | discord.gg/EvDpzfya"))
    print(Center.XCenter("""
    \n[+] General commands: 
        [-] token-information.user() | Returns general user data
        [-] token-information.payment() | Returns payment data
    \n[+] Specific commands: 
        [-] token-information.username() | Returns account username
        [-] token-information.userid() | Returns account user id
        [-] token-information.phonenumber() | Returns account phonenumber
        [-] token-information.avatar | Returns account avatar
        [-] token-information.email() | Returns account email
        [-] token-information.auth() | Returns account 2FA stat
        [-] token-information.flags() | Return account flags
        [-] token-information.language() | Return account language
        [-] token-information.verified() | Return account email verifiction
        [-] token-information.login() | Returns account login code for console
        [-] token-information.creation_date() | Return account creation date
        [-] token-information.nitro() | Return account nitro stats\n
    Use all commands with token argumant
    """ + "\033[0m"))

def user(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    res = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)

    if res.status_code == 200:
        
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        phone_number = res_json['phone']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.png'
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        nitro_res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
        nitro_data = nitro_res.json()
        nitro = bool(len(nitro_data) > 0)
        login = """function login(token) {
    setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `\"${token}\"`
    }, 50);
    setTimeout(() => {
        location.reload();
    }, 2500);
}
        """
        login = login + f"\nlogin(\"{token}\")"
        return user_name, user_id, phone_number, avatar_url, email, mfa_enabled, flags, locale, verified, creation_date, nitro, login

def payment(token):
    
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    billing_info = []

    for i in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers = headers).json():
        j = i['billing_address']
        name = j['name']
        country = j['country']
        city = j['city']
        address_one = j['line_1']
        address_two = j['line_2']
        postal_code = j['postal_code']
        state = j['state']

        if i['type'] == 1:
            cc_brand = i['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = i['last_4']
            cc_month = str(i['expires_month'])
            cc_year = str(i['expires_year'])

            data  = {
                'Payment-Type': 'Credit-Card',
                'Valid': not i['invalid'],
                'CC-Holder-Name': name,
                'CC-Brand': cc_brand.title(),
                'CC-Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                'CC-Exp-Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                'Address-1': address_one,
                'Address-2': address_two if address_two else '',
                'City': city,
                'Postal-Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default-Payment-Method': i['default']
            }

            billing_info.append(data)
            
            return billing_info
        elif i['type'] == 2:
            
            data = {
                'Payment-Type': 'PayPal',
                'Valid': not i['invalid'],
                'PayPal-Name': name,
                'PayPal-Email': i['email'],
                'Address-one': address_one,
                'Address-two': address_two if address_two else '',
                'City': city,
                'Postal-Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default-Payment-Method': i['default']
            }

            billing_info.append(data)
            
            return billing_info

def username(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return f'{res_json["username"]}#{res_json["discriminator"]}'
    
    else:
        return 'Wrong request'
    
def userid(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return res_json['id']
    
    else:
        return 'Wrong request'
    
def phonenumber(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return res_json['phone']
    
    else:
        return 'Wrong request'
    
def avatar(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return f"https://cdn.discordapp.com/avatars/{res_json['id']}/{res_json['avatar']}.png"
    
    else:
        return 'Wrong request'
    
def email(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return res_json['email']
    
    else:
        return 'Wrong request'
    
def auth(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return res_json['mfa_enabled']
    
    else:
        return 'Wrong request'
    
def flags(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return res_json['flags']
    
    else:
        return 'Wrong request'
def language(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return res_json['locale']
    
    else:
        return 'Wrong request'
    
def verified(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return res_json['verified']
    
    else:
        return 'Wrong request'
    
def login(token):
    login = """function login(token) {
    setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `\"${token}\"`
    }, 50);
    setTimeout(() => {
        location.reload();
    }, 2500);
}
    """
    login = login + f"\nlogin(\"{token}\")"

    return login

def creation_date(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://discordapp.com/api/v9/users/@me', headers = headers)
    if res.status_code == 200:

        res_json = res.json()
        return datetime.datetime.utcfromtimestamp(((int(res_json['id']) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    
    else:
        return 'Wrong request'
    
def nitro(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    nitro_res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)

    if nitro_res.status_code == 200:

        nitro_data = nitro_res.json()
        return bool(len(nitro_data) > 0)
    
    else:
        return 'Wrong request'
