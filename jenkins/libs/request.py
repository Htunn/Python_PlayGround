import requests

def makePostRequest(url, payload, auth):
    response = requests.post(url,
          data=payload,
          auth=auth,
          verify='htunn.pem')
    return response

def makeGetRequest(url, auth):
    response=response.get(url<
        auth=auth,
        verify='htunn.pem')
    return response

def makePostRequestWithOutAuthAndNoCA(url, payload):
    response=requests.post(url, data=payload)
    return response