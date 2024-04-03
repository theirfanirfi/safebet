#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random as rd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

import joblib 


# In[95]:


# # Save the model as a pickle in a file 
# joblib.dump(model, './machinelearningmodel/ml.pkl') 
  
# Load the model from the file 
ml = joblib.load('./machinelearningmodel/ml.pkl')


# In[96]:





# In[2]:


players = "Novak Djokovic,Daniil Medvedev,Rafael Nadal,Stefanos Tsitsipas,Dominic Thiem,Alexander Zverev,Andrey Rublev,Matteo Berrettini,Roberto Bautista Agut,Diego Schwartzman,Pablo Carreno Busta,David Goffin,Denis Shapovalov,Casper Ruud,Gael Monfils,Hubert Hurkacz,Milos Raonic,Cristian Garin,Grigor Dimitrov,Felix Auger Aliassime,Alex de Minaur,Jannik Sinner,Aslan Karatsev,Daniel Evans,Lorenzo Sonego,Karen Khachanov,Stan Wawrinka,Fabio Fognini,Nikoloz Basilashvili,Ugo Humbert,Reilly Opelka,John Isner,Borna Coric,Alejandro Davidovich Fokina,Taylor Fritz,Albert Ramos Vinolas,Alexander Bublik,Dusan Lajovic,Cameron Norrie,Adrian Mannarino,John Millman,Filip Krajinovic,Jan Lennard Struff,Benoit Paire,Miomir Kecmanovic,Federico Delbonis,Marton Fucsovics,Tommy Paul,Lloyd Harris,Sebastian Korda,Dominik Koepfer,Richard Gasquet,Laslo Djere,Yoshihito Nishioka,Kei Nishikori,Jeremy Chardy,Lorenzo Musetti,Guido Pella,Feliciano Lopez,Frances Tiafoe,Vasek Pospisil,Alexei Popyrin,Tennys Sandgren,Jaume Munar,Pablo Andujar,Steve Johnson,Jiri Vesely,Emil Ruusuvuori,Marcos Giron,Egor Gerasimov,Kyle Edmund,Carlos Alcaraz,Soonwoo Kwon,Jordan Thompson,Gianluca Mager,Thiago Monteiro,Ricardas Berankis,Pablo Cuevas,Marco Cecchinato,Pierre Hugues Herbert,Stefano Travaglia,Norbert Gombos,Ilya Ivashka,James Duckworth,Radu Albot,Corentin Moutet,Lucas Pouille,Facundo Bagnis,Salvatore Caruso,Mikael Ymer,Yannick Hanfmann,Roberto Carballes Baena,Kevin Anderson,Fernando Verdasco,Federico Coria,Taro Daniel,Mikhail Kukushkin,Pedro Martinez,Yuichi Sugita,Pedro Sousa,Joao Sousa,Dennis Novak,Daniel Elahi Galan,Kamil Majchrzak,Attila Balazs,Mackenzie McDonald,Yasutaka Uchiyama,Francisco Cerundolo,Denis Kudla,Arthur Rinderknech,Tallon Griekspoor,Benjamin Bonzi,Bernabe Zapata Miralles,Thiago Seyboth Wild,Andy Murray,Damir Dzumhur,Jozef Kovalik,Juan Ignacio Londero,Hugo Dellien,Gregoire Barrere,Juan Pablo Varillas,Christopher Oconnell,Peter Gojowczyk,Carlos Taberner,Jurij Rodionov,Henri Laaksonen,Brandon Nakashima,Botic van de Zandschulp,Evgeny Donskoy,Federico Gaio,J J Wolf,Juan Manuel Cerundolo,Sumit Nagal,Liam Broady,Nikola Milojevic,Prajnesh Gunneswaran,Jenson Brooksby,Maxime Cressy,Antoine Hoang,Marc Polmans,Marc Andrea Huesler,Oscar Otte,Illya Marchenko,Roman Safiullin,Blaz Rola,Jason Jung,Hugo Gaston,Alessandro Giannessi,Mohamed Safwat,Daniel Altmaier,Enzo Couacaud,Emilio Gomez,Alejandro Tabilo,Bradley Klahn,Frederico Ferreira Silva,Sebastian Ofner,Michael Mmoh,Zhizhen Zhang,Thanasi Kokkinakis,Alex Molcan,Hyeon Chung,Elias Ymer,Kimmer Coppejans,Ernesto Escobedo,Bjorn Fratangelo,Dmitry Popko,Denis Istomin,Ernests Gulbis,Cem Ilkel,Steven Diez,Roberto Marcora,Mitchell Krueger,Lukas Rosol,Alex Bolt,Alexandre Muller,Maximilian Marterer,Andrea Collarini,Guido Andreozzi,Mathias Bourgue,Marco Trungelliti,Renzo Olivo,Christopher Eubanks,Aleksandar Vukic,Robin Haase,Ramkumar Ramanathan,Lorenzo Giustino,Felipe Meligeni Alves,Daniel Masur,Quentin Halys,Zizou Bergs,Marius Copil,Thai Son Kwiatkowski,Bernard Tomic,Juan Pablo Ficovich,Tatsuma Ito,Jack Sock,Maxime Janvier,Constant Lestienne,Holger Rune,Tomas Barrios Vera,Jay Clarke,Brayden Schnur,Borna Gojo,Zdenek Kolar,Altug Celikbilek,Andrea Pellegrino,Joao Domingues,Roberto Cid Subervi,Dimitar Kuzmanov,Mats Moraing,Ulises Blanch,Matthias Bachinger,Facundo Mena,Vit Kopriva,Gastao Elias,Tristan Lamasine,Nicola Kuhn,Yosuke Watanuki,Teymuraz Gabashvili,Chun Hsin Tseng,Hiroki Moriya,Gian Marco Moroni,Hugo Grenier,Zhe Li,Jason Kubler,Nuno Borges,Andrea Arnaboldi,Pedja Krstin,Duje Ajdukovic,Mischa Zverev,Pedro Cachin,Evgeny Karlovskiy,Max Purcell,Noah Rubin,Akira Santillan,Christian Harrison,Elliot Benchetrit,Dominic Stricker,Yan Bai,Goncalo Oliveira,Mirza Basic,Evan Furness,Nino Serdarusic,Manuel Guinard,Nicolas Mejia,Evgenii Tiurnev,Nicolas Jarry,Jack Draper,Alexander Ritschard,Pedro Sakamoto,JiSung Nam,Rudolf Molleker,Alexey Vatutin,Lucas Miedler,Sasi Kumar Mukund,Darian King,Duck Hee Lee,Geoffrey Blancaneaux,Orlando Luz,Johannes Haerteis,Stefano Napolitano,Javier Barranco Cosano,Shuichi Sekiguchi,Adrian Andreev,Jelle Sels,Donald Young,Lucas Catarina,Kaichi Uchida,Stefan Kozlov,John Patrick Smith,Alexander Erler,Matija Pecotic,Andrea Vavassori,Julian Ocleppo,Petros Chrysochos,Dayne Kelly,Oriol Roca Batalla,Corentin Denolly,Jeremy Jahn,Jan Choinski,Hernan Casanova,Viktor Durasovic,Ryan Peniston,Skander Mansouri,Sekou Bangoura,Matteo Martineau,Antoine Escoffier,Ivan Nedelko,Yunseong Chung,Facundo Diaz Acosta,Edan Leshem,Miljan Zekic,Ergi Kirkin,Laurent Lokoli,Luke Saville,Elmar Ejupovic,Alex Rybakov,Andrey Kuznetsov,Zsombor Piros,Aldin Setkic,Peter Heller,Alexis Galarneau,Emilio Nava,Karim Mohamed Maamoun,Harold Mayot,Filip Peliwo,Paul Jubb,Collin Altamirano,Fajing Sun,Renta Tokuda,Jacopo Berrettini,Louis Wessels,Alvaro Lopez San Martin,Aidan McHugh,Ivan Gakhov,Martin Cuevas,Yusuke Takahashi,Calvin Hemery,Blake Mott,Sho Shimabukuro,Nicolas Kicker,Riccardo Balzerani,Strong Kirchheimer,Antoine Bellier,Maxime Chazal,Gage Brymer,Roy Smith,Sidharth Rawat,Inigo Cervantes Huegun,Gonzalo Lama,Nicolas Alvarez Varona,Mateus Alves,Sanjar Fayziev,Anton Matusevich,Adam Moundir,Alexandar Lazarov,Ryan Harrison,Dragos Nicolae Madaras,Johan Sebastien Tatlot,Thomas Fancutt,Wilson Leite,Yanki Erel,Daniel Dutra da Silva,Juan Pablo Paz,Simon Carr,Juan Ignacio Galarza,Jonathan Mridha,Alexander Donski,Maximilian Neuchrist,Kenny De Schepper,Aleksandre Metreveli,Federico Zeballos,Marvin Moeller,Mate Valkusz,Tomas Lipovsek Puches,Alibek Kachmazov,Naoki Nakagawa,Marsel Ilhan,Leandro Riedi,Ryan Nijboer,Patrick Kypson,Benjamin Sigouin,Mark Whitehouse,Jakub Paul,Juan Sebastian Gomez,Matthew Christopher Romios,Filip Bergevi,Arjun Kadhe,Karl Friberg,Sebastian Prechtel,Jie Cui,Zachary Svajda,Boris Pokotilov,Sandro Kopp,Wishaya Trongcharoenchaikul,Govind Nanda,Niki Kaliyanda Poonacha,Kirill Kivattsev,Rinky Hijikata,Jaimee Floyd Angele,Juan Bautista Otegui,Connor Farren,Thiemo de Bakker,Guy Den Heijer,David Perez Sanz,Duje Kekez,Sarp Agabigun,Toshihide Matsui,Petr Michnev,Nicolas Barrientos,George Loffhagen,Louis Tessa,Javier Marti,Jules Marie,Ajeet Rai,Gabriel Donev,Toby Martin,Matteo Donati,Manuel Sanchez,Taha Baadi,Xin Gao,Garrett Johns,Cannon Kingsley,Hiroyasu Ehara,Albano Olivetti,Hugo Schott,Mikalai Haliak,Tristan Boyer,Koray Kirci,Adrian Bodmer,Blake Ellis,Lucas Renard,Raphael Baltensperger,Domagoj Biljesko,Yibing Wu,Rigele Te,Alastair Gray,Andrew Fenty,Ryan James Storrie,Jose Pereira,Aleksei Khomich,Boris Fassbender,Congsup Congcar,Goncalo Falcao,Gerald Melzer,Daniel Cox,Ivan Sergeyev,Kiranpal Pannu,Fernando Yamacita,Pol Wattanakul,John Hallquist Lithen,Karue Sell,Alexander Klintcharov,Suraj R Prabodh,Admir Kalender,Mert Alkaya,Ranjeet Virali Murugesan,Luciano Doria,Preston Brown,Zhao Zhao,Karl Poling,William Blumberg,Alan Fernando Rubio Fierros,Tom Schonenberg,Lukas Klein,Aaron Addison,Adam Neff,Alberto Barroso Campos,Alejandro Moro Canas,Aleksandar Kovacevic,Alexander Blockx,Alexander Shevchenko,Alexis Gautier,Andres Martin,Andrey Chepelev,Aoran Wang,Arslanbek Aitkulov,Arthur Fils,Aziz Dougaz,Beibit Zhukayev,Ben Shelton,Benjamin Hassan,Benjamin Ignacio Torres Fernandez,Brandon Holt,Brandon Walkin,Bruno Kuzuhara,Camilo Ugo Carabelli,Carlos Gimeno Valero,Christopher Rungkat,Dalibor Svrcina,Damien Wenger,Daniel Antonio Nunez,Daniel Cukierman,Daniel Merida Aguilar,Daniel Rincon,David Pel,Denis Yevseyev,Dino Prizmic,Duarte Vale,Eduard Esteve Lobato,Edward Winter,Evan Zhu,Federico Agustin Gomez,Fernando Romboli,Filip Cristian Jianu,Filip Misolic,Finn Reynolds,Flavio Cobolli,Francesco Forti,Francesco Maestrelli,Francesco Passaro,Franco Agamenone,Gabriel Diallo,Gauthier Onclin,Gianmarco Ferrari,Gijs Brouwer,Gilles Arnaud Bailly,Giovanni Fonio,Giovanni Oradini,Giulio Zeppieri,Gonzalo Villanueva,Grigoriy Lomakin,Gustavo Heide,Hady Habib,Hamad Medjedovic,Henri Squire,Hudson Rivera,Inaki Montes De La Torre,Ivan Denisov,Jaden Weekes,Jakub Mensik,Jakub Wojcik,Jannik Maute,Jea Moon Lee,Jerome Kym,Jesper de Jong,Jiri Lehecka,Jorge Plans,Joris De Loore,Juan Carlos Aguilar,Juncheng Shang,Kacper Zuk,Kaito Uesugi,Keegan Smith,Leo Borg,Liam Draxl,Luca Nardi,Luca Van Assche,Lucas Gerch,Luis Carlos Alvarez,Lukas Neumayer,Manish Sureshkumar,Marcelo Zormann Da Silva,Marek Gengel,Marko Topo,Martin Damm 1,Martin Landaluce,Mateusz Terczynski,Matheus Pucinelli De Almeida,Matias Franco Descotte,Mats Rosenkranz,Matteo Arnaldi,Max Alcala Gurri,Max Hans Rehberg,Maxim Zhukov,Mayeul Darras,Mehdi Benchakroun,Menelaos Efstathiou,Michael Geerts,Michail Pervolarakis,Mili Poljicak,Moerani Bouzige,Moez Echargui,Mubarak Shannan Zayid,Nerman Fatic,Nicholas David Ionel,Nick Chappell,Nikolas Sanchez Izquierdo,Olukayode Alafia Damina Ayeni,Omar Jasika,Otto Virtanen,Pavel Kotov,Pedro Araujo,Petr Nesterov,Pruchya Isarow,Raul Brancaccio,Riccardo Bonadio,Rio Noguchi,Rodrigo Pacheco Mendez,Rubin Statham,Ryota Tanuma,Santiago Fa Rodriguez Taverna,Sascha Gueymard Wayenburg,Scott Jones,Sebastian Baez,Sebastian Fanselow,Sebastian Sec,Seong Chan Hong,Shintaro Imai,Shintaro Mochizuki,Simon Freund,Thiago Agustin Tirante,Timo Legout,Titouan Droguet,Tomas Machac,Tomas Martin Etcheverry,Tung Lin Wu,Ugo Blanchet,Valentin Vacherot,Victor Lilov,Vishnu Vardhan,Vitaliy Sachko,Yan Bondarevskiy,Yaroslav Demin,Yshai Oliel,Yuki Mochizuki,Yuta Shimizu,Abdullah Shelbayh,Arthur Cazaux,Fabian Marozsan,Alex Michelsen,Luciano Darderi,Mariano Navone,Francisco Comesana,Terence Atmane,James McCabe"


