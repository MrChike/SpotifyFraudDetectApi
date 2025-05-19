from .model import K4Score

def service_calculation(algorithm: K4Score) -> K4Score:
    # updated_formula = algorithm.formula + 100
    updated_formula = 100 + 100
    return K4Score(
        name=algorithm.name,
        description=algorithm.description,
        formula=updated_formula
    )
