import numpy as np
from typing import List

def safe_array(matrix: List) -> np.ndarray:
    try:
        arr = np.array(matrix, dtype=float)

        # Si vecteur 1D -> transformer en ligne
        if arr.ndim == 1:
            arr = arr.reshape(1, -1)  # devient matrice ligne

        if arr.ndim != 2:
            raise ValueError("Matrix must be 1D or 2D only")

        return arr
    except Exception as e:
        raise ValueError(f"Invalid matrix format: {str(e)}")
           