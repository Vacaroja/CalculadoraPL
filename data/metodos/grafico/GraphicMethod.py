import itertools
import math
from data.metodos.grafico.normalizar_matriz import normalizar_matriz
from data.metodos.simplex.SimplexMethod import SimplexMethod

def metodo_grafico(matrix,is_min,igualdades):
    matrix_ultima = matrix[-1]
    matriz = normalizar_matriz(matrix_ultima,igualdades)
    print("matriz normalizada",matriz)
    resultado = procesar_grafico_completo(matriz, is_min)
    print("resultado grafico",resultado)
    return resultado


def procesar_grafico_completo(matrix, is_min):
    idx_x1, idx_x2 = 1, 2
    idx_sol = len(matrix[0]) - 1
    restricciones = matrix[1:]
    
    # 1. Definir líneas (Restricciones + Ejes de no negatividad)
    eje_x = [0] * len(matrix[0]); eje_x[idx_x1] = 1; eje_x[idx_sol] = 0.
    print("eje x",eje_x)
    eje_y = [0] * len(matrix[0]); eje_y[idx_x2] = 1; eje_y[idx_sol] = 0
    print("eje y",eje_y)
    todas_las_lineas = restricciones + [eje_x, eje_y]
    print("todas las lineas",todas_las_lineas)
    
    vertices = []

    # 2. Calcular intersecciones
    for r1, r2 in itertools.combinations(todas_las_lineas, 2):
        a1, b1, c1 = r1[idx_x1], r1[idx_x2], r1[idx_sol]
        a2, b2, c2 = r2[idx_x1], r2[idx_x2], r2[idx_sol]
        
        denominador = (a1 * b2) - (a2 * b1)
        if denominador != 0:
            x = (c1 * b2 - c2 * b1) / denominador
            y = (a1 * c2 - a2 * c1) / denominador
            
            # Validar factibilidad
            if x >= -1e-7 and y >= -1e-7:
                cumple = True
                for res in restricciones:
                    if (res[idx_x1] * x + res[idx_x2] * y) > (res[idx_sol] + 1e-7):
                        cumple = False
                        break
                if cumple:
                    punto = (round(x, 4), round(y, 4))
                    if punto not in vertices: vertices.append(punto)

    # 3. Ordenar para Chart.js (Polígono convexo)
    if not vertices: return None
    cx = sum(p[0] for p in vertices) / len(vertices)
    print("cx",cx)
    cy = sum(p[1] for p in vertices) / len(vertices)
    print("cy",cy)
    vertices.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    
    # 4. Encontrar el Punto Óptimo
    # Extraemos coeficientes de la fila Z (ojo: en Simplex suelen estar con signo invertido)
    # Si tu matriz tiene -4 y -4 para Z = 4x1 + 4x2, usamos el valor absoluto o corregimos
    c1_obj = abs(matrix[0][idx_x1])
    c2_obj = abs(matrix[0][idx_x2])
    
    mejor_z = float('inf') if is_min else float('-inf')
    punto_optimo = None

    for vx, vy in vertices:
        z_actual = c1_obj * vx + c2_obj * vy
        if is_min:
            if z_actual < mejor_z:
                mejor_z, punto_optimo = z_actual, {"x": vx, "y": vy}
        else:
            if z_actual > mejor_z:
                mejor_z, punto_optimo = z_actual, {"x": vx, "y": vy}

    return {
        "poligono": [{"x": p[0], "y": p[1]} for p in vertices],
        "optimo": punto_optimo,
        "valor_z": round(mejor_z, 2)
    }


    


    