import grpc
from profiles.protos import profile_pb2_grpc,profile_pb2

#step 1 : Create Channel

channel = grpc.insecure_channel('localhost:50051')

#step 2 : Create client

client = profile_pb2_grpc.ProfileServiceStub(channel)

#step 3 : API call

request = profile_pb2.CreateProfileRequest(
    username="Anaz",
    user_id=2,
    profile_image_url="https://img.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_138676-2387.jpg?w=740&t=st=1699500630~exp=1699501230~hmac=b24973b64cc2f563099c02f0f0d0fde3caa3611bcf086fc17674934db52b887f"
)
response = client.CreateProfile(request)
print(response.status,response.msg,response.error)



# request = post_pb2.PostIDRequest(id=1)
# respond = client.GetPostByID(request)
# print(respond.title, respond.id)
