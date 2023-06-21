

def matches():          ## esta funcion recolecta solo links de matches en el archivo matches.csv
                        ## en el caso de que hayan matches empieza a buscar en fechas anteriores a la del match mas viejo
    from datetime import date, datetime, timedelta
    from one_function import matches
    from info_function import get_info

    last_date = ''

    while 1 == 1:
    
        dates = pd.read_csv('data/dates.csv')
        
        if(dates.empty):
            a = matches('')
            # quizas aca arriba hay un problema porque daria los datos de hoy y se necesitan como maximo de ayer
            for match in a:
                datte = date.today().strftime('%Y-%m-%d')
                info = get_info(match)

                dates.append({'date': datte, 'match': match, 'points': info[0], 'team1': info[1], 'team2': info[2]})

                #
                names = info[0] + info[1]
                from fifa_function import statistics

                for name in names:

                    df = pd.read_csv('data/players.csv')
                    if(name not in df['name']):

                        columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                        values = statistics(name)

                        df = df.append(pd.Series([name] + values, index=df.columns), ignore_index=True)

                        df.to_csv('data/players.csv')
                #

        else: 

            oldest = dates['date'].min()
            oldest = oldest.strftime('%Y-%m-%d')

            if(last_date != ''):
                oldest = last_date

            if(oldest not in dates['date']):

                def previous_day(date):# 
                    date = datetime.strptime(date, '%Y-%m-%d')
                    p_date = date - timedelta(days=1)
                    return p_date.strftime('%Y-%m-%d') 

                a = matches(previous_day(oldest))

                for match in a:
                    info = get_info(match)

                    dates.append({'date': oldest, 'match': match, 'points': info[0], 'team1': info[1], 'team2': info[2]})

                    #
                    names = info[0] + info[1]
                    from fifa_function import statistics

                    for name in names:

                        df = pd.read_csv('data/players.csv')
                        if(name not in df['name']):

                            columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                            values = statistics(name)

                            df = df.append(pd.Series([name] + values, index=df.columns), ignore_index=True)

                            df.to_csv('data/players.csv')
                    #

            last_date = previous_day(oldest)

        dates.to_csv('data/dates.csv')


# falta una ultima (pero quizas en el feature engineering) que junte las estadisticas de todos los jugadores 
# de ese se podrian hacer varias versiones para probar distintos features calculados






