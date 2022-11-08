"""Tests for the Patient model."""

################################ Observation Tests
def test_create_observation():
    from inflammation.models import Observation
    
    new_obs = Observation(1, 3)
    
    assert new_obs.day == 1
    assert new_obs.value == 3

################################ Person Tests
def test_create_person():
    from inflammation.models import Person

    name = 'Alice'
    p = Person(name=name)

    assert p.name == name


################################ Patient Tests
def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_patient_is_person():
    """Check if a patient is a person. """
    from inflammation.models import Patient, Person
    alice = Patient("Alice")
    assert isinstance(alice, Person)
    
    
def test_patients_build_check_observation_list_order():
    """ checks that the patient list is corretly formated"""
    from inflammation.models import Patient
    p = Patient("Josh Mitchell")
    obs = p.add_observation(3)
    obs = p.add_observation(2)
    obs = p.add_observation(1) 
    assert p.observations is not None
    assert len(p.observations) == 3   
    assert str(p.observations[0]) == "3"
    assert str(p.observations[1]) == "2"
    assert str(p.observations[2]) == "1"
   
    
################################ Doctor Tests
def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Makan'
    d = Doctor(name=name)

    assert d.name == name
    
def test_doctor_is_person():
    """Check if a doctor is a person."""
    from inflammation.models import Doctor, Person
    doc = Doctor("Sheila Wheels")
    assert isinstance(doc, Person)

def test_doctor_build_check_patient_list_order():
    """ checks that the patient list is corretly formated"""
    from inflammation.models import Doctor, Patient
    doc = Doctor('Dan Makan')
    p = doc.add_patient(Patient("Alice1"))
    p = doc.add_patient(Patient("Alice2"))
    p = doc.add_patient(Patient("Alice3"))
    
    assert doc.patients is not None
    assert len(doc.patients) == 3   
    assert str(doc.patients[0]) == "Alice1"
    assert str(doc.patients[1]) == "Alice2"
    assert str(doc.patients[2]) == "Alice3"
    

