import graphene

import tracks.schema


class Query(tracks.schema.Query, graphene.ObjectType):
    pass


# this is the mutation class that inherits from the tracks.schema.Mutation
class Mutation(tracks.schema.Mutation, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
