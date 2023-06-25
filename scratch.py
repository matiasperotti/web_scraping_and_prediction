

def scratch():          ## esta funcion recolecta solo links de matches en el archivo matches.csv
                        ## en el caso de que hayan matches empieza a buscar en fechas anteriores a la del match mas viejo
    from datetime import date, datetime, timedelta
    from one_function import matches
    from info_function import get_info
    import pandas as pd

    last_date = ''

    while 1 == 1:


        try:

            match = pd.read_csv('data/matches.csv', header=0)

            oldest = match['date'].min()
            oldest = datetime.strptime(oldest, '%Y-%m-%d')
            oldest = oldest.strftime('%Y-%m-%d')
            #oldest = oldest.strftime('%Y-%m-%d')

            if(last_date != ''):
                oldest = last_date

            if(oldest not in match['date'].values):

                def previous_day(date):# 
                    date = datetime.strptime(date, '%Y-%m-%d')
                    p_date = date - timedelta(days=1)
                    return p_date.strftime('%Y-%m-%d') 

                a = matches(previous_day(oldest))

                for matchh in a:

                    if(matchh not in match['match'].values):

                        info = get_info(matchh)
                        if(len(info[1]) != 0):

                            match = match.append({'date': oldest, 'match': matchh, 'points': info[0], 'team1': info[1], 'team2': info[2]}, ignore_index=True)

                            #
                            names = info[1] + info[2]
                            from fifa_function import statistics

                            for name in names:

                                df = pd.read_csv('data/players.csv', header=0)
                                if(not df['name'].str.contains(name).any()):


                                    columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                                    values = statistics(name)

                                    df = df.append(pd.Series([name] + values, index=columns), ignore_index=True)
                                    df = df[columns]#

                                    df.to_csv('data/players.csv')
                        #
                            matchcolumns = ['date', 'match', 'points', 'team1', 'team2']
                            match = match[matchcolumns]
                            match.to_csv('data/matches.csv') #######

            last_date = previous_day(oldest)




        except pd.errors.EmptyDataError:

            a = matches('')
            
            for matchh in a:

                today = date.today()
                datte = today - timedelta(days=1)
                datte = datte.strftime('%Y-%m-%d')

                info = get_info(matchh)
                if(len(info[1]) != 0):

                    match = pd.DataFrame(columns=['date', 'match', 'points', 'team1', 'team2'])
                    match = match.append({'date': datte, 'match': matchh, 'points': info[0], 'team1': info[1], 'team2': info[2]}, ignore_index=True)

                    #
                    names = info[1] + info[2]
                    from fifa_function import statistics

                    for name in names:
                        
                        df = pd.read_csv('data/players.csv', header=0)
                        if(not df['name'].str.contains(name).any()):

                            columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                            values = statistics(name)

                            df = df.append(pd.Series([name] + values, index=columns), ignore_index=True)
                            df = df[columns]#

                            df.to_csv('data/players.csv')

                    matchcolumns = ['date', 'match', 'points', 'team1', 'team2']
                    match = match[matchcolumns]
                    match.to_csv('data/matches.csv') ###

        

# falta una ultima (pero quizas en el feature engineering) que junte las estadisticas de todos los jugadores 
# de ese se podrian hacer varias versiones para probar distintos features calculados



scratch()

