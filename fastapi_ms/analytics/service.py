from .model import K1Score

def service_calculation(algorithm: K1Score) -> K1Score:
    # updated_formula = algorithm.formula + 100
    updated_formula = 100 + 100
    return K1Score(
        name=algorithm.name,
        description=algorithm.description,
        formula=updated_formula
    )
