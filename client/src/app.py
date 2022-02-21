from flask import Flask
import grpc
import hello_world_pb2
import hello_world_pb2_grpc

app = Flask(__name__)


def get_message(name):
    with grpc.insecure_channel('host.docker.internal:10000') as channel:
        stub = hello_world_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_world_pb2.HelloRequest(name=name))
        return response.message

@app.route("/hello/<name>")
def hello(name):
    return f"{get_message(name)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
