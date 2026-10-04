from server import PredictionInput


def test_valid_prediction_input():
    value = PredictionInput(
        pregnancies=6,
        glucose=148,
        blood_pressure=72,
        skin_thickness=35,
        insulin=0,
        bmi=33.6,
        diabetes_pedigree_function=0.627,
        age=50,
    )
    assert value.glucose == 148


def test_invalid_age_is_rejected():
    try:
        PredictionInput(
            pregnancies=0,
            glucose=100,
            blood_pressure=70,
            skin_thickness=20,
            insulin=80,
            bmi=25,
            diabetes_pedigree_function=0.3,
            age=130,
        )
    except Exception:
        return
    raise AssertionError("Expected invalid age to be rejected")
