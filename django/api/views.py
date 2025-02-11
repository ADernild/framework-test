import asyncio
import time

from django.http import JsonResponse


def ping(request):
    return JsonResponse({"message": "pong"})


def sleep_sync(request):
    time.sleep(1)
    return JsonResponse({"message": "Synchronous sleep complete"}, status=200)


async def sleep_async(request):
    await asyncio.sleep(1)
    return JsonResponse({"message": "Asynchronous sleep complete"}, status=200)
