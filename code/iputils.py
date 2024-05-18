import geoip2.database
import os
import json
from requests import request

max_retry = 5
region_schinese = ["CN"]
region_tchinese = ["HK", "MO", "TW"]


def get_public_ip_lang():
    if not os.path.exists("GeoLite2-Country.mmdb"):
        return "english"
    # Public IP lookup sites
    china_mainland_ip_endpoint = "https://ip.3322.net/"
    intl_ip_lookup_endpoint = "https://api.ipify.org?format=json"
    # Try China IP lookup first
    trials = 0
    while trials < max_retry:
        try:
            ip_addr_from_chn = (request("GET", china_mainland_ip_endpoint, headers={}, data={}).text.strip().
                                replace("'", ""))
            with geoip2.database.Reader("GeoLite2-Country.mmdb") as ip_reader:
                ip_info_from_chn = ip_reader.country(ip_addr_from_chn)
                country_iso_code = ip_info_from_chn.country.iso_code
                if country_iso_code is None:
                    trials += 1
                    continue
                if country_iso_code in region_schinese:
                    print("检测到位于中国大陆地区，切换为简体中文")
                    return "schinese"
                elif country_iso_code in region_tchinese:
                    print("檢測到位於中國香港/澳門/台灣地區，切換為繁體中文")
                    return "tchinese"
                else:
                    return "english"
        except Exception as e:
            trials += 1
            print(f"[ERROR] {e}")
            continue
    # Fallback intel IP lookup
    print("[WARN] Cannot detect public IP address from server in China, try detecting from an international one")
    trials = 0
    while trials < max_retry:
        try:
            ip_addr_from_intl = json.loads(request("GET", intl_ip_lookup_endpoint, headers={}, data={}).text)["ip"]
            with geoip2.database.Reader("GeoLite2-Country.mmdb") as ip_reader:
                ip_info_from_intl = ip_reader.country(ip_addr_from_intl)
                country_iso_code = ip_info_from_intl.country.iso_code
                if country_iso_code is None:
                    trials += 1
                    continue
                if country_iso_code in region_schinese:
                    print("检测到位于中国大陆地区，切换为简体中文")
                    return "schinese"
                elif country_iso_code in region_tchinese:
                    print("檢測到位於中國香港/澳門/台灣地區，切換為繁體中文")
                    return "tchinese"
                else:
                    return "english"
        except Exception as e:
            trials += 1
            print(f"[ERROR] {e}")
            continue
    print("[WARN] Cannot detect public IP address from international server, using English")
    return "english"
