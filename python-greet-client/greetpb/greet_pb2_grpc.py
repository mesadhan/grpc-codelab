# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from greetpb import greet_pb2 as greetpb_dot_greet__pb2


class GreetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Greet = channel.unary_unary(
                '/greet.GreetService/Greet',
                request_serializer=greetpb_dot_greet__pb2.GreetRequest.SerializeToString,
                response_deserializer=greetpb_dot_greet__pb2.GreetResponse.FromString,
                )
        self.GreetManyTimesMethod = channel.unary_stream(
                '/greet.GreetService/GreetManyTimesMethod',
                request_serializer=greetpb_dot_greet__pb2.GreetManyTimesRequest.SerializeToString,
                response_deserializer=greetpb_dot_greet__pb2.GreetManyTimesResponse.FromString,
                )
        self.LongGreet = channel.stream_unary(
                '/greet.GreetService/LongGreet',
                request_serializer=greetpb_dot_greet__pb2.LongGreetRequest.SerializeToString,
                response_deserializer=greetpb_dot_greet__pb2.LongGreetResponse.FromString,
                )
        self.GreetEveryoneMethod = channel.stream_stream(
                '/greet.GreetService/GreetEveryoneMethod',
                request_serializer=greetpb_dot_greet__pb2.GreetEveryoneRequest.SerializeToString,
                response_deserializer=greetpb_dot_greet__pb2.GreetEveryoneResponse.FromString,
                )


class GreetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Greet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GreetManyTimesMethod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LongGreet(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GreetEveryoneMethod(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Greet': grpc.unary_unary_rpc_method_handler(
                    servicer.Greet,
                    request_deserializer=greetpb_dot_greet__pb2.GreetRequest.FromString,
                    response_serializer=greetpb_dot_greet__pb2.GreetResponse.SerializeToString,
            ),
            'GreetManyTimesMethod': grpc.unary_stream_rpc_method_handler(
                    servicer.GreetManyTimesMethod,
                    request_deserializer=greetpb_dot_greet__pb2.GreetManyTimesRequest.FromString,
                    response_serializer=greetpb_dot_greet__pb2.GreetManyTimesResponse.SerializeToString,
            ),
            'LongGreet': grpc.stream_unary_rpc_method_handler(
                    servicer.LongGreet,
                    request_deserializer=greetpb_dot_greet__pb2.LongGreetRequest.FromString,
                    response_serializer=greetpb_dot_greet__pb2.LongGreetResponse.SerializeToString,
            ),
            'GreetEveryoneMethod': grpc.stream_stream_rpc_method_handler(
                    servicer.GreetEveryoneMethod,
                    request_deserializer=greetpb_dot_greet__pb2.GreetEveryoneRequest.FromString,
                    response_serializer=greetpb_dot_greet__pb2.GreetEveryoneResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greet.GreetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Greet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.GreetService/Greet',
            greetpb_dot_greet__pb2.GreetRequest.SerializeToString,
            greetpb_dot_greet__pb2.GreetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GreetManyTimesMethod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greet.GreetService/GreetManyTimesMethod',
            greetpb_dot_greet__pb2.GreetManyTimesRequest.SerializeToString,
            greetpb_dot_greet__pb2.GreetManyTimesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LongGreet(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/greet.GreetService/LongGreet',
            greetpb_dot_greet__pb2.LongGreetRequest.SerializeToString,
            greetpb_dot_greet__pb2.LongGreetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GreetEveryoneMethod(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/greet.GreetService/GreetEveryoneMethod',
            greetpb_dot_greet__pb2.GreetEveryoneRequest.SerializeToString,
            greetpb_dot_greet__pb2.GreetEveryoneResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
