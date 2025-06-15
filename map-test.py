data = [
    {
        "nombre": "L",
        "apellido": "Lawliet",
        "RUT": "12.123.442-3"
    },
    {
        "nombre": "Light",
        "apellido": "Yagami",
        "RUT": "1.111.2343-"
    },
]

def corregir(persona):
    return {
        "name": persona["nombre"],
        "dni": persona["RUT"].replace('.', '').replace('-', '')
    }

data = list(map(corregir, data))
print(data)