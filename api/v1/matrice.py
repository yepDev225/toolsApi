from fastapi import APIRouter, HTTPException
from schemas.matrice_schema import DbMatriceIn, MatrixOut
from api.deps import safe_array
from starlette import status
import numpy as np

route = APIRouter(
    tags=["Matrice"],
    prefix="/matrice"
)
error_detail= {"dim": "Les deux matrices doivent etre de même dimension.", "mulcolrow": "Le nombre de colonne de la première matrice dois être égale au nombre de ligne de la deuxieme", "singular":"la matrice n'est pas inversible", "square": "la matrice doit être une matrice carrée"}

@route.post("/addition", status_code=status.HTTP_200_OK, response_model=MatrixOut)
async def addition_matrice(matrices_datas:DbMatriceIn):
    try:
        a= safe_array(matrices_datas.first)
        b= safe_array(matrices_datas.last)
        if a.shape != b.shape:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error_detail["dim"])
        return (a+b).tolist()
    except ValueError as ve:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@route.post("/soustraction", status_code=status.HTTP_200_OK, response_model=MatrixOut)
async def soustract_matrice(matrices_datas:DbMatriceIn):
    try:
        a= safe_array(matrices_datas.first)
        b= safe_array(matrices_datas.last)
        if a.shape != b.shape:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error_detail["dim"])
        c = a-b
        
        return c.tolist()
    except ValueError as ve:
            raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@route.post("/multiplication", status_code=status.HTTP_200_OK, response_model=MatrixOut)
async def multiply_matrice(matrices_datas:DbMatriceIn):
    try:
        a= safe_array(matrices_datas.first)
        b= safe_array(matrices_datas.last)
        if a.shape[1] != b.shape[0]:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error_detail["mulcolrow"])
        
        return np.matmul(a,b).tolist()
    except ValueError as ve:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@route.post("/inverse", status_code=status.HTTP_200_OK, response_model=MatrixOut)
def get_inverse(matrix:MatrixOut):
    try:
        matrix = safe_array(matrix) 
        if matrix.shape[0] != matrix.shape[1]:
             raise ValueError(error_detail["square"])
        if np.linalg.det(matrix) == 0:
            raise ValueError(error_detail["singular"])
        return np.linalg.inv(matrix).tolist()
    except ValueError as ve:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@route.post("/transposition", status_code=status.HTTP_200_OK, response_model=MatrixOut)
def get_transpose(matrix:MatrixOut):
    try:
        matrix = safe_array(matrix) 
        return np.linalg.matrix_transpose(matrix).tolist()
    except ValueError as ve:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@route.post("/determinant", status_code=status.HTTP_200_OK, response_model=float)
def get_transpose(matrix:MatrixOut):
    try:
        matrix = safe_array(matrix)
        if matrix.shape[0] != matrix.shape[1]:
             raise ValueError(error_detail["square"])
        return np.linalg.det(matrix).tolist()
    except ValueError as ve:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))



