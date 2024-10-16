import variables
import constantes
import funciones
import clases
import metodos

def ejecutar_todos():
    print("=== Variables ===")
    variables.imprimir_variables()
    
    print("\n=== Constantes ===")
    constantes.imprimir_constantes()
    
    print("\n=== Funciones ===")
    funciones.imprimir_resultados()
    
    print("\n=== Clases ===")
    clases.ejecutar_clases()
    
    print("\n=== Métodos ===")
    metodos.ejecutar_metodos()
    

if __name__ == "__main__":
    ejecutar_todos()
