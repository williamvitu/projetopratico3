from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    # Melhoria, adicionar anotação dos atributos (Fixed)
    def __init__(self, restaurant_name: str, cuisine_type: str, flavors_list: list[str]):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
    # Melhoria, validação nos atributos da classe (fixed)
        if not isinstance(restaurant_name, str):
            raise TypeError("O atributo 'restaurant_name' deve ser uma string.")
        if not isinstance(cuisine_type, str):
            raise TypeError("O atributo 'cuisine_type' deve ser uma string.")
        if not isinstance(flavors_list, list):
            raise TypeError("O atributo 'flavors_list' deve ser uma lista de strings.")

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        # Melhoria, validar se o restaurante está aberto e possui estoque (FIXED)
        if self.flavors:
            result = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                result += f"\t-{flavor}"
            return result
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento {self.flavors}!"
            else:
                return f"Não temos no momento {self.flavors}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                return "\nSabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Estamos sem estoque atualmente!"
