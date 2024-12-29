# Current version of the script 
debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION=CURRENT_VERSION.replace('\n','')
server_local = "http://127.0.0.1:3000"
server_online = "https://api.topixsb.dev"
mode_server = server_online
"""
-------------------------------------------
MAJOR (Angka Pertama):

Angka ini meningkat ketika ada perubahan yang tidak kompatibel yang mengharuskan 
pengguna untuk memodifikasi kode atau penggunaan mereka yang ada. Misalnya, 
jika suatu fungsi dihapus atau perilakunya berubah secara signifikan, Anda akan 
meningkatkan versi mayor.
-------------------------------------------
MINOR (Angka Kedua):

Angka ini meningkat ketika fitur baru ditambahkan dengan cara yang kompatibel 
dengan versi sebelumnya. Ini berarti bahwa fungsionalitas yang ada tetap tidak 
berubah, tetapi kemampuan atau peningkatan baru diperkenalkan. Misalnya, 
jika fungsi baru ditambahkan tanpa memengaruhi yang sudah ada, Anda akan 
menaikkan versi minor.
-------------------------------------------
PATCH (Angka Ketiga):

Angka ini meningkat ketika perbaikan bug yang kompatibel dengan versi sebelumnya 
diperkenalkan. Ini biasanya merupakan perubahan kecil yang menyelesaikan masalah 
tanpa menambah fitur baru atau merusak fungsionalitas yang ada. Misalnya, 
jika ada bug yang diperbaiki dalam suatu fungsi tetapi antarmuka fungsi tersebut 
tetap sama, Anda akan menaikkan versi patch.
-------------------------------------------
"""



import os,sys,random,requests


VERSION_CHECK_URL = f"{mode_server}/termux-version"

def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        # Pastikan direktori ada
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")
        
def update_script():
    version_info = get_latest_version_info()
    if not version_info:
        return
    
    latest_version = version_info.get("version")
    download_url = version_info.get("download_url")
    print(download_url)
    print(f"CURRENT_VERSION {CURRENT_VERSION}\nlatest_version {latest_version}\ndownload_url {download_url}")
    if latest_version and download_url:
        if latest_version != CURRENT_VERSION:
            print(f"New version available: {latest_version}")
            print(f"Downloading update... {download_url}")
            download_new_version(download_url, sys.argv[0])
            print("Script updated to the latest version. Please restart the script.")
            exit()
        else:
            print("You already have the latest version.")
    else:
        print("Invalid version information received.")
update_script()


import platform
from datetime import datetime
local_ip = requests.get('https://api.ipify.org').text
response = requests.get(f"https://ipinfo.io/{local_ip}/json")
data_jaringan = response.json()

try:
    from colorama import init, Fore, Back, Style
    init()
    # Fungsi color pengganti menggunakan colorama
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    
    # Reinisialisasi setelah install
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem



def disp(clrnama):
    def get_closest_color(r, g, b):
        # Memetakan warna RGB ke warna colorama terdekat
        colors = {
            'RED': (255, 0, 0, Fore.RED),
            'GREEN': (0, 255, 0, Fore.GREEN),
            'BLUE': (0, 0, 255, Fore.BLUE),
            'YELLOW': (255, 255, 0, Fore.YELLOW),
            'MAGENTA': (255, 0, 255, Fore.MAGENTA),
            'CYAN': (0, 255, 255, Fore.CYAN),
            'WHITE': (255, 255, 255, Fore.WHITE)
        }
        
        min_distance = float('inf')
        closest_color = Fore.WHITE  # default
        
        for _, (cr, cg, cb, color) in colors.items():
            distance = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
            if distance < min_distance:
                min_distance = distance
                closest_color = color
                
        return closest_color

    clrfirsttime = True
    clrVnama = clrnama.split("[")
    clrdisps = clrVnama[0]
    
    for clrx in clrVnama:
        if clrfirsttime == False:
            try:
                # Mengkonversi hex ke RGB
                clrcode1 = int(clrx[0:2], 16)
                clrcode2 = int(clrx[2:4], 16)
                clrcode3 = int(clrx[4:6], 16)
                clrhuruf = clrx[7:8]
                
                # Mendapatkan warna colorama terdekat
                closest_color = get_closest_color(clrcode1, clrcode2, clrcode3)
                clrdisps += closest_color + clrhuruf + Style.RESET_ALL
            except:
                clrdisps += clrx[7:8]
                
        if clrfirsttime:
            clrfirsttime = False

    clrdisps += clrVnama[len(clrVnama)-1][8:len(clrVnama[len(clrVnama)-1])]
    return clrdisps

