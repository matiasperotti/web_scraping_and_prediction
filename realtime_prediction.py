
# this function make the same that the function scratch, preprocessing the data and make the prediction to save it
# but not save info in matches.csv because is using data from the future e.g it does not know the winner


from datetime import date, datetime, timedelta
from one_function import matches
from info_function_realtime import get_info
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

def gmatches(date):

    match = pd.read_csv('./data/predictions.csv', index_col=0)
    a = matches(date)
    
    for matchh in a:


        if(matchh not in match['match'].values):


            info = get_info(matchh)

            #print('info', info)

            if((len(info[0]) != 0) & (len(info[1]) != 0)):

                match.loc[len(match)] = [date] + [matchh] + [info[0]] + [info[1]] + [0]

                names = info[0] + info[1]
                from fifa_function import statistics

                for name in names:
                    
                    #df = pd.read_csv('/home/ubuntu/futbol_scratch_-_prediction/data/players.csv', index_col=0)
                    df = pd.read_csv('./data/players.csv', index_col=0)
                    if(not df['name'].str.contains(name).any()):
                        
                        columns = ['name', 'Ball_Control', 'Dribbling', 'Marking', 'Slide_Tackle' ,'Stand_Tackle', 'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes' ,'Height', 'Weight', 'Age']

                        values = statistics(name)
                        
                        df.loc[len(df)] = [name] + values

                        #df.to_csv('/home/ubuntu/futbol_scratch_-_prediction/data/players.csv')
                        df.to_csv('./data/players.csv')
                        match.to_csv('./data/predictions.csv')
        
    print(match.head())
    return match

