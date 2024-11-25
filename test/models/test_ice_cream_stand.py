from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available_success(self):
        # Setup
        test_flavors = ["Morango", "Chocolate", "Creme"]
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)
        icecream.open_restaurant()

        # Chamada
        resultado = icecream.flavors_available()

        # Validação
        resultado_esperado = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
        for flavor in test_flavors:
            resultado_esperado += f"\t-{flavor}"

        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_flavors_out_of_stock(self):
        # Setup
        test_flavors = []
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.flavors_available()

        # Validação
        resultado_esperado = "Estamos sem estoque atualmente!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_find_flavor(self):
        assert False

    def test_add_flavor(self):
        assert False
