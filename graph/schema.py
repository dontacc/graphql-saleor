import graphene
from graphene_django import DjangoObjectType

from app.models import *



class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'detail')



class DetailType(DjangoObjectType):
    class Meta:
        model = Details
        fields = ('id', 'name', 'notes', 'category')


class Query(graphene.ObjectType):

    all_details = graphene.List(DetailType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    


    def resolve_all_details(root, info):
        return Details.objects.all().select_related('category')
    

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except:
            return None
        

schema = graphene.Schema(query=Query)


