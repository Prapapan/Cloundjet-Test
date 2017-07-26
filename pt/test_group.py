import pytest



@pytest.mark.django_db

def test_group_letter():

    person = PersonFactory.creat(group__name='admins')

    assert person.group_letter() == 'A'
