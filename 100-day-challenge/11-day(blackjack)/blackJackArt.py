logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
     

cards_pattern = lambda v: [f'''
     ______
    |{v} /\  |
    | /  \ |
    |(____)|
    |  ||  |
    |_____♠|
''', f'''
     ______
    |{v} /\  |
    | /  \ |
    | \  / |
    |  \/  |
    |_____♦|
''', f'''
     ______
    |{v} __  |
    | (  ) |
    |(____)|
    |  ||  |
    |_____♣|
''', f'''
     ______
    |{v}_  _ |
    |( \/ )|
    | \  / |
    |  \/  |
    |_____♥|
''']

hidden_card = '''
     ______
    |X     |
    |  XX  |
    |  XX  |
    |  XX  |
    |_____X|
'''
