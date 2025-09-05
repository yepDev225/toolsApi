from pydantic import BaseModel
from typing import List

class DbMatriceIn(BaseModel):
    first: List[List[float]]
    last: List[List[float]]


MatrixOut = List[List[float]]
