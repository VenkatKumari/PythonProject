import json

data = {}
data['people'] = []
data['people'].append\
        ({
    'name': 'Sahana ',
    'nationality': 'India',
    'Degree': 'M.Sc(SE)'
})
data['people'].append\
        ({
    'name': 'Giorgi',
    'Nationality': 'Giorgia',
    'Degree': 'M.Sc(CS)'
})
data['people'].append\
        ({
    'name': 'VK',
    'Nationality': 'French',
    'Degree': 'M.Sc(SE)'
})

with open('data3.txt', 'w') as outfile:
    json.dump(data, outfile)