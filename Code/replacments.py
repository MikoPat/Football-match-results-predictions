
def get_replacement(club_name):

    replacments_club_names = {
        'Arsenal' : 'Arsenal',
        'Aston Villa' : 'Aston Villa',
        'Bournemouth' : 'Bournemouth',
        'Brentford' : 'Brentford',
        'Brighton' : 'Brighton',
        'Burnley' : 'Burnley',
        'Chelsea' : 'Chelsea',
        'Crystal Palace' : 'Crystal Palace',
        'Everton' : 'Everton',
        'Fulham' : 'Fulham',
        'Liverpool' : 'Liverpool',
        'Luton Town' : 'Luton',
        'Manchester City' : 'Man City',
        'Manchester Utd' : 'Man United',
        'Newcastle Utd' : 'Newcastle',
        "Nott'ham Forest" : 'Forest',
        'Sheffield Utd ' : 'Sheffield United',
        'Tottenham' : 'Tottenham',
        'West Ham' : 'West Ham',
        'Wolves' : 'Wolves',
        'Leicester' : 'Leicester',
        'Leeds' : 'Leeds',
        'Southampton' : 'Southampton',
        'Watford' : 'Watford',
        'Norwich' : 'Norwich',
        'West Brom' : 'West Brom',
        'Stoke' : 'Stoke',
        'Swansea' : 'Swansea',
        'Cardiff' : 'Cardiff',
        'Huddersfield' : 'Huddersfield'
    }

    return replacments_club_names.get(club_name, club_name)