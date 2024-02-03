# Gas prices dictionary
GAS_PRICES = {1: 1.742, 2: 1.885, 3: 1.681, 4: 1.780, 5: 1.489}

# Constants
IVA = 0.21
GASOLINE_95 = 1.742
GASOLINE_98 = 1.885
DIESEL_A = 1.681
DIESEL_A1 = 1.780   
GASOLINE_100 = 1.489

# Types of gasoline, you can add as many as you want
TYPES_GASOLINE = {
    1: {"name": "Gasoline Regular 95 octanos", "price": GASOLINE_95},
    2: {"name": "Gasoline Premium 98 octanos", "price": GASOLINE_98},
    3: {"name": "Diesel A", "price": DIESEL_A},
    4: {"name": "Diesel A+", "price": DIESEL_A1},
    5: {"name": "Gasoline Premium 100 octanos", "price": GASOLINE_100}
}

# Welcome messages and the prices of the gasoline
def display_petrol_prices():
    # Print welcome and price information
    print("\n\n\n-------------------------Bienvenido a SHELL Estación de Servicio--------------------------------\n")
    print("--------------------------------Gracias por su visita-------------------------------------------\n")
    print("\n                    Estos son los precios actuales de la gasolina:\n\n")
    # Print prices for different types of gasoline
    print(f"             1. Regular 95 Octanos: €{GASOLINE_95} por litro\n")
    print(f"             2. Premium 98 Octanos: €{GASOLINE_98} por litro\n")
    print(f"             3. Diesel A: €{DIESEL_A} por litro\n")
    print(f"             4. Diesel A+: €{DIESEL_A1} por litro\n")
    print(f"             5. S Premium 100 Octanos: €{GASOLINE_100} por litro\n\n")

# Calculate the total cost and the gas type, and choose which gas type to use
def calculate_total_cost(gas_type, liters):
    if gas_type not in GAS_PRICES:
        raise ValueError(f"Tipo de gas no válido: {gas_type}. Por favor escriba 1, 2, 3, 4 o 5")

    price_per_liter = GAS_PRICES[gas_type]

    # IVA rate in this case 21%
    IVA_RATE = 0.21
    
    price_per_liter_without_iva, _, _ = calculate_iva_details(price_per_liter)
    
    total_cost = round(price_per_liter_without_iva * liters * (1 + IVA_RATE), 2)

    return total_cost, price_per_liter, price_per_liter_without_iva

# Calculate price details with IVA_RATE
def calculate_iva_details(price_with_iva):
    
    IVA_RATE = 0.21
    
    price_without_iva = round(price_with_iva / (1 + IVA_RATE), 2)

    iva_amount = round(price_without_iva * IVA_RATE, 2)

    price_with_iva_again = round(price_without_iva + iva_amount, 2)

    return price_without_iva, iva_amount, price_with_iva_again

# A while loop to keep the program running until the user quits
def calculate_change(paid, total_cost):
    if paid < total_cost:
        raise ValueError(f"\nEl dinero pagado (€{paid}) es menor que el precio total (€{total_cost}). Por favor pague el precio correcto.")
    return round(paid - total_cost, 2)

# Get customer information
def get_customer_info():
    name = input("\n     Nombre: ")
    address = input("\n     Dirección: ")
    dni = input("\n     DNI: ")
    phone_number = input("\n     Teléfono: ")
    postal_code = input("\n     Código postal: ")
    return name, address, dni, phone_number, postal_code

# Print the receipt
def print_receipt(gas_type, liters, total_cost, paid, change, name, address, dni, postal_code, phone_number=None):
    if name:
        print("\n\n------------------------SHELL Estación de Servicio----------------------------")
        print(f"\nNombre: {name}")
        print(f"Dirección: {address}")
        print(f"DNI: {dni}")
        if phone_number is not None:
            print(f"Teléfono: {phone_number}")
        print(f"Código postal: {postal_code}")
    else:
        print("\n\n------------------------SHELL Estación de Servicio------------------------------")
    print(f"\nTipo de gasolina: {TYPES_GASOLINE[gas_type]['name']}")
    print(f"Cantidad de litros: {liters}")
    print(f"Cantidad pagada: €{paid}")
    print(f"Precio total: €{total_cost}")
    print(f"Cambio devuelto: €{change}")
    # Calculate IVA amount and add it to the receipt
    iva_amount = round(total_cost - (total_cost / (1 + IVA)), 2)
    print(f"IVA (21%): €{iva_amount}")
    print("\n--------------------------------------------------------------------------------\n")

# Main function
def main():
    while True:
        display_petrol_prices()

        try:
            gas_type = int(input("\n ¿Qué tipo de gasolina desea? (1, 2, 3, 4 o 5): "))
            liters = float(input("\n     Cantidad de litros que desea poner: "))

            total_cost, price_per_liter, price_per_liter_without_iva = calculate_total_cost(gas_type=gas_type, liters=liters)

            print(f"\n       Ha elegido {liters} litros de {TYPES_GASOLINE[gas_type]['name']}")

            _, iva_amount_per_liter, _ = calculate_iva_details(price_per_liter)

            print(f"\n         Precio por litro sin IVA: €{price_per_liter_without_iva}")
            print(f"\n         IVA por litro: €{iva_amount_per_liter}\n")
            print(f"       Precio por litro IVA incluido: €{price_per_liter}")

            total_iva_amount = round(iva_amount_per_liter * liters, 2)
            print(f"\n     IVA Total: €{total_iva_amount}")

            print(f"\n Precio Final: €{total_cost}")

            while True:
                try:
                    paid = float(input("\n     Cantidad pagada por el cliente: "))
                    change = calculate_change(paid, total_cost)
                    break
                except ValueError as e:
                    print(e)

            # Capture the user's choice for needing a receipt
            receipt_needed = input("\n ¿Necesita una factura? (s/n): ")

            if receipt_needed.lower() == 's':
                name, address, dni, phone_number, postal_code = get_customer_info()
                print_receipt(gas_type=gas_type, liters=liters, total_cost=total_cost, paid=paid, change=change, name=name, address=address, dni=dni, postal_code=postal_code)
            else:
                # If the user doesn't need a receipt, print a simplified receipt
                print_receipt(gas_type=gas_type, liters=liters, total_cost=total_cost, paid=paid, change=change, name=None, address=None, dni=None, phone_number=None, postal_code=None)


        except ValueError as e:
            print(e)

        answer = input("\n Desea hacer otra operación....(y/n): ")
        if answer.lower() == 'n':
            print("\n          Gracias por visitarnos, le esperamos de vuelta\n ")
            break

# Start the main program
if __name__ == "__main__":
    main()
