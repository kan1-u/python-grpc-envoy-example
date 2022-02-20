from grpc.tools import protoc
import sys


protoc.main(
    (
        '',
        '-I./protos',
        '--python_out=./server/src',
        '--grpc_python_out=./server/src',
        './protos/hello_world.proto',
    )
)

protoc.main(
    (
        '',
        '-I./protos',
        '--python_out=./client/src',
        '--grpc_python_out=./client/src',
        './protos/hello_world.proto',
    )
)
