from functools import _Descriptor
import graphene
from graphene_django import DjangoObjectType

from .models import Track


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        return Track.objects.all()


class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    # if you have a mutation with lots of arguments use **kwargs partens
    def mutate(self, info, title, description, url):
        # kwargs.get('tite)
        track = Track(title=title, description=description,
                      url=url)  # create a new track
        track.save()  # adding to db
        return CreateTrack(track=track)  # returning the track


class mutation(graphene.ObjectType):  # this is the mutation class
    create_track = CreateTrack.Field()  # this is the mutation field


# results in localhost:8000/graphql

# Query
# {
#   tracks {
# 	id
# 	title
# 	description
# 	url
# 	createdAt
# 	}
# }

# Mutation
# Mutation {
# 	createTrack(title: “Track 3”, description:”Track 3”, url:”www.tracsk.com”){
# 		track{
# 			id
# 			title
# 			description
# 			url
# 			createdAt
# 		}
# 	}
# }
