#Eva D.
#P1. 11/29/24

#Init
import random

#Global Variables (all set to 0)
pokemon_level = 0
pokemon_name = "Charmander"
battle_wins = 0
battle_losses = 0

#ASCII Art for the stupid Pokemon
ascii_art = {
    "Charmander": """
     ⠀⠀⠀⠀ ⢀⣀⣠⠤⠤⠤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⠞⠉⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⠰⣦⠀⠀⠀⠀⠀⠀⢀⣼⢡⠾⣷⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⢷⠛⠀⠀⠀⠀⠀⠀⠀⠉⢸⡀⢸⣇⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⢸⠿⣿⢹⡀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣏⢉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠸⣦⡤⠞⠃⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡟⡈⠉⠀⠀⡀⠀⠀⠀⡀⠀⠀⠀⠀⢀⣠⠄⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣤⣀⠀⠀⠀
⠀⠀⠀⠸⣇⠙⢶⢤⣄⣁⣀⣀⣈⣁⣤⠤⠔⢾⣽⠁⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣄⡿⢿⣿⡆⠀⠀
⠀⠀⠀⠀⠙⠦⣜⠛⠳⣄⡀⢀⡼⠟⠛⠛⣶⠞⠁⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡇⠈⠁⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠒⠤⣭⡟⢒⣒⠒⣋⠁⠀⠀⢸⣅⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡞⠙⠀⠀⠀⣧⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⢩⡇⣠⠿⠛⠧⣄⠀⠀⠀⠀⠀⠉⠙⠲⢤⣀⡀⠀⣀⡀⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⢸⠀⠀
⢠⣴⣶⣾⠶⠚⠁⠀⠀⠀⢸⡼⠁⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⢻⣷⡶⠀⠀⡟⠀⠀⠀⠀⠀⣠⣿⣇⡀
⠈⠻⢿⡀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⢠⣿⣆⣨⣿⡆⠀⠀⢻⡄⠀⠀⠀⠀⠈⠛⣹⠁
⠀⠀⢾⠽⠒⠒⠒⠒⠒⠒⡇⠀⠀⠀⠀⠀⠀⠀⠀⠸⡍⠓⠒⢶⡒⠒⠒⠚⠉⠁⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⣠⠞⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣳⠶⡞⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⢠⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡷⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⣠⡾⠁⠀⣼⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⠋⠁⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠘⣧⣤⣤⣤⠴⠚⠉⠀⢀⣾⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⢀⡴⢫⡞⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠙⠶⣄⡀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⡇⢀⣀⡤⠖⢋⡴⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣆⡀⠀⠀⠀⠀⢀⣤⡤⠟⠓⠒⠲⠤⠤⢿⣄⠀⠀⠀⠀⠀⠀⣏⣩⡤⠴⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣴⣿⣍⣻⠀⠀⠀⠀⣨⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⠿⢵⡿⠽⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⡤⢤⡶⢿⡽⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣙⣳⣿⣛⣙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""",
    "Charmeleon": """ ,-'`|
                  _,"'    j
           __....+       /               .
       ,-'"             /               ; `-._.'.
      /                (              ,'       .'
     |            _.    \             \   ---._ `-.
     ,|    ,   _.'  Y    \             `- ,'   \   `.`.
     l'    \ ,'._,\ `.    .              /       ,--. l
  .,-        `._  |  |    |              \       _   l .
 /              `"--'    /              .'       ``. |  )
.\    ,                 |                .        \ `. '
`.                .     |                '._  __   ;. |'
  `-..--------...'       \                  `'  `-"'.  |
      `......___          `._                        |  |
               /`            `..                     |   .
              /|                `-.                  |    L
             / |               \   `._               .    |
           ,'  |,-"-.   .       .     `.            /     |
         ,'    |     '   \      |       `.         /      |
       ,'     /|       \  .     |         .       /       |
     ,'      / |        \  .    +          \    ,'       .'
    .       .  |         \ |     \          \_,'        / j
    |       |  L          `|      .          `        ,' '
    |    _. |   \          /      |           .     .' ,'
    |   /  `|    \        .       |  /        |   ,' .'
    |   ,-..\     -.     ,        | /         |,.' ,'
    `. |___,`    /  `.   /`.       '          |  .'
      '-`-'     j     ` /."7-..../|          ,`-'
                |        .'  / _/_|          .
                `,       `"'/"'    \          `.
                  `,       '.       `.         |
             __,.-'         `.        |'       |
            /_,-'\          ,'        |        _.
             |___.---.   ,-'        .-':,-"`\,' .
                  L,.--"'           '-' |  ,' `-.|
                                        `.' mh """,
    "Charizard": """
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⠖⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢤⡀⠀⠀⠀⠀⢸⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠈⠢⡀⠀⠀⢀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⡔⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⡹⠀⠀⠘⢄⠀⠈⠲⢖⠈⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠈⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠁⢠⠞⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠉⠑⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠚⠁⠀⠀⠀⡇⠀⠀⠀⠀⠀⢀⠇⠀⡤⡀⠀⠀⠀⢀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢠⣾⣿⣷⣶⣤⣄⣉⠑⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠞⢁⣴⣾⣿⣿⡆⢇⠀⠀⠀⠀⠀⠸⡀⠀⠂⠿⢦⡰⠀⠀⠋⡄⠀⠀⠀⠀⠀⠀⠀⢰⠁⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡴⢁⣴⣿⣿⣿⣿⣿⣿⡘⡄⠀⠀⠀⠀⠀⠱⣔⠤⡀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⡜⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⢣⠀⠀⠀⠀⠀
⠀⠀⠀⡼⢠⣾⣿⣿⣿⣿⣿⣿⣿⣧⡘⢆⠀⠀⠀⠀⠀⢃⠑⢌⣦⠀⠩⠉⠀⡜⠀⠀⠀⠀⠀⠀⢠⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣣⡀⠀⠀⠀
⠀⠀⢰⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠱⡀⠀⠀⠀⢸⠀⠀⠓⠭⡭⠙⠋⠀⠀⠀⠀⠀⠀⠀⡜⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡱⡄⠀⠀
⠀⠀⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢃⠀⠀⠀⢸⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⢀⠜⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠘⣆⠀
⠀⢸⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⣆⠀⠀⡆⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⡠⠖⣡⣾⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⠀
⠀⡏⣾⣿⣿⣿⣿⡿⡛⢟⢿⣿⣿⣿⣿⣿⣿⣧⡈⢦⣠⠃⠀⠀⠀⠀⠀⢱⣀⠤⠒⢉⣾⡉⠻⠋⠈⢘⢿⣿⣿⣿⣿⠿⣿⣿⠏⠉⠻⢿⣿⣿⣿⣿⡘⡆
⢰⡇⣿⣿⠟⠁⢸⣠⠂⡄⣃⠜⣿⣿⠿⠿⣿⣿⡿⠦⡎⠀⠀⠀⠀⠀⠒⠉⠉⠑⣴⣿⣿⣎⠁⠠⠂⠮⢔⣿⡿⠉⠁⠀⠹⡛⢀⣀⡠⠀⠙⢿⣿⣿⡇⡇
⠘⡇⠏⠀⠀⠀⡾⠤⡀⠑⠒⠈⠣⣀⣀⡀⠤⠋⢀⡜⣀⣠⣤⣀⠀⠀⠀⠀⠀⠀⠙⢿⡟⠉⡃⠈⢀⠴⣿⣿⣀⡀⠀⠀⠀⠈⡈⠊⠀⠀⠀⠀⠙⢿⡇⡇
⠀⠿⠀⠀⠀⠀⠈⠀⠉⠙⠓⢤⣀⠀⠁⣀⡠⢔⡿⠊⠀⠀⠀⠀⠙⢦⡀⠀⠐⠢⢄⡀⠁⡲⠃⠀⡜⠀⠹⠟⠻⣿⣰⡐⣄⠎⠀⠀⠀⠀⠀⠀⠀⠀⢣⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠙⢦⣀⢀⡴⠁⠀⠀⠀⠀⠉⠁⢱⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠈⢏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢀⡴⠁⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣧⣠⠤⠖⠋⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠳⢄⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠊⠈⠁⠀⠀⠀⡔⠛⠲⣤⣀⣀⣀⠀⠈⢣⡀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⢀⡠⢔⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢈⠤⠒⣀⠀⠀⠀⠀⣀⠟⠀⠀⠀⠑⠢⢄⡀⠀⠀⠈⡗⠂⠀⠀⠀⠙⢦⠤⠒⢊⡡⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠒⣒⡁⠬⠦⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⢺⢠⠤⡀⢀⠤⡀⠠⠷⡊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠣⡀⡱⠧⡀⢰⠓⠤⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
}

# Functions
def evolve_pokemon():
    global pokemon_name
    if pokemon_level >= 10:
        pokemon_name = "Charizard"
        print(ascii_art["Charizard"])
        print("Your Pokémon evolved into Charizard!\n")
    elif pokemon_level >= 5:
        pokemon_name = "Charmeleon"
        print(ascii_art["Charmeleon"])
        print("Your Pokémon evolved into Charmeleon!\n")
    elif pokemon_level >= 0:
        pokemon_name = "Charmander"
        print(ascii_art["Charmander"])
        print("Your Pokémon evovled into Charmander!\n")

def display_pokemon():
    print(ascii_art.get(pokemon_name, ""))
    print(f"Pokemon Name: {pokemon_name}")
    print(f"Pokemon Level: {pokemon_level}")
    print(f"Battle Wins: {battle_wins}, Battle Losses: {battle_losses}")

def train_pokemon():
    global pokemon_level
    pokemon_level += 1
    evolve_pokemon()
    print("You trained your Pokémon! Your Pokémon level increased by 1.")

def gym_battle():
    global pokemon_level, battle_wins, battle_losses
    outcome = random.randint(1, 2)  # 50% chance to win
    if outcome == 1:
        pokemon_level += 2
        battle_wins += 1
        evolve_pokemon()
        print("Your Pokémon won the gym battle! Your Pokémon level increased by 2.")

    else:
        battle_losses += 1
        print("Your Pokémon lost the gym battle. Better luck next time!")

def main():
    global pokemon_level
    print("\nWelcome to the Pokémon Evolution Simulator!")
    while True:
        print("\nMenu:")
        print("1. Train Pokémon")
        print("2. Gym Battle")
        print("3. Rest / Display Pokémon Info")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            train_pokemon()
        elif choice == "2":
            gym_battle()
        elif choice == "3":
            display_pokemon()
        elif choice == "4":
            print("Exiting the game. See you next time!")
            break
        else:
            print("Invalid. Please select a valid option.")

if __name__ == "__main__":
    main()
