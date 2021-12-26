from fastapi import APIrouter

router = APIrouter()

@router.get("/eurocopa")
def eurocopa_root():
    return{"message" : "Bienvenidoa a la Eurocopa"}