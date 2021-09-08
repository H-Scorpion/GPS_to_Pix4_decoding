import joblib



def getPVT(all_recv):
    for timestamp, obj in all_recv:
        if  obj._id == 7:
            obj.fixType = 0x03
            joblib.dump(obj, 'NAV-SOL_template.pkl') 
            break

if __name__=='__main__':
    all_recv = joblib.load('./gpsData/demoGps.pkl')
    getPVT(all_recv)
    
