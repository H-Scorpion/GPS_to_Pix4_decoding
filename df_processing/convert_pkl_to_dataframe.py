import time
import joblib
import pandas as pd

# filename ='demoGps.pkl'
filename ='ubxPacket_20210901-165743.pkl'
all_objs = joblib.load('./gpsData/' + filename)

timestamp_start = time.time()
all_records = []

for timestamp, obj in all_objs:
    try:
        record = {}
        for k in obj.Fields.__dict__.keys():
            if not k.startswith('__'):
                record[k] = getattr(obj, k)

        record['timestamp'] = timestamp
        record['obj'] = obj
        record['_id'] = obj._id
        record['__name__'] = type(obj).__name__
    except TypeError:
        continue
    else:
        all_records.append(record)
        print(timestamp, 'converted:', obj._id)


df = pd.DataFrame.from_records(all_records)
df.to_pickle(f'{filename[:-4]}_df.pkl')
df.drop(columns=['obj']).to_excel(f'{filename[:-4]}_df.xlsx')
