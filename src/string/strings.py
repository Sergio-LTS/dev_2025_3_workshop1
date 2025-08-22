class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        resultado = ""
        for char in texto:
            resultado = char + resultado
        return resultado
    
    def contar_vocales(self, texto):
       return sum(1 for c in texto.lower() if c in "aeiou")
    
    def contar_consonantes(self, texto):
        return sum(1 for c in texto.lower() if c.isalpha() and c not in "aeiou")
    
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower()
    
    def contar_palabras(self, texto):
       return len(texto.split())
    
    def palabras_mayus(self, texto):
        return " ".join(p.capitalize() for p in texto.split())
    
    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())
    
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] == "-":
            texto = texto[1:]
        return all(c in "0123456789" for c in texto)
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass