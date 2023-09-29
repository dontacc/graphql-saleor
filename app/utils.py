import requests
from .variables import *


def get_token():
      
    query = '''
        mutation createToken($email: String!, $password: String!){
            tokenCreate(email: $email, password: $password){
                token
                refreshToken
                errors{
                    message
                    field
                }
            }
        }
    '''
    
    
    var = {
        "email": "arianminooei@gmail.com",
        "password": "arianmin"
    }
    
    
    res = requests.post(url=URL, 
                        json={"query": query, "variables": var}, 
                        headers={})
    
    
    token = res.json()['data']['tokenCreate']['token']
    return token