def predictions():
                        
    while 1 == 1:
        

        #tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        tomorrow = ''

        matches = gmatches(tomorrow)
        players = pd.read_csv('./data/players.csv')

        matches = matches.replace('None', np.nan)
        players = players.replace('None', np.nan)

        matches = matches.iloc[:, -3:]

        team1nones = 0
        team2nones = 0

        all_columns = [
            '1Ball_Control', '1Dribbling', '1Marking', '1Slide_Tackle', '1Stand_Tackle',
            '1Aggression', '1Reactions', '1Att_Position', '1Interceptions', '1Vision',
            '1Short_Pass', '1Long_Pass', '1Acceleration', '1Stamina', '1Strength',
            '1Balance', '1Sprint_Speed', '1Agility', '1Jumping', '1Heading',
            '1Shot_Power', '1Finishing', '1Long_Shots', '1Curve', '1FK_Acc', '1Penalties',
            '1Volleys', '1GK_Positioning', '1GK_Diving', '1GK_Handling', '1GK_Kicking',
            '1GK_Reflexes', '1Height', '1Weight', '1Age',
            '1Quantity',
            '2Ball_Control', '2Dribbling', '2Marking', '2Slide_Tackle', '2Stand_Tackle',
            '2Aggression', '2Reactions', '2Att_Position', '2Interceptions', '2Vision',
            '2Short_Pass', '2Long_Pass', '2Acceleration', '2Stamina', '2Strength',
            '2Balance', '2Sprint_Speed', '2Agility', '2Jumping', '2Heading',
            '2Shot_Power', '2Finishing', '2Long_Shots', '2Curve', '2FK_Acc', '2Penalties',
            '2Volleys', '2GK_Positioning', '2GK_Diving', '2GK_Handling', '2GK_Kicking',
            '2GK_Reflexes', '2Height', '2Weight', '2Age',
            '2Quantity'
        ]

        df = pd.DataFrame(columns = all_columns)


        def meanlist(listt):
            if len(listt) == 0:
                return 0
            else:
                summ = sum(listt)
                mean = summ / len(listt)
                return round(mean, 1)


        for i in range(matches.shape[0]):

            columns = players.columns[-35:]
            column_values = {column: [] for column in columns}

            for player in eval(matches['team1'].iloc[i]):

                for column in columns:
                        
                    stats = players[players['name'] == player]

                    aaa = stats[column]


                    for index, value in aaa.iteritems():
                        value = pd.to_numeric(value, errors='coerce')
                        if not pd.isnull(value):
                            column_values[column].append(value)
            
            aaa1 = []
            for column in columns:
                aa = meanlist(column_values[column])
                aaa1.append(aa)
            quantity1 = len(column_values['Age'])

            ######################################f

            for player in eval(matches['team2'].iloc[i]):

                for column in columns:
                        
                    stats = players[players['name'] == player]

                    aaa = stats[column]


                    for index, value in aaa.iteritems():
                        value = pd.to_numeric(value, errors='coerce')
                        if not pd.isnull(value):
                            column_values[column].append(value)
            
            aaa2 = []
            for column in columns:
                aa = meanlist(column_values[column])
                aaa2.append(aa)
            quantity2 = len(column_values['Age'])


            v = []
            v = v + aaa1
            v.append(quantity1)
            v = v + aaa2
            v.append(quantity2)

            df = df.append(pd.Series(v, index=all_columns), ignore_index=True)

            #print(df.head())

            


            ### pegar la columna de 'match' que seria matchh

            #####3################################


            df2 = pd.DataFrame()

            df2['ball_control'] = df['1Ball_Control'] - df['2Ball_Control']
            df2['Dribbling'] = df['1Dribbling'] - df['2Dribbling']
            df2['Marking'] = df['1Marking'] - df['2Marking']
            df2['Slide_Tackle'] = df['1Slide_Tackle'] - df['2Slide_Tackle']
            df2['Stand_Tackle'] = df['1Stand_Tackle'] - df['2Stand_Tackle']
            df2['Aggression'] = df['1Aggression'] - df['2Aggression']
            df2['Reactions'] = df['1Reactions'] - df['2Reactions']
            df2['Att_Position'] = df['1Att_Position'] - df['2Att_Position']
            df2['Interceptions'] = df['1Interceptions'] - df['2Interceptions']
            df2['Vision'] = df['1Vision'] - df['2Vision']
            df2['Short_Pass'] = df['1Short_Pass'] - df['2Short_Pass']
            df2['Long_Pass'] = df['1Long_Pass'] - df['2Long_Pass']
            df2['Acceleration'] = df['1Acceleration'] - df['2Acceleration']
            df2['Stamina'] = df['1Stamina'] - df['2Stamina']
            df2['Strength'] = df['1Strength'] - df['2Strength']
            df2['Balance'] = df['1Balance'] - df['2Balance']
            df2['Sprint_Speed'] = df['1Sprint_Speed'] - df['2Sprint_Speed']
            df2['Agility'] = df['1Agility'] - df['2Agility']
            df2['Jumping'] = df['1Jumping'] - df['2Jumping']
            df2['Heading'] = df['1Heading'] - df['2Heading']
            df2['Shot_Power'] = df['1Shot_Power'] - df['2Shot_Power']
            df2['Finishing'] = df['1Finishing'] - df['2Finishing']
            df2['Long_Shots'] = df['1Long_Shots'] - df['2Long_Shots']
            df2['Curve'] = df['1Curve'] - df['2Curve']
            df2['FK_Acc'] = df['1FK_Acc'] - df['2FK_Acc']
            df2['Penalties'] = df['1Penalties'] - df['2Penalties']
            df2['Volleys'] = df['1Volleys'] - df['2Volleys']
            df2['GK_Positioning'] = df['1GK_Positioning'] - df['2GK_Positioning']
            df2['GK_Diving'] = df['1GK_Diving'] - df['2GK_Diving']
            df2['GK_Handling'] = df['1GK_Handling'] - df['2GK_Handling']
            df2['GK_Kicking'] = df['1GK_Kicking'] - df['2GK_Kicking']
            df2['GK_Reflexes'] = df['1GK_Reflexes'] - df['2GK_Reflexes']
            df2['Height'] = df['1Height'] - df['2Height']
            df2['Weight'] = df['1Weight'] - df['2Weight']
            df2['Age'] = df['1Age'] - df['2Age']
            df2['1Quantity'] = df['1Quantity']
            df2['2Quantity'] = df['2Quantity']




            columns = ['ball_control', 'Dribbling', 'Marking', 'Slide_Tackle', 'Stand_Tackle',
                'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision',
                'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength',
                'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading',
                'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties',
                'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking',
                'GK_Reflexes', 'Height', 'Weight', 'Age']



            scaler = StandardScaler()

            df2[columns] = scaler.fit_transform(df2[columns])

            df2 = round(df2, 1)

            #matches['prediction'].iloc[i] = 2
            matches.loc[i, 'prediction'] = 2

            matches.head()

        """
        datatable = df2['ball_control', 'Dribbling', 'Marking', 'Slide_Tackle', 'Stand_Tackle',
            'Aggression', 'Reactions', 'Att_Position', 'Interceptions', 'Vision',
            'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength',
            'Balance', 'Sprint_Speed', 'Agility', 'Jumping', 'Heading',
            'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'FK_Acc', 'Penalties',
            'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Handling', 'GK_Kicking',
            'GK_Reflexes', 'Height', 'Weight', 'Age', '1Quantity', '2Quantity']
        """



        #model = tf.keras.models.load_model('./autokeras_model')

        # hay que hacer la prediccion

        df2.head()
        #datatable.head()

        #match.to_csv('/home/ubuntu/futbol_scratch_-_prediction/data/predictions.csv') 
        #match.to_csv('./data/predictions.csv') 

        # hay que cambiar nombres de muchas variables que en los distintos scrips tenian el mismo nombre


### como entra la info del partido?

### no tomando todos los objetos de partidos, por algun motivo solo esta agarrando los primeros 4 (del dia en que hago esto)


predictions()

