from concurrent import futures
import grpc
import hello_world_pb2
import hello_world_pb2_grpc


class GreeterService(hello_world_pb2_grpc.GreeterServicer):
    def __init__(self):
        pass

    def SayHello(self, request, context):
        name = request.name
        message = f'Hello {name}!'
        return hello_world_pb2.HelloReply(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_GreeterServicer_to_server(
        GreeterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