# In[3]:


players_arr = players.split(',')


# In[8]:


players_df = pd.DataFrame(columns=['players'], data=players_arr)


# In[11]:


# Initialize LabelEncoder
label_encoder = LabelEncoder()


# In[14]:


players_df['players_encoded'] = label_encoder.fit_transform(players_df['players'])


# In[16]:


players_df.values


# In[17]:


players_list = []
for player in players_df.values:
    players_list.append({
        "id": player[1],
        "name": player[0]
    })


# In[19]:


tournments = "Acapulco,Adelaide,Antwerp,Nur-Sultan,Atlanta,Atp Cup,Tour Finals,Auckland,Australian Open,Barcelona,Basel,Bastad,Beijing,Belgrade,Belgrade 2,Brisbane,Buenos Aires,Chengdu,Cincinnati Masters,Cordoba,Dallas,Delray Beach,Doha,Dubai,Eastbourne,Estoril,Geneva,Gstaad,Halle,Hamburg,Hong Kong,Houston,Indian Wells Masters,Kitzbuhel,Laver Cup,Queens Club,Los Cabos,Lyon,Madrid Masters,Mallorca,Marrakech,Marseille,Metz,Miami Masters,Monte Carlo Masters,Montpellier,Canada Masters,Moscow,Munich,Newport,Paris Masters,Pune,Rio de Janeiro,Roland Garros,Rome Masters,Rotterdam,San Diego,Santiago,Shanghai Masters,s Hertogenbosch,Stockholm,St Petersburg,St. Petersburg,Stuttgart,Sydney,Tel Aviv,Tokyo,Tokyo Outdoor,Umag,Us Open,US Open,Vienna,Washington,Wimbledon,Winston-Salem,Zhuhai"


