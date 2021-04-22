def get_age_range(age):
    if age < 18:
        return 'menor'
    elif 18 <= age < 65:
        return 'mayor'
    elif 65 <= age <= 120:
        return 'jubilado'
    else:
        return 'cadaver'


def person_to_string(name, last_name, age_status):
    return "Su nombre es: {} {} y usted es: {}".format(name, last_name, age_status)


#name = input('Ingrese su Nombre:')
#last_name = input('Ingrese su Apellido:')
#age = input('Ingrese su Edad:')
#age_status = get_age_range(int(age))


#print(person_to_string(name, last_name, age_status))
