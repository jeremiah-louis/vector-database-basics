from pymilvus import MilvusClient
from decouple import config
# Authentication enabled with a cluster user
client = MilvusClient(
    uri=config("MILVUS_URL"),
    token=config("MILVUS_TOKEN"), # replace this with your token
)

print(client)