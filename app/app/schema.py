import graphene
import tracks.schema
import users.schema
import graphql_jwt


class Query(tracks.schema.Query, graphene.ObjectType):
    pass

# this is query for users


class Query(users.schema.Query, graphene.ObjectType):
    pass

# this is the mutation class that inherits from the tracks.schema.Mutation


class Mutation(tracks.schema.Mutation, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, graphene.ObjectType):
    # replaced pass with the following from graphql_jwt https://github.com/flavors/django-graphql-jwt
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query)
