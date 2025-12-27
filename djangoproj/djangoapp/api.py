from ninja import NinjaAPI
api = NinjaAPI()

@api.get("/")
def check(request):
    return {"message": "OK"}
