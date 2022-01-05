from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()  # this is the user model
        # only fields that are needed
        only_field = ('id', 'email', 'password', 'username')


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)  # username is required
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


# mutation {
#     createUser(username: "test", password: "test", email: "test@gmail/com") {
#         user {
#             id
#             username
#             email
#             dateJoined
#         }
#     }
# }
