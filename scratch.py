

def scratch():          ## esta funcion recolecta solo links de matches en el archivo matches.csv
                        ## en el caso de que hayan matches empieza a buscar en fechas anteriores a la del match mas viejo
    from datetime import date, datetime, timedelta
    from one_function import matches
    from info_function import get_info
    import pandas as pd

    last_date = ''

    while 1 == 1:


        try:

            match = pd.read_csv('data/matches.csv')

            oldest = match['date'].min()
            oldest = oldest.strftime('%Y-%m-%d')

            if(last_date != ''):
                oldest = last_date

            if(oldest not in match['date']):

                def previous_day(date):# 
                    date = datetime.strptime(date, '%Y-%m-%d')
                    p_date = date - timedelta(days=1)
                    return p_date.strftime('%Y-%m-%d') 

                a = matches(previous_day(oldest))

                for matchh in a:
                    info = get_info(matchh)

                    match.append({'date': oldest, 'match': matchh, 'points': info[0], 'team1': info[1], 'team2': info[2]}, ignore_index=True)

                    #
                    names = info[1] + info[2]
                    from fifa_function import statistics

                    for name in names:

                        df = pd.read_csv('data/players.csv')
                        if(name not in df['name']):

                            columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                            values = statistics(name)

                            df = df.append(pd.Series([name] + values, index=columns), ignore_index=True)

                            df.to_csv('data/players.csv')
                    #

            last_date = previous_day(oldest)

            match.to_csv('data/matches.csv')



        except pd.errors.EmptyDataError:

            a = matches('')
            # quizas aca arriba hay un problema porque daria los datos de hoy y se necesitan como maximo de ayer
            for matchh in a:
                datte = date.today().strftime('%Y-%m-%d')
                info = get_info(matchh)

                match = pd.DataFrame(columns=['date', 'match', 'points', 'team1', 'team2'])
                match.append({'date': datte, 'match': matchh, 'points': info[0], 'team1': info[1], 'team2': info[2]}, ignore_index=True)

                #
                names = info[1] + info[2]
                from fifa_function import statistics

                for name in names:

                    df = pd.read_csv('data/players.csv')
                    if(name not in df['name']):

                        columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                        values = statistics(name)

                        df = df.append(pd.Series([name] + values, index=columns), ignore_index=True)

                        df.to_csv('data/players.csv')

                match.to_csv('data/matches.csv')

        

# falta una ultima (pero quizas en el feature engineering) que junte las estadisticas de todos los jugadores 
# de ese se podrian hacer varias versiones para probar distintos features calculados



scratch()



# tiene que empezar a buscar si o si desde ayer
# los matches con distinto formato estan rompiendo todo

# empezar a buscar match desde el dia de la ultima fecha por si se pauso el programa y no junto todos los datos

