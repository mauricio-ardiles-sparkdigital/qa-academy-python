def get_age_range(age):
    """Recibe el parametro age (int) y devuelve el status de la persona"""
    if age < 18:
        return 'menor'
    elif 18 <= age < 65:
        return 'mayor'
    else:
        return 'jubilado'


def person_to_string(name_param, last_name_param, age_status_param, message):
    return "Su nombre es: {} {} y usted es {}. {}".format(name_param, last_name_param, age_status_param, message)


def menor_options():
    """Devuelve un string con las caracteristicas del juguete seleccionado
       Para este ejemplo solo se ingresara los siguientes valores:
       is_electronic = si / no
       can_walk = si / no
    """
    is_electronic = input('El juguete es electronico? (si/no): ')
    while is_electronic != 'si' and is_electronic != 'no':
        is_electronic = input('Ingrese una opcion valida. El juguete es electronico? (si/no): ')

    toy_color = input('Ingrese el color deseado para su juguete: ')

    can_walk = input('El juguete puede caminar? (si/no): ')
    while can_walk != 'si' and can_walk != 'no':
        can_walk = input('Ingrese una opcion valida. El juguete puede caminar? (si/no): ')

    return "El juguete deseado {} es electronico, su color es {} y el juguete {} puede caminar".format(is_electronic,
                                                                                                       toy_color,
                                                                                                       can_walk)


def mayor_options():
    """Devuelve un string con las caracteristicas de la prenda seleccionada
           Para este ejemplo solo ingresara los siguientes valores:
           kind_of_clothes = camisa / pantalon
        """
    kind_of_clothes = input('Desea una camisa o un pantalon?: ')
    while kind_of_clothes != 'camisa' and kind_of_clothes != 'pantalon':
        kind_of_clothes = input('Ingrese una opcion valida. Desea una camisa o un pantalon?: ')

    clothes_color = input('Ingrese el color deseado: ')
    size = input('Ingrese el talle: ')
    return "Producto deseado: {}, su color es {} y su talle es {}".format(kind_of_clothes, clothes_color, size)


def jubilado_options():
    """Devuelve un string con el destino seleccionado por la persona jubilada para viajar
       Destinos validos:  Federacion , Cataratas, Santa Teresita
    """
    destination = input('Ingrese lugar de destino (Federacion , Cataratas, Santa Teresita) ')
    while destination != 'Federacion' and destination != 'Cataratas' and destination != 'Santa Teresita':
        destination = input('Destino invalido, ingrese nuevamente (Federacion , Cataratas, Santa Teresita ')

    return "El lugar seleccionado para viajar es {}".format(destination)


def sell_by_age_status(age_status_param):
    """Estrategia de venta de acuerdo al status de la persona, retorna un string con la seleccion de compra"""
    if age_status_param == 'menor':
        return menor_options()
    elif age_status_param == 'mayor':
        return mayor_options()
    else:
        return jubilado_options()


person_qty = int(input('Ingrese cuantas personas:'))

for i in range(0, person_qty):
    # missing do .. while loop :-(
    age = int(input('Ingrese su Edad:'))

    while age < 1 or age > 120:
        age = int(input('Ingrese una edad en el rango de 1 a 120:'))

    name = input('Ingrese su Nombre:')
    last_name = input('Ingrese su Apellido:')
    age_status = get_age_range(age)
    sell_message = sell_by_age_status(age_status)

    print(person_to_string(name, last_name, age_status, sell_message))
