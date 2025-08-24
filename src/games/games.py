class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra",
        }

        j1 = jugador1.strip().lower()
        j2 = jugador2.strip().lower()

        if j1 == j2:
            return "empate"
        elif reglas[j1] == j2:
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
            return tablero[0][0]
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]

        # Verificar si hay espacios vacíos
        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        combinacion = []
        for i in range(longitud):
            combinacion.append(colores_disponibles[i % len(colores_disponibles)])
        return combinacion

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        # No puede quedarse en la misma casilla
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # Movimiento solo en línea recta
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        # Revisar obstáculos en el camino
        if desde_fila == hasta_fila:  # Movimiento horizontal
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][c] != " ":
                    return False
        else:  # Movimiento vertical
            paso = 1 if hasta_fila > desde_fila else -1
            for f in range(desde_fila + paso, hasta_fila, paso):
                if tablero[f][desde_col] != " ":
                    return False

        return True
    def validar_movimiento_alfil_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        # No puede quedarse en la misma casilla
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # Movimiento solo en diagonal
        if abs(desde_fila - hasta_fila) != abs(desde_col - hasta_col):
            return False

        # Revisar obstáculos en el camino
        paso_fila = 1 if hasta_fila > desde_fila else -1
        paso_col = 1 if hasta_col > desde_col else -1
        f, c = desde_fila + paso_fila, desde_col + paso_col
        while f != hasta_fila and c != hasta_col:
            if tablero[f][c] != " ":
                return False
            f += paso_fila
            c += paso_col

        return True