import django
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests
from .variables import *
from .utils import *




class CreateCategory(APIView):


    def post(self, request):
        
        if get_token():

            query = '''
                mutation createCategory($parent: ID, $input: CategoryInput!){
                    categoryCreate(parent: $parent, input: $input){
                        category{
                            name
                        }
                        errors{
                            message
                            field
                        }
                    }
                }
            '''

            var = {
                "input": {
                    "name": "digital2"
                }
            }

            header = {
                "Authorization-Bearer": get_token(),
            }
            
            res = requests.post(url=URL, 
                                json={'query': query, 'variables': var}, 
                                headers=header)
            
            print(res.json())
            return Response()
        else:
            print("aa")
            return Response()

        

      


class CreateProduct(APIView):

    def post(self, request):
        

        if get_token():

            query = '''
                mutation productCreate($input: ProductCreateInput!){
                    productCreate(input: $input){
                        product{
                            name
                            id
                            __typename      
                        }
                    }
                }     
            '''


            var = {
                "input":{
                    "productType": "UHJvZHVjdFR5cGU6MTc=", 
                    "name": "product1",
                    "category": "Q2F0ZWdvcnk6NDU=",
                    "attributes": [{"id": "QXR0cmlidXRlOjQz", "values": ["digital-audio"]}]
                }
                
            }


            header = {
                "Authorization-Bearer": get_token()
            }


            result = requests.post(url=URL, 
                                   json={"query": query, "variables": var}, 
                                   headers=header)
            

            if result.status_code == 200:
                print("OK")
                return Response()
            else:
                return Response()

        else:
            print("error")
            return Response()

        
class ProductTypes(APIView):

    def get(self, request):
        

        query = '''
            query {
                productTypes(first: $first){
                    edges{
                        node{
                            name
                            id
                            __typename
                            slug
                        }
                    }
                }
            }
        '''


        result = requests.post(url=URL, json={"query": query})

        print(result.json())
        return Response()

