a = "app_id=92313732367395&unit_id=256330535246694&ifa=a8ee4159-d475-4a51-910e-ed68d79232dd&user_id=c5725a9568e146cba9a2b4dfd2fec2ab&client_ip=1.216.142.24&revenue_types=[%22cpc%22]&gender=M&device_name=SM-S911N&target_fill=10&cursor=bzc_NodIghhLJPVZYOpDWXfbklEVXvNCQ-CujqF8E7AQ7kr2WlrNJ8KlSqUKoAEbcbHZWjdKHLzoq6riZxjezC0KL3uWHdhhV3RdT2WEusIT0EGnoXj-7CU4OqPRLAViHbh8QzpIMscY6BYiDV8q4opq0GYexYwV2fY6oBfTVA_HSf-sRnykarNM3uSHqKb_FQT4Kzz_seIjkZ0TJHlJZY0v16bcTTu-8e24bSWE9yc_17Pb8HckAWfMPuEwcoQ7aHWs"

b = a.split("&")
# print(b)

c = "types=%7B%22NATIVE%22%3A%5B%5D%2C%20%22VAST%22%3A%5B%5D%7D&device_id=44829950&gender=F&timezone=Asia%2FSeoul&mcc_mnc=45010&os_version=33&locale=ko_KR&birth_year=1964&device_name=SM-S908N&ad_id=d92eca6d-ddde-4f82-b825-6d25be6bb07d&size=10&app_version_code=4050703&user_id=14ebe7c69589869e7e9022f3abaf6c9a&sdk_version=41721&session_key=DkuAAFnMrTVIwYwoFNWAl6JDwhuN6%2BDJd0dxgA3Sp65sTp%2F7G70vO8TdsglvDR4etdjxIznFq7PuU2TKYt7okL8HMkkLBcjV6L8y%2F4kdorpi8bD5WutR19g%3D&app_version_name=4.5.7&network_type=wifi&app_id=283126574269099&unit_id=271029097511324&user_agent=Dalvik%2F2.1.0%20%28Linux%3B%20U%3B%20Android%2013%3B%20SM-S908N%20Build%2FTP1A.220624.014%29"
d = c.split("&")
# print(d)

k = "accountId=297431200&birthday=&clientIp=118.235.42.45&country=&creativeSize=0&cursor=bzc_Ae43hnxdTbh1cijGGfWTBy_X1GXdMrTvuheS7FkXnnNO1VkQVSexsDr8IcSIUdpcnIEf6O-B27sCAr2BqhtrQzpyb4lgv8Gk_T7Uol05spPQzVKr3GunvDr-AGXkHCxWmN2Oc3UxeD2Q4w_-w8uGOtE7Qc0a0hJTdYchWqCGuHLmRfT-s7XRvVI0yJrj8RTFWsQ9NvXHz72xkZHaUNZV2tsZU2gBSWtZbeNNXvIN36ukQRzcYyKJsL4tGrLwJofnUEBf7lJWXEVzdMexLu9j9w%3D%3D&deviceId=297431200&deviceName=SM-S911N&gender=M&ifa=1427cd0a-0675-49b3-af49-d37cebbad7aa&ifv=&language=&membershipDays=0&networkType=&osVersion=&platform=&relationship=&revenueTypes=%5B%22cpc%22%2C%22cpm%22%5D&sdkVersion=0&targetFill=10&timezone=Asia%2FSeoul&types=%7B%22NATIVE%22%3A%5B%5D%7D&unitId=256330535246694&userAgent=&userId=30fbe7afe85d496fafac6e2ccebb6e39"
k = k.split("&")
print(k)

def list_to_dict(input_string):
    data = {}
    for element in input_string:
        a, b = element.split('=')
        data[a] = b
        print(f"key: {a}, value: {b}")
    return data
# not_s2s = list_to_dict(b)
# s2s = list_to_dict(d)

# for k, v in not_s2s.items():
#     if k in s2s:
#         print(f"key: {k}, s2s value: {s2s[k]}, CJ: {not_s2s[k]}")

list_to_dict(k)