warnasekarang=""
def generate(namax):
    global warnasekarang
    gabungwarna = ""
    contohnama = namax
    # proses memecah huruf di nama
    data = {
        "huruf": "",
        "Hadji": [255, 0, 0],
        "mode": 1,
        "HadjiCPM": ""
    }
    while True:
        while True:
            tanya = random.choice(["merah","kuning","hijau","biru","ungu","pink"])
            if tanya!=warnasekarang:
                warnasekarang = tanya
                break
        if tanya == "merah":
            data["Hadji"] = [255, 0, 0]
            break
        elif tanya == "kuning":
            data["Hadji"] = [230, 245, 66]
            break
        elif tanya == "hijau":
            data["Hadji"] = [0, 255, 0]
            break
        elif tanya == "biru":
            data["Hadji"] = [0, 0, 255]
            break
        elif tanya == "ungu":
            data["Hadji"] = [150, 66, 245]
            break
        elif tanya == "pink":
            data["Hadji"] = [245, 66, 215]
            break
        else:
            print("Harus sesuai pilihan warna ..!")

    for huruf in contohnama:
        while True:
            # print(f"\nmode sekarang : {data['mode']}")
            tambah = 45
            if data["mode"] == 1:
                if data["Hadji"][1]+tambah <= 255:
                    data["Hadji"][1] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["Hadji"] = [255, 255, 0]
            elif data["mode"] == 2:
                if data["Hadji"][0]-tambah >= 0:
                    data["Hadji"][0] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["Hadji"] = [0, 255, 0]
            elif data["mode"] == 3:
                if data["Hadji"][2]+tambah >= 255:
                    data["Hadji"][2] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["Hadji"] = [0, 255, 255]
            elif data["mode"] == 4:
                if data["Hadji"][1]-tambah >= 0:
                    data["Hadji"][1] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["Hadji"] = [0, 0, 255]
            elif data["mode"] == 5:
                if data["Hadji"][0]+tambah >= 255:
                    data["Hadji"][0] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["Hadji"] = [255, 0, 255]
            elif data["mode"] == 6:
                if data["Hadji"][2]-tambah >= 255:
                    data["Hadji"][2] -= tambah
                    break
                else:
                    data["mode"] = 1
                    data["Hadji"] = [255, 0, 0]
        # print(f"{huruf} {data['Hadji']}")
        gabungwarna += color(huruf,
                             fore=(data["Hadji"][0],
                                   data["Hadji"][1],
                                   data["Hadji"][2]),
                             back=(0, 0, 0))
        kodas = []
        for t in range(3):
            clrcode = hex(data["Hadji"][t])[2::]
            if len(clrcode) == 1:
                clrcode += "0"
            kodas.append(clrcode)
        data["HadjiCPM"] += f"[{kodas[0]}{kodas[1]}{kodas[2]}]{huruf}"
    # print(f"hasil\t:  {disp(data['HadjiCPM'])}")
    # print(f"kode\t:  {data['HadjiCPM']}")
    return data["HadjiCPM"]
def refresh_x():
    import inspect
    kucing_garong = inspect.getfile(inspect.currentframe())
    with open(kucing_garong, 'r') as file:
        gajah_terbang = file.read()
        gajah_duduk = len(gajah_terbang)
    return gajah_duduk
pySystem.Clear()
pySystem.Size(80, 40)


text = """
< [ YouTube TopixSB ] > X < [ ₱ⱤØ₲Ɽ₳₥ ฿Ɇ₮₳ ] >"""[1:]

