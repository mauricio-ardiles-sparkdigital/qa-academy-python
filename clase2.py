def get_age_range(age):
    if age < 18:
        return 'menor'
    elif 18 <= age < 65:
        return 'mayor'
    else:
        return 'jubilado'


def person_to_string(name_param, last_name_param, age_status_param):
    return "Su nombre es: {} {} y usted es: {}".format(name_param, last_name_param, age_status_param)


person_qty = int(input('Ingrese cuantas personas:'))

for i in range(0, person_qty):
    # missing do .. while loop :-(
    age = int(input('Ingrese su Edad:'))

    while age < 1 or age > 120:
        age = int(input('Ingrese una edad en el rango de 1 a 120:'))

    name = input('Ingrese su Nombre:')
    last_name = input('Ingrese su Apellido:')
    age_status = get_age_range(age)

    print(person_to_string(name, last_name, age_status))
