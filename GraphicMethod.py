import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


class ecuacionPL:
        
    

    def __init__(self):
        self.restricciones_valores = []
        self.restricciones_solucion = []
        self.funcion_objetivo = []
        self.igualidades = []
    
    
        



def graphicMethod(restricciones_valores = [[1,2],[3,2],[5,2]],restricciones_solucion = [80,160,200],funcion_objetivo = [2000,2000],igualidades = ['>=','>=','>='],isMin = True):
    A_ub = []
    B_ub = []
    x1_bounds = (0,None)
    x2_bounds = (0,None)
    ecuacion = ecuacionPL()
    x2_restricciones = []
    
    x1 = np.linspace(0,60,10000)
    for valor, sol, igual in zip(restricciones_valores, restricciones_solucion, igualidades):
        if igual == '<=':
            A_ub.append(valor)
            B_ub.append(sol)
        elif igual == '>=':
            # Multiplicar por -1 para convertir >= en <=
            A_ub.append([-v for v in valor])
            B_ub.append(-sol)
    
    for valor,sol,igual in zip(restricciones_valores,restricciones_solucion,igualidades):
        x1_value = valor[0]
        x2_value = valor[1]
        x2 = (sol - x1_value*x1)/x2_value
        NotNegative = ((x2 >= 0) & (x1 >=0))
        plt.plot(x1,x2,label = f'{x1_value}x1 + {x2_value}x2 {igual} {sol}')
    
    A = np.array(A_ub)
    B = np.array(B_ub)
    
    if (isMin):
        plt.fill_between(x1,200,x2 ,where=NotNegative, alpha=0.2, color='green', label='Región Factible')
        
    else:
        plt.fill_between(x1, 0, x2, where=NotNegative, alpha=0.2, color='green', label='Región Factible')
    
    plt.xlim(x1_bounds)
    plt.ylim(x2_bounds)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    
    c = np.array(funcion_objetivo)
     
    if (isMin): 
        res = linprog(c,A_ub=A,b_ub=B,bounds=(x1_bounds,x2_bounds),method='highs')
    else:
        res = linprog(-c,A_ub=A,b_ub=B,bounds=(x1_bounds,x2_bounds),method='highs')
    
    vertice = (res.x[0],res.x[1])
    plt.show()
    
    print(f"el maximo se alcanza con x1={res.x[0]} y x2={res.x[1]} con un valor de {res.fun}")

graphicMethod()


    