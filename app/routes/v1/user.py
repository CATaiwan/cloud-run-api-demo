from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def index():
    return [
        {
            "first_name": "Foo",
            "last_name": "Bar",
            "email": "foobar@main.com",
            "mobile": "12345678",
        },
        {
            "first_name": "Coo",
            "last_name": "Dar",
            "email": "coodar@main.com",
            "mobile": "87654321",
        },
    ]
