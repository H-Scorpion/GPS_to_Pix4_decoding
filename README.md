# GPS data processing and transmission
This repo helps us collect data from u-blox gps module,
transfering it to the format that FC can understand.
Besides, before sending it to FC, we can do some computation
to get better positioning data
## File Structure
### serialComPort.txt
Specify ttl COM Port inside
### getGpsData
Gps Tx to ttl Rx
Retrived Gps data will be stored in './gpsData'.
Data comes in 3 type:
'.txt', '.log', '.pkl'
txt for plain text
log for binary gps data
pkl for ubx object
