import asyncio
import numpy as np
from scipy.sparse import csr_matrix
from pymilvus import MilvusClient, AsyncMilvusClient, DataType, RRFRanker, AnnSearchRequest

client = MilvusClient("./milvus_demo.db")
client.create_collection(
    collection_name="demo_collection",
    dimension=384  # The vectors we will use in this demo has 384 dimensions
)

# Connect to Milvus server using AsyncMilvusClient
async_client = AsyncMilvusClient(
    uri="http://localhost:19530",
    token="root:Milvus"
)

loop = asyncio.get_event_loop()


###############################################################################

import asyncio
from pymilvus import AsyncMilvusClient

async def my_async_function():
    client = AsyncMilvusClient(uri="http://localhost:19530")
    # This is an asynchronous call and requires 'await'
    await client.insert("my_collection", data=my_data)
    await client.close()

# Run the async function
asyncio.run(my_async_function())
