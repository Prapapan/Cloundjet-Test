from yourfactories import PersonFactory



def test_group_letter():

    person = PersonFactory.build(group__name='admins')

    assert person.group_letter() == 'A'
