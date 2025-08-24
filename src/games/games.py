import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        Retorna "jugador1", "jugador2", "empate" o "invalid".
        """
        # Normalizar entradas
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        opciones = {"piedra", "papel", "tijera"}
        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"
        
        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }
        
        if reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"
    

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    

    def ta_te_ti_ganador(self, tablero):
        # Revisar filas
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        # Revisar columnas
        for col in range(3):
            if tablero[0][col] != " " and tablero[0][col] == tablero[1][col] == tablero[2][col]:
                return tablero[0][col]

        # Revisar diagonales
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            # Solo es victoria si NO hay espacios vacíos en el tablero
            if all(" " not in fila for fila in tablero):
                return tablero[0][0]

        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            if all(" " not in fila for fila in tablero):
                return tablero[0][2]

        # Si aún hay espacios vacíos → continua
        for fila in tablero:
            if " " in fila:
                return "continua"

        # Si no hay espacios y nadie ganó → empate
        return "empate"
    

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        """
        # Validar límites del tablero
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 
                0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False

        # Movimiento a la misma posición -> inválido
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        # La torre debe moverse en línea recta
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        
        # Movimiento horizontal
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][c] != " ":
                    return False
        
        # Movimiento vertical
        elif desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for f in range(desde_fila + paso, hasta_fila, paso):
                if tablero[f][desde_col] != " ":
                    return False
        
        return True
