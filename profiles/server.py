try:  #importing dependencies and system variables
    import os
    import sys
    from concurrent import futures
    import grpc
    from dotenv import load_dotenv
    import django

    load_dotenv()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") 

    # Extend sys.path with the Django project path
    project_path = os.getenv('DJANGO_PROJECT_FULL_PATH')
    if project_path:
        sys.path.extend([project_path])
        if 'setup' in dir(django):
            django.setup()
    else:
        raise ImportError("DJANGO_PROJECT_FULL_PATH environment variable not set.")

except ModuleNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)

try: #importing all the required django components (models,protos,handlers...)
    from profiles.models import UserProfile
    from profiles.protos import profile_pb2_grpc,profile_pb2
except ModuleNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)


class ProfileService(profile_pb2_grpc.ProfileServiceServicer):
    """
    ProfileService handles all the possible gRPC connections mentioned in the 
    profile.proto file . The methods of this class are responsible for that
    
    """

    def CreateProfile(self, request, context):
        """Handles the CreateProfile gRPC service.

        This function is responsible for processing gRPC requests to create a new user profile.

        Args:
            request: An instance of the gRPC request message containing information to create the profile.
            context: The gRPC context, providing information about the request's context.

        Returns:
            msg: A gRPC response message indicating the result of the create profile operation.
            status: A gRPC response message indicating the status of the create profile operation through status codes.
            error: A gRPC response message indicating the errors encounterd in the create profile operation if any.
        """
        try:
            # Get the username and user_id from the request
            username = request.username
            user_id = request.user_id
            
            # Get the profile_image_url from the request, or use a default value if not provided
            # If profile_image_url is not provided or is an empty string, use a default image URL
            profile_image_url = request.profile_image_url or 'https://cdn.vectorstock.com/i/1000x1000/75/67/programmer-computer-expert-chalk-white-icon-vector-37237567.webp'
            
        except Exception as e:
            # If an exception occurs, handle it here
            print(f"Error: {e}")
            response = profile_pb2.CreateProfileResponse(
                status = 400,
                msg = 'Invalid Request not enough credentials',
                error = str(e),
            )
            #returning response to client
            return response
        try:
            # Double-check if the user profile with the credentials exists in the database using the provided data
            if UserProfile.objects.filter(username=username).exists() or UserProfile.objects.filter(user_id=user_id).exists():
                response = profile_pb2.CreateProfileResponse(
                    status=400,
                    msg='An profile with this username or user_id already exists',
                    error='Duplicate user profile',
                )
                #returning response to client
                return response
            else:
                # Continue with creating the user profile if it doesn't already exist
                UserProfile.objects.create(username=username, user_id=user_id, profile_image_url=profile_image_url)
                response = profile_pb2.CreateProfileResponse(
                    status=200,
                    msg='User profile created successfully',
                )
                #returning response to client
                return response
        except Exception as e:
            # Handle exceptions that might occur during user profile creation
            response = profile_pb2.CreateProfileResponse(
                status=500,
                msg='Failed to create user profile',
                error=str(e),  # Include the exception message in the response
            )
            #returning response to client
            return response
            
def serve():
    """Starts the gRPC server to handle PostService requests.

    Creates a gRPC server, adds the PostService implementation, and starts serving
    on the specified port.

    Usage:
        serve()

    Returns:
        None
    """
    # Create a gRPC server with a ThreadPoolExecutor
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the ProfileService implementation to the server
    profile_pb2_grpc.add_ProfileServiceServicer_to_server(ProfileService(), server)

    # Specify the port to listen on (insecure)
    server.add_insecure_port('[::]:50051')

    # Start the gRPC server
    server.start()
    
    #printing this on the console as a conformation for the successful start of the server
    print("server started running on port [::]:50051")

    # Wait for the server to be terminated (e.g., manually stopping the server)
    server.wait_for_termination()

if __name__ == '__main__':
    # If this script is the main entry point, start the gRPC server
    serve()














#  class PostService(post_pb2_grpc.PostServiceServicer):
#     def __init__(self):
#         self.status = {
#             'non_status': post_pb2.PostStatus.NO_STATUS,
#             'accepted': post_pb2.PostStatus.ACCEPTED,
#             'rejected': post_pb2.PostStatus.REJECTED,
#         }

#     def Search(self, request, context):
#         search_key = request.search_key
#         posts = Post.objects.filter(
#             Q(title__icontains=search_key),
#             Q(body__icontains=search_key),
#         )
#         responds = []
#         for post in posts:
#             tags = [tag_pb2.Tag(id=tag.id, title=tag.title, body=tag.body) for tag in post.tags.all()]
#             responds.append(post_pb2.Post(
#                 id=post.id,
#                 title=post.title,
#                 body=post.body,
#                 tags=tags,
#                 post_status=self.status[post.status],
#             ))
#         return post_pb2.PostsRespond(posts=responds)


#     def GetPostByID(self, request, context):
#         post_id = request.id
#         post = Post.objects.filter(id=post_id).first()
#         tags = [tag_pb2.Tag(id=tag.id, title=tag.title, body=tag.body) for tag in post.tags.all()]
#         respond = post_pb2.Post(
#             id=post.id,
#             title=post.title,
#             body=post.body,
#             tags=tags,
#             post_status=self.status[post.status],
#         )
#         return respond


