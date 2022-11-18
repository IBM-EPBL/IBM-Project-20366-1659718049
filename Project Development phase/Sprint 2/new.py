import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "JJoSicw67yzKlSR_agOi5liOkDvcZwsd3m4bV0ck9Sjx"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()['access_token']



print('mltoken',mltoken)

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["age","bp","al","su","rbc","pc","pcc","ba","bgr","bu","sc","pot","wc","htn","dm","cad","pe","ane"]], "values": [[48.0,70.0,4.0,0.0,0,1,1,0,117.0,56.0,3.8,2.5,6700,1,0,0,1,1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6b7627de-946c-42c9-a3d2-563154efd72b/predictions?version=2022-11-17', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
