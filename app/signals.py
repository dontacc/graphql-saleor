from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import *
from .utils import *



@receiver(pre_save, sender=Product)
def create_warehouse(sender, instance, **kwargs):
    
    query = '''
        mutation createWarehouse($input: WarehouseCreateInput!){
            createWarehouse(input: $input){
                warehouse{
                    id
                    name
                    email
                    address{
                        city
                        country{
                            code
                            country
                        }
                    }
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
            "name": "carfix",
            "slug": "car-fix",
            "address": {"country": "IR", "city": "ISfahan", "streetAddress1": "khaghani street"}
        }
    }

    header = {
        "Authorization-Bearer": get_token()
    }


    result = requests.post(url=URL, 
                           json={"query": query, "variables": var}, headers=header)
    
    print(result.json())


