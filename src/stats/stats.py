class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: El valor mediano
            
        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        pass
    
    def moda(self, numeros):
        if not numeros:
            return None
        frecuencias = {}
        max_freq = 0
        moda_val = numeros[0]
        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1
            if frecuencias[num] > max_freq:
                max_freq = frecuencias[num]
                moda_val = num
        return moda_val
    
    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0
        media = self.promedio(numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        varianza = suma_cuadrados / len(numeros)
        return varianza ** 0.5
    
    def varianza(self, numeros):

        if not numeros:
            return 0
        media = self.promedio(numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        return suma_cuadrados / len(numeros)
    
    def rango(self, numeros):

        if not numeros:
            return 0
        return max(numeros) - min(numeros)