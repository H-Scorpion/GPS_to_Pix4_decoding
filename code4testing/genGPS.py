import joblib
import copy



# dict_keys(['__module__', 'iTOW', 'year', 'month', 'day',
#  'hour', 'min', 'sec', 'valid', 'tAcc', 'nano', 'fixType',
#  'flags', 'flags2', 'numSV', 'lon', 'lat', 'height', 'hMSL',
#  'hAcc', 'vAcc', 'velN', 'velE', 'velD', 'gSpeed', 'headMot',
#  'sAcc', 'headAcc', 'pDOP', 'flags3', 'reserved1', 'reserved1x',
#  'headVeh', 'magDec', 'magAcc', '__dict__', '__weakref__', '__doc__'])

pvt_obj = joblib.load('./NAV_template/NAV-PVT_template.pkl')
sol_obj = joblib.load('./NAV_template/NAV-SOL_template.pkl')
# print(pvt_obj)
data_len = 5000
height = [5 for _ in range(data_len)]
lon = [round(121*10**7+10*i,3) for i in range(data_len)]
lat = [round(25*10**7+10*i,3) for i in range(data_len)]
timestamp = [0.2+i*0.2 for i in range(data_len)]
genGpsData = []

for i in range(data_len):
    pvt_gps = copy.deepcopy(pvt_obj)
    sol_gps = copy.deepcopy(sol_obj)
    pvt_gps.height = height[i]
    pvt_gps.lon = pvt_gps.lon + lon[i]
    pvt_gps.lat = pvt_gps.lat + lat[i]
    pvt_gps.fixType = 0x03
    genGpsData.append(
        (timestamp[i], pvt_gps)
    )
    # genGpsData.append(
    #     (timestamp[i]+0.02, sol_obj)
    # )
    # print((0.2+i*0.2,gps))

    if i % 1000 == 0 :
        print(i)

joblib.dump(genGpsData,'./fakeGps.pkl')

# all_fake = joblib.load('fakeGps.pkl')
# print(all_fake[0][1])
