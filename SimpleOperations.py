import functools

class SimpleOperations:
    # Constructor de la clase (no tiene atributos)
    def __init__(self):
        pass


    def apply_discount(self, price, discount): # descuento del 25% -> 0.25
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        precio_con_descuento = price * (1 - discount) # Notacion para tratar con porcentajes decimales
        return precio_con_descuento

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""

        precio_con_tax = price * (1 + tax_rate)
        return precio_con_tax
        
# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
discount_10_percent = functools.partial(operations.apply_discount, discount=0.10)
tax_19_percent = functools.partial(operations.calculate_tax, tax_rate=0.19)

# twenty_percent_discount 
# vat_tax
twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

# Usar las funciones preconfiguradas.
precio_original = 100.0

precio_con_descuento_10 = discount_10_percent(precio_original)
precio_con_tax_19 = tax_19_percent(precio_original)
precio_con_descuento_20 = twenty_percent_discount (precio_original)
precio_con_vat_tax = vat_tax(precio_original)

print("Precio original:", precio_original)
print("Precio con descuento del 10%:", precio_con_descuento_10)
print("Precio final con impuesto del 19%:", precio_con_tax_19)
print("Precio con descuento del 20%:", precio_con_descuento_20)
print("Precio final con impuesto del 21%:", precio_con_vat_tax)



