import argparse
from algorithm import gerar_grafo, calcular_propriedades

def main(ini, fim, stp, p):
    print("V    E    gmin  gmax  gmed   diam")
    print("-----------------------------------------------")

    for n in range(ini, fim + 1, stp):
        G = gerar_grafo(n, p)
        num_vertices, num_arestas, grau_min, grau_max, grau_medio, diametro = calcular_propriedades(G)
        
        # Imprime os resultados formatados
        print(f"{num_vertices:<4} {num_arestas:<4} {grau_min:<4} {grau_max:<4} {grau_medio:.1f}   {diametro}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processa os parâmetros para gerar e calcular propriedades de grafos.")
    parser.add_argument("ini", type=int, help="Valor inicial (ini)")
    parser.add_argument("fim", type=int, help="Valor final (fim)")
    parser.add_argument("stp", type=int, help="Valor do passo (stp)")
    parser.add_argument("p", type=float, help="Probabilidade (p)")

    args = parser.parse_args()
    main(ini=args.ini, fim=args.fim, stp=args.stp, p=args.p)