# In[97]:


players_list


# In[20]:


tournments_arr = tournments.split(',')


# In[21]:


tournments_df = pd.DataFrame(columns=['tournments'], data=tournments_arr)


# In[25]:


tournments_df['tournments'] = tournments_df['tournments'].unique()


# In[28]:


tournments_df['tournments_econded'] = label_encoder.fit_transform(tournments_df['tournments'])


# In[30]:


tournments_list = []
for tournment in tournments_df.values:
    tournments_list.append({
        "id": tournment[1],
        "name": tournment[0]
    })


# In[32]:


rounds = ['F','SF','QF','R16','R32','R64','R128','RR']


# In[33]:


rounds_df = pd.DataFrame(columns=['rounds'], data=rounds)


# In[35]:


rounds_df['rounds_econded'] = label_encoder.fit_transform(rounds_df['rounds'])


# In[37]:


rounds_list = []
for rond in rounds_df.values:
    rounds_list.append({
        "id": rond[1],
        "name": rond[0]
    })


# In[38]:


rounds_list


# In[39]:


player1_encoded = []
for i in players_list:
    player1_encoded.append(i['id'])


# In[50]:


player2_encoded = []
for i in range(0, len(player1_encoded)):
    r = rd.randint(0, len(player1_encoded)-1)
    player2_encoded.append(player1_encoded[r])