banner = r"""
___ç$$$ç________________
__$$$$$$$_####______####_       YouTube TopixSB
___*$$$$$$ç####___########        
_____*$$$$$$$$$$$##########     ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█
_____$$$$$$$$$$$$$##########    ░▒█░░ ░▀▀▀▄▄ ▒█▀▀▄
______$$$$$$$$$$$$$##########   ░▒█░░ ▒█▄▄▄█ ▒█▄▄█ 
______$$$$$$$$$$_$$$##########
______$$$$$$$$$$##$$$##########
_______$$$$$$$$$_##$$##########
______$$$$$$$$$$___$$#########
_____$_$$$$$$$$$$__$$_########
___$$__$$$$$$$$$$_$$$__######
______$$$$$$$$$$__$$$___#####
______$$$$$$$$$___$$____####
______$$$$$$$$$_________###
______$$$$$$$$__________##
_______$$$$$$___________##
_______$$$$$$______________
_______$$$$$$$$____________
_______$$$$$$$$____________
_______$$$$_$$$$___________
_______$$$$_$$$$___________
_______$$$___$$$$__________
__ççç$$$$$$_çç$$$$__________       
                          
           Car Parking Multiplayer Instant Script
                    LESS THEN 1 MINUTE

                        PRESS ENTER          
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.purple_to_red, pyColorate.Vertical, enter=True)

pySystem.Clear()

print("\n"*2    )
print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
print("\n"*2)


delet=["cpm/pos.py","cpm/__init__.py"]
for psdd in delet:
    if os.path.exists(f"{psdd}") == True:
        os.system(f"rm {psdd}")



def c(colr, tex):
    try:
        w = {
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "CYAN": Fore.CYAN,
            "YELLOW": Fore.YELLOW,
            "GOLD": Fore.YELLOW  # Colorama tidak memiliki gold, gunakan yellow sebagai alternatif
        }
        return w[colr.upper()] + tex + Style.RESET_ALL
    except:
        return tex
def mask_password(password):
    if len(password) <= 3:
        return password
    return password[:3] + '*' * (len(password) - 3)
def heder():
        if Your_Data['username']:
            get_userInfo()
        pySystem.Clear()
        print(f"build : {refresh_x()}")
        versi_tampil = disp(generate(f"Topix SB CPM TOOLS {CURRENT_VERSION}"))
        loc_info = f"  Location\t  : {data_jaringan.get('city')}, {data_jaringan.get('region')}, {data_jaringan.get('country')}"
        loc_info = pyColorate.Horizontal(pyColors.green_to_yellow, loc_info)
        isp_info = f"  ISP     \t  : {data_jaringan.get('org')}"
        isp_info = pyColorate.Horizontal(pyColors.green_to_yellow, isp_info)
        bannerwz = f"""{c("cyan","=====================================================")}
  {versi_tampil} {c("cyan","||")} {c("green","https://carparking.topixsb.dev/")}
{c("cyan","=====================================================")}
{loc_info}
{isp_info}"""
        if Your_Data['email_web']:
            data_client=f"""
  username   : {Your_Data['username']}
  role       : {Your_Data['role']}
  money      : 99999999999999
  expire_at  : {Your_Data['expire_at']}
  last login : {Your_Data['last_login_date']}"""
            if 'email' in Your_Data:
                data_client+=f"""\n\n  Car Parking Email : {Your_Data["email"]}
  Car Parking Passw : {mask_password(Your_Data["password"])}"""
            
            bannerwz+=pyColorate.Horizontal(pyColors.green_to_yellow, data_client)
        print(bannerwz)

tex="""     IMPORTANT READ

    You must log out of the CPM application first, 
    unless you only want to use the "Inject Rank" and "Instant Rank" features, 
    as these two features do not require you to log out.

    Please refill your cash only at https://carparking.topixsb.dev

