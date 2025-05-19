from .model import K3Score

def service_calculation(algorithm: K3Score) -> K3Score:
    # updated_formula = algorithm.formula + 100
    updated_formula = 100 + 100
    return K3Score(
        name=algorithm.name,
        description=algorithm.description,
        formula=updated_formula
    )