# In[53]:


tournments_ids = []
for i in tournments_list:
    tournments_ids.append(i['id'])


# In[55]:


tournments_encoded = []
for i in range(0, len(player1_encoded)):
    r = rd.randint(0, len(tournments_ids)-1)
    tournments_encoded.append(tournments_ids[r])


# In[58]:


rounds_ids = []
for i in rounds_list:
    rounds_ids.append(i['id'])


# In[59]:


rounds_ids


# In[60]:


rounds_encoded = []
for i in range(0, len(player1_encoded)):
    r = rd.randint(0, len(rounds_ids)-1)
    rounds_encoded.append(rounds_ids[r])


# In[62]:


len(rounds_encoded)


# In[63]:


win_prediction = []
for i in range(0, len(player1_encoded)):
    r = rd.randint(0, 1)
    win_prediction.append(r)


# In[65]:


len(win_prediction)


# In[66]:


data = {
    'player1': player1_encoded,
    'player2': player2_encoded,
    'tournments': tournments_encoded,
    'rounds': rounds_encoded,
    'win_prediction': win_prediction  # 1 indicates player1 won, 0 indicates player2 won
}


# In[68]:


# df = pd.DataFrame(data)


# # In[70]:


# X = df[['player1', 'player2', 'tournments','rounds']].values


