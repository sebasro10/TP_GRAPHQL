# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import showtime_pb2 as showtime__pb2


class ShowtimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Home = channel.unary_unary(
                '/Showtime/Home',
                request_serializer=showtime__pb2.Empty2.SerializeToString,
                response_deserializer=showtime__pb2.Message2.FromString,
                )
        self.GetTimes = channel.unary_unary(
                '/Showtime/GetTimes',
                request_serializer=showtime__pb2.Empty2.SerializeToString,
                response_deserializer=showtime__pb2.Schedule.FromString,
                )
        self.GetMoviesByDate = channel.unary_unary(
                '/Showtime/GetMoviesByDate',
                request_serializer=showtime__pb2.Date.SerializeToString,
                response_deserializer=showtime__pb2.MoviesByDate.FromString,
                )


class ShowtimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Home(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMoviesByDate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShowtimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Home': grpc.unary_unary_rpc_method_handler(
                    servicer.Home,
                    request_deserializer=showtime__pb2.Empty2.FromString,
                    response_serializer=showtime__pb2.Message2.SerializeToString,
            ),
            'GetTimes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimes,
                    request_deserializer=showtime__pb2.Empty2.FromString,
                    response_serializer=showtime__pb2.Schedule.SerializeToString,
            ),
            'GetMoviesByDate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMoviesByDate,
                    request_deserializer=showtime__pb2.Date.FromString,
                    response_serializer=showtime__pb2.MoviesByDate.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Showtime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Showtime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Home(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Showtime/Home',
            showtime__pb2.Empty2.SerializeToString,
            showtime__pb2.Message2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Showtime/GetTimes',
            showtime__pb2.Empty2.SerializeToString,
            showtime__pb2.Schedule.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMoviesByDate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Showtime/GetMoviesByDate',
            showtime__pb2.Date.SerializeToString,
            showtime__pb2.MoviesByDate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
