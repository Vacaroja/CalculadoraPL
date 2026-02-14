import itertools
import math
from data.metodos.grafico.normalizar_matriz import normalizar_matriz
from data.metodos.simplex.SimplexMethod import SimplexMethod

def metodo_grafico(matrix,is_min,igualdades):
    matriz = normalizar_matriz(matrix,igualdades)
    print("matriz normalizada",matriz)
    resultado = procesar_grafico_completo(matriz, is_min)
    print("resultado grafico",resultado)
    return resultado


def procesar_grafico_completo(matrix, is_min):
    idx_x1, idx_x2 = 1, 2
    idx_sol = len(matrix[0]) - 1
    restricciones = matrix[1:]
    tipo_solucion = "Optima Unica"
    # 1. Definir líneas (Ejes de no negatividad)
    eje_x = [0] * len(matrix[0]); eje_x[idx_x1] = 1; eje_x[idx_sol] = 0.
    eje_y = [0] * len(matrix[0]); eje_y[idx_x2] = 1; eje_y[idx_sol] = 0
    todas_las_lineas = restricciones + [eje_x, eje_y]
    
    vertices = []
    # 2. Calcular intersecciones (Igual que antes)
    for r1, r2 in itertools.combinations(todas_las_lineas, 2):
        a1, b1, c1 = r1[idx_x1], r1[idx_x2], r1[idx_sol]
        a2, b2, c2 = r2[idx_x1], r2[idx_x2], r2[idx_sol]
        
        denominador = (a1 * b2) - (a2 * b1)
        if denominador != 0:
            x = (c1 * b2 - c2 * b1) / denominador
            y = (a1 * c2 - a2 * c1) / denominador
            
            if x >= -1e-7 and y >= -1e-7:
                cumple = True
                for res in restricciones:
                    if (res[idx_x1] * x + res[idx_x2] * y) > (res[idx_sol] + 1e-7):
                        cumple = False
                        break
                if cumple:
                    punto = (round(x, 4), round(y, 4))
                    if punto not in vertices: vertices.append(punto)

    if not vertices: return None

    # --- NUEVA LÓGICA: Calcular puntos para las rectas de las restricciones ---
    # Determinamos un límite máximo para que las líneas no se vean cortadas
    max_x = max(p[0] for p in vertices) * 2 if vertices else 10
    max_y = max(p[1] for p in vertices) * 2 if vertices else 10
    limite = max(max_x, max_y, 10)

    rectas_para_grafico = []
    for res in restricciones:
        a, b, c = res[idx_x1], res[idx_x2], res[idx_sol]
        puntos_recta = []
        
        # Caso 1: La línea cruza el eje Y (x=0) -> y = c/b
        if b != 0:
            y_val = c / b
            if 0 <= y_val <= limite * 2: puntos_recta.append({"x": 0, "y": round(y_val, 2)})
        
        # Caso 2: La línea cruza el eje X (y=0) -> x = c/a
        if a != 0:
            x_val = c / a
            if 0 <= x_val <= limite * 2: puntos_recta.append({"x": round(x_val, 2), "y": 0})

        # Caso 3: Si la línea es horizontal o vertical, o solo tiene un punto, 
        # forzamos un segundo punto para que Chart.js dibuje la línea
        if len(puntos_recta) < 2:
            if a == 0 and b != 0: # Horizontal
                puntos_recta = [{"x": 0, "y": c/b}, {"x": limite, "y": c/b}]
            elif b == 0 and a != 0: # Vertical
                puntos_recta = [{"x": c/a, "y": 0}, {"x": c/a, "y": limite}]
        
        if puntos_recta:
            rectas_para_grafico.append(puntos_recta)

    # 3. Ordenar polígono (Igual que antes)
    cx = sum(p[0] for p in vertices) / len(vertices)
    cy = sum(p[1] for p in vertices) / len(vertices)
    vertices.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    
    # 4. Punto Óptimo (Igual que antes)
    c1_obj = abs(matrix[0][idx_x1]); c2_obj = abs(matrix[0][idx_x2])
    mejor_z = float('inf') if is_min else float('-inf')
    punto_optimo = None

    for vx, vy in vertices:
        z_actual = c1_obj * vx + c2_obj * vy
        if (is_min and z_actual < mejor_z) or (not is_min and z_actual > mejor_z):
            mejor_z, punto_optimo = z_actual, {"x": vx, "y": vy}
    
    # Validar Solución Múltiple
    conteo_optimos = 0
    for vx, vy in vertices:
        z_v = c1_obj * vx + c2_obj * vy
        if abs(z_v - mejor_z) < 1e-7: # Tolerancia para flotantes
            conteo_optimos += 1
    
    if conteo_optimos > 1:
        tipo_solucion = "Solucion Multiple"

    # Validar No Acotada (Lógica simple para Gráfico)
    # Si el valor de Z es absurdamente alto o los vértices no cierran
    if mejor_z > 1e10: 
        tipo_solucion = "No Acotada"

    return {
        "poligono": [{"x": p[0], "y": p[1]} for p in vertices],
        "optimo": punto_optimo,
        "valor_z": round(mejor_z, 2),
        "tipo": tipo_solucion,
        "rectas": rectas_para_grafico # <--- Enviamos las líneas aquí
    }


    


    