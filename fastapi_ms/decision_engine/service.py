from .model import K2Score

def service_calculation(algorithm: K2Score) -> K2Score:
    # updated_formula = algorithm.formula + 200
    updated_formula = 200 + 200
    return K2Score(
        name=algorithm.name,
        description=algorithm.description,
        formula=updated_formula
    )
