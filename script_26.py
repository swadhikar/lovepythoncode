airlines_list = [
    'IndiGo (6E)',
    'Air India (AI)',
    'Emirates (EK)',
    'Etihad Airways (EY)',
    'Fly Dubai (FZ)',
    'KLM (KL)',
    'SpiceJet (SG)'
 ]

with open('airlines.txt', 'w') as file_desc:
 for airline_name in airlines_list:
     # Using print function writes to file
     print(airline_name, file=file_desc)
