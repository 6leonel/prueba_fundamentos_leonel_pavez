#leonel pavez / Evaluación Formativa N°2 30/04/2024 
#FUNDAMENTOS DE PROGRAMACION_003D


# -*- coding: utf-8 -*-
class SushiDelivery:
    def __init__(self):
        self.menu = {
            1: ("pikachu Roll", 4500),
            2: ("otaku Roll", 5000),
            3: ("pulpo Venenoso Roll", 5200),
            4: ("anguila Electrica Roll", 4800)
        }
        self.order = {}
        self.discount_code = "soyotaku"
        self.discount_rate = 0.1

    def display_menu(self):
        print("***** MENU *****")
        for key, value in self.menu.items():
            print(f"{key}. {value[0]} - ${value[1]}")
        print("****************")

    def add_to_order(self):
        self.display_menu()
        while True:
            choice = input("seleccione un numero de roll para agregar al pedido (1-4), o 'X' para finalizar: ")
            if choice.upper() == "X":
                break
            try:
                choice = int(choice)
                if choice in self.menu:
                    if choice not in self.order:
                        self.order[choice] = 1
                    else:
                        self.order[choice] += 1
                    print(f"{self.menu[choice][0]} agregado al pedido.")
                else:
                    print("por favor, seleccione una opcion valida.")
            except ValueError:
                print("por favor, ingrese un numero valido.")

    def apply_discount(self):
        code = input("¿tiene un codigo de descuento? Ingrese el codigo o 'X' para continuar sin descuento: ")
        if code.upper() == self.discount_code:
            subtotal = sum(self.menu[roll][1] * quantity for roll, quantity in self.order.items())
            discount = subtotal * self.discount_rate
            total = subtotal - discount
            print("descuento aplicado.")
            return total
        elif code.upper() == "X":
            subtotal = sum(self.menu[roll][1] * quantity for roll, quantity in self.order.items())
            print("continuando sin descuento.")
            return subtotal
        else:
            print("codigo no valido.")
            self.apply_discount()

    def display_order_details(self):
        print("***** DETALLE DEL PEDIDO *****")
        total_products = sum(self.order.values())
        print(f"TOTAL PRODUCTOS: {total_products}")
        print("******************************")
        for roll, quantity in self.order.items():
            print(f"{self.menu[roll][0]} : {quantity}")
        print("******************************")
        subtotal = sum(self.menu[roll][1] * quantity for roll, quantity in self.order.items())
        total = self.apply_discount()
        print(f"Subtotal por pagar: ${subtotal}")
        if total != subtotal:
            print(f"descuento por codigo: ${subtotal - total}")
        print(f"TOTAL: ${total}")

    def start_order(self):
        self.add_to_order()
        self.display_order_details()
        while True:
            choice = input("¿Desea realizar otro pedido? (si/no): ")
            if choice.lower() == "si":
                self.order = {}
                self.start_order()
            elif choice.lower() == "no":
                print("Gracias por su pedido. ¡Hasta luego!")
                break
            else:
                print("Por favor, responda con 'Si' o 'No'.")

if __name__ == "__main__":
    delivery = SushiDelivery()
    delivery.start_order()