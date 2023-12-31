# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from profiles.protos import profile_pb2 as profile__pb2


class ProfileServiceStub(object):
    """Service Documentation:
    The ProfileService service provides operations related to user profiles.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProfile = channel.unary_unary(
                '/profileservice.ProfileService/CreateProfile',
                request_serializer=profile__pb2.CreateProfileRequest.SerializeToString,
                response_deserializer=profile__pb2.CreateProfileResponse.FromString,
                )


class ProfileServiceServicer(object):
    """Service Documentation:
    The ProfileService service provides operations related to user profiles.
    """

    def CreateProfile(self, request, context):
        """CreateProfile Method:
        Creates a user profile based on the provided request.

        Request:
        - username: The username of the user.
        Field number: 1
        - user_id: The unique identifier for the user.
        Field number: 2
        - profile_image_url: The URL of the user's profile image.
        Field number: 3

        Response:
        - status: The status of the create profile operation.
        Field number: 1
        - msg: A human-readable message providing additional information about the operation.
        Field number: 2
        - error: If an error occurred, this field contains a human-readable error message.
        Field number: 3
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProfile,
                    request_deserializer=profile__pb2.CreateProfileRequest.FromString,
                    response_serializer=profile__pb2.CreateProfileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'profileservice.ProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProfileService(object):
    """Service Documentation:
    The ProfileService service provides operations related to user profiles.
    """

    @staticmethod
    def CreateProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/profileservice.ProfileService/CreateProfile',
            profile__pb2.CreateProfileRequest.SerializeToString,
            profile__pb2.CreateProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
