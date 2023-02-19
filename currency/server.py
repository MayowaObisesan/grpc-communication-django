from concurrent import futures
import sys
import django

import grpc
import os
from gen_default_currency_pb2_grpc import add_CurrencyServicer_to_server

from gen_default_currency_pb2_grpc import CurrencyServicer

# from protos.gen_default_currency_pb2 import DefaultRequest, DefaultResponse
# import protos.gen_default_currency_pb2_grpc

sys.path.append(f"{os.getcwd()}/currency/settings.py")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency.settings")
django.setup()

from core.models import Currency

from gen_default_currency_pb2 import DefaultCurrencyRequest, DefaultCurrencyResponse


class GenDefaultCurrencyService(CurrencyServicer):
    def generateDefaultCurrency(self, request, context):
        print(f"request is: {request}")
        default_currencies = [
            Currency(user_id=request.user_id, name="Nigerian Naira", code="NGN"),
            Currency(user_id=request.user_id, name="United States Dollar", code="USD"),
        ]
        # Currency.objects.bulk_create(default_currencies)
        currency_ngn = Currency.objects.create(
            user_id=request.user_id, name="Nigerian Naira", code="NGN"
        )
        currency_usd = Currency.objects.create(
            user_id=request.user_id, name="United States Dollars", code="USD"
        )
        return DefaultCurrencyResponse(**{"id": 1, "name": currency_ngn.name})
        # return {"status": grpc.StatusCode.OK, "message": "Default currencies created"}


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CurrencyServicer_to_server(GenDefaultCurrencyService(), server)
    server.add_insecure_port("[::]:50051")
    print("Server started")
    server.start()
    server.wait_for_termination()


# if __name__ == "__main__":
serve()
