import graphene
import tracks.schema


class Query(tracks.schema.Query, graphene.ObjectType):
    pass


query = graphene.Schema(query=Query)