# # In[71]:


# y = df['win_prediction'].values


# # In[73]:


# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Initialize and train the neural network model
# model = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', random_state=42)
# model.fit(X_train, y_train)


# # In[74]:


# # Make predictions
# predictions = model.predict(X_test)

# # Evaluate model performance
# accuracy = accuracy_score(y_test, predictions)
# print("Accuracy:", accuracy)


# In[93]:


def predict(player1: str, player2: str, tournment: str, roundd: str):
    player1_id = None
    player2_id = None
    tournment_id = None
    round_id = None
    
    for player in players_list:
        if player['name'] == player1:
            player1_id = player['id']
        
        if player['name'] == player2:
            player2_id = player['id']
            
    for tor in tournments_list:
        if tor['name'] == tournment:
            tournment_id = tor['id']
    
    for rnd in rounds_list:
        if rnd['name'] == roundd:
            round_id = rnd['id']
    
    
    return ml.predict([[player1_id, player2_id, tournment_id, round_id]])[0]
        


# In[94]:


# predict("Daniil Medvedev","Stefanos Tsitsipas","Metz","SF")


# # In[88]:


# if predict("Daniil Medvedev","Stefanos Tsitsipas","Metz","SF")[0] == 0:
#     print("Player 1 wins")
# else:
#     print("Player 2 wins")


# In[89]:


import pickle


# In[90]:


# Save the trained model as a pickle string. 
# saved_model = pickle.dumps(model) 


# In[91]:





# In[ ]:




