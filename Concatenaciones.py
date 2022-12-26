#para concatenar varias variables en una:

name = "Alex"
last_name = "Brito Martinez"

#se puede usar:

full_name = name + " " + last_name
print(full_name)

# " " siendo el espacio entre name y last_name

#format es una manera de concatenar distintas variables de forma eficiente
#usando templates

template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

#otra manera

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2', template)

#tercera forma

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)
