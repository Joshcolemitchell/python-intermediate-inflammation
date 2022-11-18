"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[4, 2, 5], [1, 6, 2], [4, 1, 9]], [4, 6, 9]),
        ([[4, -2, 5], [1, -6, 2], [-4, -1, 9]], [4, -1, 9]),
    ])
def test_daily_max(test, expected):
    """Test max function works for zeroes, positive integers, mix of positive/negative integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

def test_daily_max_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_max

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])
    npt.assert_array_equal(daily_max(test_input), test_result)
    
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[4, 2, 5], [1, 6, 2], [4, 1, 9]], [1, 1, 2]),
        ([[4, -2, 5], [1, -6, 2], [-4, -1, 9]], [-4, -6, 2]),
    ])
def test_daily_min(test, expected):
    """Test min function works for zeroes, positive integers, mix of positive/negative integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))
    
    
def test_daily_min_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_min

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])
    npt.assert_array_equal(daily_min(test_input), test_result)
  
def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])    
          
def test_daily_max_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_max

    with pytest.raises(TypeError):
        error_expected = daily_max([['Hello', 'there'], ['General', 'Kenobi']])
        
        
@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        (
            'hello',
            None,
            TypeError,
        ),
        (
            3,
            None,
            TypeError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        )
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if isinstance(test, list):
        test = np.array(test)
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(test), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(test), np.array(expected), decimal=2)

def tests_check_day_is_less_than_zero():
    from inflammation.models import Patient

    patient = Patient("test")

    with pytest.raises(ValueError):
        patient.add_observation(0, -1)

def tests_check_if_observation_exists():
    from inflammation.models import Patient
    from inflammation.models import DayAlreadyExistsError

    patient = Patient("test")

    patient.add_observation(0, 1)
    with pytest.raises(DayAlreadyExistsError):
        patient.add_observation(0, 1)

def tests_doctor_removes_patient_successfully():
    from inflammation.models import Patient
    from inflammation.models import Doctor

    doctor = Doctor("Dr. Jones")
    patient1 = Patient("Harry")
    patient2 = Patient("James")

    doctor.add_patient(patient1)
    doctor.add_patient(patient2)
    assert len(doctor.patients) == 2

    doctor.remove_patient(patient2)
    assert len(doctor.patients) == 1

    assert doctor.patients[0].name == "Harry"

def test_doctor_removes_not_existing_patient():
    from inflammation.models import Patient
    from inflammation.models import Doctor
    from inflammation.models import PatientDoesNotExistError

    doctor = Doctor("Dr. Jones")
    patient1 = Patient("Harry")
    patient2 = Patient("James")

    doctor.add_patient(patient1)
    doctor.add_patient(patient2)
    assert len(doctor.patients) == 2

    fake_patient = Patient("Sean")
    with pytest.raises(PatientDoesNotExistError):
        doctor.remove_patient(fake_patient)

def test_doctor_removes_not_existing_patient_in_empty_list():
    from inflammation.models import Patient
    from inflammation.models import Doctor
    from inflammation.models import PatientDoesNotExistError

    doctor = Doctor("Dr. Jones")

    fake_patient = Patient("Sean")
    with pytest.raises(PatientDoesNotExistError):
        doctor.remove_patient(fake_patient)