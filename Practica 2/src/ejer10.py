def inicializar_diccionario(rounds):
    dic = {}
    for name in rounds[0]['scores'].keys():
        dic[name] = {
            'total_points' : 0,
            'rounds_won' : 0,
            'points_best_round' : 0,
            'average' : 0.0
        }
    return dic
        #print(name)




def imprimir_posiciones(sort):
    print(f'{'Cocinero':<13} {'Puntaje':<10}')
    for name, data in sort:
        print(f"{name:<13} {data['total_points']:<5} pts")
    print("-" * 35)




def imprimir_tabla_final(sort, round_count):
    print('Tabla de posiciones final:')
    print(f'{'Cocinero':<13} {'Puntaje':<10} {'Rondas ganadas':<16} {'Mejor ronda':<13} {'Promedio':<10}')
    for name,data in sort:
        data['average'] = data['total_points'] / round_count
        print(f'{name:<13} {data['total_points']:<10} {data['rounds_won']:<16} {data['points_best_round']:<13} {data['average']:<10}')