"""

print(pyColorate.Horizontal(pyColors.green_to_yellow, pyCenter.XCenter(tex)))



def warnain(text,inpo="",title=""):
    tex = f"""{c("cyan","=====================================================")}"""
    if inpo:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.red_to_purple, inpo)}"
    if title:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.cyan_to_green, title)}"
    tex+=f"""
{pyColorate.Horizontal(pyColors.cyan_to_green, text)}
{c("cyan","=====================================================")}"""
    print(tex)


def send_registration_data(uname, upass):
    url = f"{mode_server}/register-acc"
    
    data = {
        "username": uname,
        "password": upass
    }
    
    try:
        response = requests.post(url, data=data)
        
        # Pastikan untuk memanggil .json() untuk mendapatkan data JSON
        response_data = response.json()
        return response_data
    except Exception as e:
        return f"An error occurred: {e}"
def send_login_data(uname, upass):
    url = f"{mode_server}/login-acc"
    
    data = {
        "username": uname,
        "password": upass
    }
    
    try:
        response = requests.post(url, data=data)
        
        if debug_mode:
            print(f"Response status: {response.status_code}")
            print(f"Response text: {response.text}")
        
        if response.status_code != 200:
            try:
                error_data = response.json()
                return {
                    "status": False, 
                    "message": error_data.get('message', 'Unknown error occurred')
                }
            except:
                return {
                    "status": False, 
                    "message": f"Server error: {response.status_code}"
                }
            
        try:
            response_data = response.json()
            
            if response_data['status']:
                # Simpan semua data user termasuk token
                Your_Data.update({
                    'access_token': response_data['access_token'],
                    'username': response_data['data']['username'],
                    'role': response_data['data']['role'],
                    'money': response_data['data']['money'],
                    'email_web': response_data['data']['email'],
                    'last_login': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Tambahkan waktu login
                })
            return response_data
            
        except ValueError as e:
            return {
                "status": False, 
                "message": f"Invalid JSON response: {response.text}"
            }
            
    except requests.RequestException as e:
        return {
            "status": False, 
            "message": f"Request error: {str(e)}"
        }
    except Exception as e:
        return {
            "status": False, 
            "message": f"Unexpected error: {str(e)}"
        }

def serper(cit, datanya):

        return {"status": False, "message": "Silakan login terlebih dahulu"}

    url = f"{mode_server}/app_endpoint"

    data = {

        "username": Your_Data['username'],
        "item": {
            "name": cit
        },
        "email": Your_Data.get('email', ''),
        "password": Your_Data.get('password', '')
    }
    
    for x in datanya:
        data[x] = datanya[x]
        
    try:
        response = requests.post(url, json=data)
        
        # Handle berbagai status code
        if response.status_code == 401:
            # Token expired atau invalid
            Your_Data.clear()
            Your_Data.update({
                'email_web': None, 
                'expire_at': None, 
                'last_login_date': None, 
                'money': None, 
                'role': None, 
                'username': None,
                'access_token': None
            })
            return {"status": False, "message": "Sesi anda telah berakhir, silakan login kembali"}
        elif response.status_code == 429:
            # Rate limit
            return {"status": False, "message": "Terlalu banyak request, mohon tunggu beberapa saat"}
        elif response.status_code >= 500:
            # Server error
            return {"status": False, "message": "Server sedang bermasalah, coba lagi nanti"}
            
        try:
            result = response.json()
            return result
        except ValueError:
            return {"status": False, "message": f"Invalid JSON response: {response.text}"}
            
    except requests.RequestException as e:
        return {"status": False, "message": f"Request error: {str(e)}"}
    except Exception as e:
        return {"status": False, "message": f"Unexpected error: {str(e)}"}


def get_userInfo():

    data = {
        "user": Your_Data['username'],
    }

    try:
        response = requests.post(url, json=data, timeout=10.0)
        
        if response.status_code == 401:
            Your_Data.clear()
            Your_Data.update({
                'email_web': None, 
                'expire_at': None, 
                'last_login_date': None, 
                'money': None, 
                'role': None, 
                'username': None,
                'access_token': None
            })
            return {"status": False, "message": "Sesi anda telah berakhir, silakan login kembali"}
            
        try:
            reqreg = response.json()
            Your_Data['role'] = reqreg['role']
            Your_Data['last_login_date'] = reqreg['last_login_date']
            Your_Data['expire_at'] = reqreg['expire_at']
            Your_Data['money'] = reqreg['balance']
            return {"status": True}
        except ValueError:
            return {"status": False, "message": f"Invalid JSON response: {response.text}"}
            
    except requests.Timeout:
        return {"status": False, "message": "Request timeout. Silakan coba lagi."}
    except requests.RequestException as e:
        return {"status": False, "message": f"Request error: {str(e)}"}
    except Exception as e:
        return {"status": False, "message": f"Unexpected error: {str(e)}"}

datamobil=[ 
{"id": 140, "name": 'Cars 13'},
{"id": 184, "name": 'Cars 29'},
{"id": 131, "name": 'Cars 34'},
{"id": 187, "name": 'Cars 38'},
{"id": 9, "name": 'Cars 39'},
{"id": 21, "name": 'Cars 40'},
{"id": 39, "name": 'Cars 41'},
{"id": 54, "name": 'Cars 42'},
{"id": 60, "name": 'Cars 43'},
{"id": 62, "name": 'Cars 44'},
{"id": 121, "name": 'Cars 45'},
{"id": 126, "name": 'Cars 46'},
{"id": 147, "name": 'Cars 47'},
{"id": 148, "name": 'Cars 48'},
{"id": 151, "name": 'Cars 49'},
{"id": 154, "name": 'Cars 50'},
{"id": 161, "name": 'Cars 51'},
{"id": 168, "name": 'Cars 52'},
{"id": 177, "name": 'Cars 53'},
{"id": 180, "name": 'Cars 54'},
{"id": 185, "name": 'Cars 55'},
{"id": 196, "name": 'Cars 56'},
{"id": 200, "name": 'Cars 57'},
{"id": 206, "name": 'Cars 58'},
{"id": 209, "name": 'Cars 59'},
{"id": 0, "name": 'Cars 60'},
{"id": 1, "name": 'Cars 61'},
{"id": 6, "name": 'Cars 62'},
{"id": 8, "name": 'Cars 63'},
{"id": 12, "name": 'Cars 64'},
{"id": 30, "name": 'Cars 65'},
{"id": 43, "name": 'Cars 66'},
{"id": 81, "name": 'Cars 67'},
{"id": 85, "name": 'Cars 68'},
{"id": 112, "name": 'Cars 69'},
{"id": 113, "name": 'Cars 70'},
{"id": 150, "name": 'Cars 71'},
{"id": 160, "name": 'Cars 72'},
{"id": 175, "name": 'Cars 73'},
{"id": 181, "name": 'Cars 74'},
{"id": 182, "name": 'Cars 75'},
{"id": 183, "name": 'Cars 76'},
{"id": 210, "name": 'Cars 77'},
{"id": 5, "name": 'Cars 78'},
{"id": 11, "name": 'Cars 79'},
{"id": 17, "name": 'Cars 80'},
{"id": 19, "name": 'Cars 81'},
{"id": 20, "name": 'Cars 82'},
{"id": 28, "name": 'Cars 83'},
{"id": 35, "name": 'Cars 84'},
{"id": 47, "name": 'Cars 85'},
{"id": 49, "name": 'Cars 86'},
{"id": 51, "name": 'Cars 87'},
{"id": 82, "name": 'Cars 91'},
{"id": 88, "name": 'Cars 93'},
{"id": 128, "name": 'Cars 98'},
{"id": 156, "name": 'Cars 101'},
{"id": 189, "name": 'Cars 102'},
{"id": 14, "name": 'Cars 107'},
{"id": 103, "name": 'Cars 120'},
{"id": 109, "name": 'Cars 122'},
{"id": 144, "name": 'Cars 127'},
{"id": 153, "name": 'Cars 128'},
{"id": 211, "name": 'Cars 132'},
{"id": 104, "name": 'Cars 134'},
{"id": 115, "name": 'Cars 135'},
{"id": 143, "name": 'Cars 139'},
{"id": 188, "name": 'Cars 141'},
{"id": 7, "name": 'Cars 143'},
{"id": 32, "name": 'Cars 146'},
{"id": 41, "name": 'Cars 147'},
{"id": 58, "name": 'Cars 148'},
{"id": 162, "name": 'Cars 149'},
{"id": 178, "name": 'Cars 150'},
{"id": 198, "name": 'Cars 151'},
{"id": 202, "name": 'Cars 152'},
{"id": 203, "name": 'Cars 153'},]
data_AWD = [
                '6L45-A/T',
                '7S Tronic',
                '7 DSG',
                '8 Speed Tiptonic S',
                '9G Tronic',
                'Speedshift mct 9',
                'dsg7s',
                'dsg/s-tronic',
                'getrag 233',
                'getrag v161',
                'gr6',
                'sc924',
                'l6sss',
                'nsx9',
                'smt6',
                'w6maa gen 2',
                'zf 4hp22',
                'zf 6hp26s',
                'zf 8hp50',
                'zf 8hp70',
                'zf 8hp76',
                'zf 8hp'
            ]


Your_Data = {
    'email_web': None, 
    'expire_at': None, 
    'last_login_date': None, 
    'money': None, 
    'role': None, 
    'username': None,
    'access_token': None
}
req_menu = requests.get(f"{mode_server}/get_menu")
menu_cpm1 = req_menu.json()
req_menu = requests.get(f"{mode_server}/get_menu_cpm2")
menu_cpm2 = req_menu.json()

if __name__ == "__main__":
    input("Understand ? ")
    inpo = ""
    while True:
        if not Your_Data['email_web']:
            heder()
            menus="""  [1] Login
  [2] Register
  [q] Exit"""
            warnain(menus,inpo)
            pil = input("  Choice : ")
            heder()
            if pil == "1":
                warnain("  Login TopixSB Account")
                uname = input("  Username : ")
                upass = input("  Password : ")
                reqreg = send_login_data(uname,upass)
                inpo = reqreg['message']
                if reqreg['status']:
                    Your_Data['email_web']=reqreg['data']['email']
                    Your_Data['username']=reqreg['data']['username']
                    Your_Data['password'] = upass
                    Your_Data['identifier'] = reqreg['data']['password']

                    Your_Data['role'] = reqreg['data']['role']
                    Your_Data['last_login_date']=reqreg['data']['last_login_date']
                    Your_Data['expire_at']=reqreg['data']['expire_at']
                    Your_Data['money']=reqreg['data']['money']
            elif pil == "2":
                warnain("  Registration TopixSB Account")
                uname = input("  Username : ")
                upass = input("  Password : ")
                reqreg = send_registration_data(uname,upass)
                inpo = reqreg['message']
            elif pil == "q":
                exit()
        else:
            heder()
            menus="""  [1] CPM 1
  [2] CPM 2
  [q] Exit"""
            warnain(menus,inpo)
            pilawal = input("  Choice : ")
            inpo=""
            heder()
            if pilawal == "1":
                while True:
                    heder()
                    menus1=""
                    for x,v in enumerate(menu_cpm1):
                        if debug_mode:
                            menus1+=f"[{v['id_item']}]"
                        if v['status']=="active":
                            menus1+=f"  [{x}] {v['nama_item']}\t\t[{v['harga_item']}]\n"
                        elif v['status']=="maintenance":
                            menus1+=f"  [🔧] {v['nama_item']}\t\t[{v['harga_item']}]\n"
                    menus1+="  [q] Back"
                    warnain(menus1,inpo,title="[ Car Parking Multiplayer 1 ]")
                    pil = input("  Choice : ")
                    inpo=""
                    heder()
                    if pil == "q":
                        break
                    if pil == "":
                        continue
                    if 'email' not in Your_Data:
                        print( f"""{c("cyan","=====================================================")}""")
                        Your_Data['email'] = input("CPM Email : ")
                        Your_Data['password'] = input("CPM Password : ")
                    dat_pil = menu_cpm1[int(pil)]
                    data={}
                    gas=False
                    if dat_pil['id_item'] in [2,3,4,8,9,10,13,14,17]:
                        print( f"""{c("cyan","=====================================================")}""")
                        gas=True
                    else:
                        print( f"""{c("cyan","=====================================================")}""")
                        if dat_pil['id_item']==1:
                            data['customName'] = input("New Name : ")
                        elif dat_pil['id_item']==5:
                            data['customID'] = input("Custom ID : ")
                        elif dat_pil['id_item']==6:
                            data['customIDplus'] = input("Custom ID ++ : ")
                        elif dat_pil['id_item']==7:
                            while True:
                                try:
                                    data['varian'] = int(input("Varian [1 -> 100] : "))
                                    break
                                except:
                                    pass
                        elif dat_pil['id_item']==11:
                            data['hp'] = input("hp : ")
                            data['innerHp'] = input("innerHp : ")
                            data['nm'] = input("nm : ")
                            data['innerNm'] = input("innerNm : ")
                        elif dat_pil['id_item']==[12,15]:
                            data['new_email'] = input("new email : ")
                            data['new_password'] = input("new password : ")
                        elif dat_pil['id_item']==16:
                            data['boost_win'] = input("Win Boost : ")
                        gas=True
                        

                    if gas:
                        reqreg = serper(dat_pil['nama_item'],data)
                        inpo = reqreg['message']

            if pilawal == "2":
                while True:
                    heder()
                    menus2=""
                    for x,v in enumerate(menu_cpm2):
                        if debug_mode:
                            menus2+=f"[{v['id_item']}]"
                        if v['status']=="active":
                            menus2+=f"  [{x}] {v['nama_item']}\t\t[{v['harga_item']}]\n"
                        elif v['status']=="maintenance":
                            menus2+=f"  [🔧] {v['nama_item']}\t\t[{v['harga_item']}]\n"
                    menus2+="  [q] Back"
                    warnain(menus2,inpo,title="[ Car Parking Multiplayer 2 ]")
                    pil = input("  Choice : ")
                    inpo=""
                    heder()
                    if pil == "q":
                        break
                    if pil == "":
                        continue
                    if 'email' not in Your_Data:
                        print( f"""{c("cyan","=====================================================")}""")
                        Your_Data['email'] = input("CPM 2 Email : ")
                        Your_Data['password'] = input("CPM 2 Password : ")
                    dat_pil = menu_cpm2[int(pil)]
                    data={}
                    gas=False
                    if dat_pil['id_item'] in [19,20,21,22,23,24,25,26,31,33]:
                        print( f"""{c("cyan","=====================================================")}""")
                        warnain("Masih dalam proses pengembangan")
                    else:
                        print( f"""{c("cyan","=====================================================")}""")
                        if dat_pil['id_item']==1:
                            gas=True
                            data['new_email'] = input("New Email : ")
                            data['new_password'] = input("New Password : ")
                        elif dat_pil['id_item']==2:
                            gas=True
                            data['del_email'] = input("Del Email : ")
                            data['del_password'] = input("Del Password : ")
                        elif dat_pil['id_item'] == 9:
                            gas = True
                            warnain("\n".join([f"{i+1}. {mobil['name']}" for i, mobil in enumerate(datamobil)]), inpo, title="Pilih Mobil")
                            nomor_mobil = int(input("Masukkan nomor urut mobil: ")) - 1
                            data['dataCarNumber'] = datamobil[nomor_mobil]['id']
                        elif dat_pil['id_item'] == 17:
                            gas = True
                            warnain("\n".join([f"{i+1}. {awd}" for i, awd in enumerate(data_AWD)]), inpo, title="Pilih AWD")
                            nomor_awd = int(input("Masukkan nomor urut mobil: ")) - 1
                            data['awdnya'] = data_AWD[nomor_awd]
                        elif dat_pil['id_item'] == 18:
                            gas = True
                            warnain("\n".join([f"{i+1}. {awd}" for i, awd in enumerate(data_AWD)]), inpo, title="Pilih AWD")
                            nomor_awd = int(input("Masukkan nomor urut awd: ")) - 1
                            data['awdnya'] = data_AWD[nomor_awd]


                        gas=True
                    if gas:
                        reqreg = serper(f"CPM 2 {dat_pil['nama_item']}",data)
                        inpo = reqreg['message']
            elif pilawal == "q":
                exit()
            


