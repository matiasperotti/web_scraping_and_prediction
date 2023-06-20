
import pandas as pd


dates = pd.read_csv('dates.csv')

last_match = #yqs
# funcion que busque la fecha anterior


if fecha_anterior not in dates.date:

    a = matches(fecha_anterior)

    # funcion que recolecta nombres de jugadores

    players = pd.read_csv('players.csv')

    for name in list_names:
        if name in players.name:
            # append estadisticas en nueva tabla
        else:
            # nueva_tabla.append(fifa_function.statistics(name))

    players.to_csv('players.csv')

    # nueva_tabla deberia ser la tabla donde esten los partidos y stats, y todo este if 
    # deberia estar preguntando tambien ahi por los juegos o algo asi




def matches():          ## esta funcion recolecta solo links de matches en el archivo matches.csv
                        ## en el caso de que hayan matches empieza a buscar en fechas anteriores a la del match mas viejo
    from datetime import date, datetime, timedelta

    while 1 == 1:
        dates = pd.read_csv('data/dates.csv')
        
        if(dates.empty):
            a = matches('')
            for match in a:
                dates.append({'date': date.today().strftime('%Y-%m-%d'), 'match': match})

        else:
            oldest = dates['date'].min()
            oldest = oldest.strftime('%Y-%m-%d')

            def previous_day(date):
                date = datetime.strptime(date, '%Y-%m-%d')
                p_date = date - timedelta(days=1)
                return p_date.strftime('%Y-%m-%d') 

            a = matches(previous_day(oldest))
            for match in a:
                dates.append({'date': oldest, 'match': match})
            

        dates.to_csv('data/dates.csv')






