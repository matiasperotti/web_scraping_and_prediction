

def scratch():          ## esta funcion recolecta solo links de matches en el archivo matches.csv
                        ## en el caso de que hayan matches empieza a buscar en fechas anteriores a la del match mas viejo
    from datetime import date, datetime, timedelta
    from one_function import matches
    from info_function import get_info
    import pandas as pd
    import numpy as np

    
    
    while 1 == 1:
        
        def previous_day(date):
            date = datetime.strptime(date, '%Y-%m-%d')
            p_date = date - timedelta(days=1)
            return p_date.strftime('%Y-%m-%d')

        def next_day(date):
            date = datetime.strptime(date, '%Y-%m-%d')
            p_date = date + timedelta(days=1)
            return p_date.strftime('%Y-%m-%d')

        try:

            last = ''

            match = pd.read_csv('/home/ubuntu/futbol_scratch_-_prediction/data/matches.csv', index_col=0)

            oldest = match['date'].max()# pongo oldest pero voy a estar usando fechas mas recientes

            oldest = datetime.strptime(oldest, '%Y-%m-%d')
            oldest = oldest.strftime('%Y-%m-%d')

            yyy = (datetime.now() - timedelta(days=2))
            yyy = yyy.strftime('%Y-%m-%d')

            if(oldest < yyy):
                oldest = next_day(oldest)
                # esto va a permitir buscar fechas mas recientes pero solo si el dia aun no ocurre
                # en caso que no haya dias para buscar informacion el programa va a leer hasta que se cumpla la consigna


            if(oldest not in match['date'].values):
                a = matches(oldest)
                
                for matchh in a:
                    
                    if(matchh not in match['match'].values):
                        info = get_info(matchh)
                                 
                        if(len(info[1]) != 0):
                                                    
                            match.loc[len(match)] = [oldest] + [matchh] + [info[0]] + [info[1]] + [info[2]]

                            names = info[1] + info[2]
                            from fifa_function import statistics

                            for name in names:
                                
                                df = pd.read_csv('/home/ubuntu/futbol_scratch_-_prediction/data/players.csv', index_col=0)
                                if(not df['name'].str.contains(name).any()):
                                    
                                    columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                                    values = statistics(name)
                                    
                                    df.loc[len(df)] = [name] + values
                    
                                    df.to_csv('/home/ubuntu/futbol_scratch_-_prediction/data/players.csv')
                    
                            match.to_csv('/home/ubuntu/futbol_scratch_-_prediction/data/matches.csv') 
                            
            last = oldest


        except pd.errors.EmptyDataError:

            a = matches('')
            
            for matchh in a:

                today = date.today()
                datte = today - timedelta(days=1)
                datte = datte.strftime('%Y-%m-%d')
                
                info = get_info(matchh)
                if(len(info[1]) != 0):
            
                    match = pd.DataFrame(columns=['date', 'match', 'points', 'team1', 'team2'])
                    roww = pd.Series({'date': datte, 'match': matchh, 'points': info[0], 'team1': info[1], 'team2': info[2]})
                    match = match.append(roww, ignore_index=True)
                    

                    #
                    names = info[1] + info[2]
                    from fifa_function import statistics

                    for name in names:
                        
                        df = pd.read_csv('/home/ubuntu/futbol_scratch_-_prediction/data/players.csv', index_col=0)
                        if(not df['name'].str.contains(name).any()):

                            columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                            values = statistics(name)
                            
                            df.loc[len(df)] = [name] + values
                                         
                            df.to_csv('/home/ubuntu/futbol_scratch_-_prediction/data/players.csv')

                    matchcolumns = ['date', 'match', 'points', 'team1', 'team2']
                    match = match[matchcolumns]
                    
                    match.to_csv('/home/ubuntu/futbol_scratch_-_prediction/data/matches.csv')
        


scratch()

