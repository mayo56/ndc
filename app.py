import pyxel



# <<< ============ >>>
# ////////////////////
#       VARIABLE
# ////////////////////
# menu start
menu_start_select = 0
menu_start_select_range = 1
menu_start = True

# menu pause
menu_pause_select = 0
menu_pause_select_range = 1
menu_pause = False

# menu egnime
menu_egnime_select = 0
menu_egnime_select_range = 3
menu_egnime = False
egnime = [
  {
    "x": 36,
    "text": "2+2= ?",
    "A": "1",
    "B": "2",
    "C": "5",
    "D": "4",
    "good:": "d",
  },
  {
    "x": 36,
    "text": "2+2= ?",
    "A": "1",
    "B": "2",
    "C": "5",
    "D": "4",
    "good:": "d",
  },
  {
   "x": 36,
    "text": "2+2= ?",
    "A": "1",
    "B": "2",
    "C": "5",
    "D": "4",
    "good:": "d",
  },
  {
    "x": 36,
    "text": "2+2= ?",
    "A": "1",
    "B": "2",
    "C": "5",
    "D": "4",
    "good:": "d",
  },
  {
    "x": 36,
    "text": "2+2= ?",
    "A": "1",
    "B": "2",
    "C": "5",
    "D": "4",
    "good:": "d",
  },
]

# >>> -- GOD MODE -- <<<
god_mode = False

# >>> -- OVERLAY -- <<<
player_life = 3
player_keys = 0
player_skip = 0
player_clue = 0

# >>> -- Player -- <<<
player_position = [1775,1719]

# >> -- Coffres -- <<<
coffres = [
  {"x":1538+55,"y":1560+55, "open": False},
  {"x":1272+55,"y":1300+55, "open": False},
  {"x":1449+55,"y":1124+55, "open": False},
  {"x":1073+55,"y":1547+55, "open": False},
  {"x":1400+55,"y":1713+55, "open": False},
]

# >>> -- JSP -- <<<
mur = [
  {
    "a": {
      "x": 227,
      "y": 221,
    },
    "b": {
      "x": 228,
      "y": 221,
    },
    "c": {
      "x": 227,
      "y": 222,
    },
    "d": {
      "x": 228,
      "y": 222,
    },
  },
  {
    "a": {
      "x": 228,
      "y": 221,
    },
    "b": {
      "x": 228,
      "y": 221,
    },
    "c": {
      "x": 228,
      "y": 223,
    },
    "d": {
      "x": 228,
      "y": 223,
    },
  },
  {
    "a": {
      "x": 230,
      "y": 221,
    },
    "b": {
      "x": 230,
      "y": 221,
    },
    "c": {
      "x": 230,
      "y": 223,
    },
    "d": {
      "x": 230,
      "y": 223,
    },
  },
   {
    "a": {
      "x": 230,
      "y": 221,
    },
    "b": {
      "x": 231,
      "y": 221,
    },
    "c": {
      "x": 230,
      "y": 222,
    },
    "d": {
      "x": 231,
      "y": 222,
    },
  },
   {
    "a": {
      "x": 231,
      "y": 221,
    },
    "b": {
      "x": 231,
      "y": 221,
    },
    "c": {
      "x": 231,
      "y": 221,
    },
    "d": {
      "x": 231,
      "y": 221,
    },
  },
   {
    "a": {
      "x": 231,
      "y": 212,
    },
    "b": {
      "x": 231,
      "y": 212,
    },
    "c": {
      "x": 231,
      "y": 221,
    },
    "d": {
      "x": 231,
      "y": 221,
    },
  },
   {
    "a": {
      "x": 227,
      "y": 212,
    },
    "b": {
      "x": 227,
      "y": 212,
    },
    "c": {
      "x": 227,
      "y": 222,
    },
    "d": {
      "x": 227,
      "y": 222,
    },
  },
   {
    "a": {
      "x": 227,
      "y": 212,
    },
    "b": {
      "x": 228,
      "y": 212,
    },
    "c": {
      "x": 227,
      "y": 213,
    },
    "d": {
      "x": 228,
      "y": 213,
    },
  },
   {
    "a": {
      "x": 228,
      "y": 204,
    },
    "b": {
      "x": 228,
      "y": 204,
    },
    "c": {
      "x": 228,
      "y": 213,
    },
    "d": {
      "x": 228,
      "y": 213,
    },
  },
   {
    "a": {
      "x": 230,
      "y": 201,
    },
    "b": {
      "x": 230,
      "y": 201,
    },
    "c": {
      "x": 230,
      "y": 213,
    },
    "d": {
      "x": 230,
      "y": 213,
    },
  },
   {
    "a": {
      "x": 223,
      "y": 204,
    },
    "b": {
      "x": 223,
      "y": 204,
    },
    "c": {
      "x": 228,
      "y": 204,
    },
    "d": {
      "x": 228,
      "y": 204,
    },
  },
   {
    "a": {
      "x": 223,
      "y": 201,
    },
    "b": {
      "x": 223,
      "y": 201,
    },
    "c": {
      "x": 230,
      "y": 202,
    },
    "d": {
      "x": 230,
      "y": 202,
    },
  },
   {
    "a": {
      "x": 223,
      "y": 204,
    },
    "b": {
      "x": 223,
      "y": 204,
    },
    "c": {
      "x": 223,
      "y": 230,
    },
    "d": {
      "x": 223,
      "y": 230,
    },
  },
   {
    "a": {
      "x": 220,
      "y": 204,
    },
    "b": {
      "x": 220,
      "y": 204,
    },
    "c": {
      "x": 220,
      "y": 229,
    },
    "d": {
      "x": 220,
      "y": 229,
    },
  },
   {
    "a": {
      "x": 223,
      "y": 194,
    },
    "b": {
      "x": 223,
      "y": 194,
    },
    "c": {
      "x": 223,
      "y": 201,
    },
    "d": {
      "x": 223,
      "y": 201,
    },
  },
   {
    "a": {
      "x": 220,
      "y": 194,
    },
    "b": {
      "x": 220,
      "y": 194,
    },
    "c": {
      "x": 220,
      "y": 202,
    },
    "d": {
      "x": 220,
      "y": 202,
    },
  },
   {
    "a": {
      "x": 208,
      "y": 202,
    },
    "b": {
      "x": 208,
      "y": 202,
    },
    "c": {
      "x": 220,
      "y": 202,
    },
    "d": {
      "x": 220,
      "y": 202,
    },
  },
   {
    "a": {
      "x": 208,
      "y": 204,
    },
    "b": {
      "x": 208,
      "y": 204,
    },
    "c": {
      "x": 220,
      "y": 204,
    },
    "d": {
      "x": 220,
      "y": 204,
    },
  },
   {
    "a": {
      "x": 208,
      "y": 204,
    },
    "b": {
      "x": 208,
      "y": 204,
    },
    "c": {
      "x": 208,
      "y": 215,
    },
    "d": {
      "x": 208,
      "y": 215,
    },
  },
   {
    "a": {
      "x": 191,
      "y": 216,
    },
    "b": {
      "x": 291,
      "y": 216,
    },
    "c": {
      "x": 208,
      "y": 216,
    },
    "d": {
      "x": 208,
      "y": 216,
    },
  },
   {
    "a": {
      "x": 192,
      "y": 205,
    },
    "b": {
      "x": 192,
      "y": 205,
    },
    "c": {
      "x": 191,
      "y": 216,
    },
    "d": {
      "x": 191,
      "y": 216,
    },
  },
   {
    "a": {
      "x": 191,
      "y": 184,
    },
    "b": {
      "x": 191,
      "y": 184,
    },
    "c": {
      "x": 191,
      "y": 202,
    },
    "d": {
      "x": 191,
      "y": 202,
    },
  },
   {
    "a": {
      "x": 191,
      "y": 184,
    },
    "b": {
      "x": 191,
      "y": 184,
    },
    "c": {
      "x": 208,
      "y": 184,
    },
    "d": {
      "x": 208,
      "y": 184,
    },
  },
   {
    "a": {
      "x": 208,
      "y": 184,
    },
    "b": {
      "x": 208,
      "y": 184,
    },
    "c": {
      "x": 208,
      "y": 202,
    },
    "d": {
      "x": 208,
      "y": 202,
    },
  },
   {
    "a": {
      "x": 172,
      "y": 204,
    },
    "b": {
      "x": 172,
      "y": 204,
    },
    "c": {
      "x": 191,
      "y": 204,
    },
    "d": {
      "x": 191,
      "y": 204,
    },
  },
   {
    "a": {
      "x": 175,
      "y": 202,
    },
    "b": {
      "x": 175,
      "y": 202,
    },
    "c": {
      "x": 191,
      "y": 202,
    },
    "d": {
      "x": 191,
      "y": 202,
    },
  },
   {
    "a": {
      "x": 172,
      "y": 193,
    },
    "b": {
      "x": 172,
      "y": 193,
    },
    "c": {
      "x": 172,
      "y": 204,
    },
    "d": {
      "x": 172,
      "y": 204,
    },
  },
   {
    "a": {
      "x": 175,
      "y": 179,
    },
    "b": {
      "x": 175,
      "y": 179,
    },
    "c": {
      "x": 175,
      "y": 202,
    },
    "d": {
      "x": 175,
      "y": 202,
    },
  },
   {
    "a": {
      "x": 167,
      "y": 192,
    },
    "b": {
      "x": 167,
      "y": 192,
    },
    "c": {
      "x": 172,
      "y": 192,
    },
    "d": {
      "x": 172,
      "y": 192,
    },
  },
   {
    "a": {
      "x": 167,
      "y": 192,
    },
    "b": {
      "x": 167,
      "y": 192,
    },
    "c": {
      "x": 167,
      "y": 220,
    },
    "d": {
      "x": 167,
      "y": 220,
    },
  },
   {
    "a": {
      "x": 167,
      "y": 220,
    },
    "b": {
      "x": 167,
      "y": 220,
    },
    "c": {
      "x": 183,
      "y": 220,
    },
    "d": {
      "x": 183,
      "y": 220,
    },
  },
   {
    "a": {
      "x": 164,
      "y": 223,
    },
    "b": {
      "x": 164,
      "y": 223,
    },
    "c": {
      "x": 183,
      "y": 223,
    },
    "d": {
      "x": 183,
      "y": 223,
    },
  },
   {
    "a": {
      "x": 163,
      "y": 213,
    },
    "b": {
      "x": 163,
      "y": 213,
    },
    "c": {
      "x": 164,
      "y": 223,
    },
    "d": {
      "x": 164,
      "y": 223,
    },
  },
   {
    "a": {
      "x": 153,
      "y": 216,
    },
    "b": {
      "x": 153,
      "y": 216,
    },
    "c": {
      "x": 163,
      "y": 213,
    },
    "d": {
      "x": 163,
      "y": 213,
    },
  },
   {
    "a": {
      "x": 153,
      "y": 213,
    },
    "b": {
      "x": 153,
      "y": 213,
    },
    "c": {
      "x": 153,
      "y": 219,
    },
    "d": {
      "x": 153,
      "y": 219,
    },
  },
   {
    "a": {
      "x": 140,
      "y": 219,
    },
    "b": {
      "x": 140,
      "y": 219,
    },
    "c": {
      "x": 153,
      "y": 219,
    },
    "d": {
      "x": 153,
      "y": 219,
    },
  },
   {
    "a": {
      "x": 143,
      "y": 217,
    },
    "b": {
      "x": 143,
      "y": 217,
    },
    "c": {
      "x": 149,
      "y": 217,
    },
    "d": {
      "x": 149,
      "y": 217,
    },
  },
   {
    "a": {
      "x": 150,
      "y": 211,
    },
    "b": {
      "x": 150,
      "y": 211,
    },
    "c": {
      "x": 150,
      "y": 216,
    },
    "d": {
      "x": 150,
      "y": 216,
    },
  },
   {
    "a": {
      "x": 150,
      "y": 211,
    },
    "b": {
      "x": 150,
      "y": 211,
    },
    "c": {
      "x": 164,
      "y": 211,
    },
    "d": {
      "x": 164,
      "y": 211,
    },
  },
   {
    "a": {
      "x": 140,
      "y": 200,
    },
    "b": {
      "x": 140,
      "y": 200,
    },
    "c": {
      "x": 140,
      "y": 219,
    },
    "d": {
      "x": 140,
      "y": 219,
    },
  },
   {
    "a": {
      "x": 143,
      "y": 200,
    },
    "b": {
      "x": 143,
      "y": 200,
    },
    "c": {
      "x": 143,
      "y": 217,
    },
    "d": {
      "x": 143,
      "y": 217,
    },
  },
   {
    "a": {
      "x": 164,
      "y": 188,
    },
    "b": {
      "x": 164,
      "y": 188,
    },
    "c": {
      "x": 164,
      "y": 211,
    },
    "d": {
      "x": 164,
      "y": 211,
    },
  },
   {
    "a": {
      "x": 164,
      "y": 188,
    },
    "b": {
      "x": 164,
      "y": 188,
    },
    "c": {
      "x": 171,
      "y": 188,
    },
    "d": {
      "x": 171,
      "y": 188,
    },
  },
   {
    "a": {
      "x": 175,
      "y": 179,
    },
    "b": {
      "x": 175,
      "y": 179,
    },
    "c": {
      "x": 175,
      "y": 202,
    },
    "d": {
      "x": 175,
      "y": 202,
    },
  },
   {
    "a": {
      "x": 151,
      "y": 179,
    },
    "b": {
      "x": 151,
      "y": 179,
    },
    "c": {
      "x": 171,
      "y": 179,
    },
    "d": {
      "x": 171,
      "y": 179,
    },
  },
   {
    "a": {
      "x": 175,
      "y": 179,
    },
    "b": {
      "x": 175,
      "y": 179,
    },
    "c": {
      "x": 191,
      "y": 179,
    },
    "d": {
      "x": 191,
      "y": 179,
    },
  },
   {
    "a": {
      "x": 191,
      "y": 160,
    },
    "b": {
      "x": 191,
      "y": 160,
    },
    "c": {
      "x": 191,
      "y": 179,
    },
    "d": {
      "x": 191,
      "y": 179,
    },
  },
]


# <<< ============ >>>

#  menu
class Menu_Start:
    def upate(self) -> None:
      global menu_start_select, menu_start_select_range, menu_egnime, menu_pause, menu_start

      if pyxel.btnp(pyxel.KEY_UP):
        menu_start_select -= 1
        if menu_start_select < 0:
          menu_start_select = menu_start_select_range
      if pyxel.btnp(pyxel.KEY_DOWN):
        menu_start_select += 1
        if menu_start_select > menu_start_select_range:
          menu_start_select = 0

      if pyxel.btnp(pyxel.KEY_RETURN):
        if menu_start_select == 1:
          pyxel.quit()
        if menu_start_select == 0:
          menu_start = False

    
    def draw(self) -> None:
      # restart
      pyxel.camera(0,0)

      global menu_start_select, menu_start_select_range
      pyxel.rect(14, 14, 100, 100, 1)
      pyxel.text(45, 25, "MENU_START", 3)

      if menu_start_select == 0:
        pyxel.text(42, 40, "<  START  >", 4)
      else:  
        pyxel.text(54, 40, "START", 4)

      if menu_start_select == 1:
        pyxel.text(44, 60, "<  QUIT  >", 4)
      else: 
        pyxel.text(56, 60, "QUIT", 4)


# MENU PAUSE
class Menu_Pause:
    def upate(self) -> None:
      global menu_pause_select, menu_pause_select_range, menu_egnime, menu_pause, menu_start

      if pyxel.btnp(pyxel.KEY_TAB) and not menu_egnime and not menu_start:
        if menu_pause == False:
          menu_pause = True
          menu_pause_select = 0
        else:
          menu_pause = False

      if menu_pause:
        if pyxel.btnp(pyxel.KEY_UP):
          menu_pause_select -= 1
          if menu_pause_select < 0:
            menu_pause_select = menu_pause_select_range
        if pyxel.btnp(pyxel.KEY_DOWN):
          menu_pause_select += 1
          if menu_pause_select > menu_pause_select_range:
            menu_pause_select = 0

        if pyxel.btnp(pyxel.KEY_RETURN):
          if menu_pause_select == 1:
            pyxel.quit()
          if menu_pause_select == 0:
            menu_pause = False

    
    def draw(self) -> None:
      # restart
      global menu_pause_select, menu_pause_select_range, player_position, menu_egnime, menu_start

      if menu_pause:
        pyxel.rect((player_position[0] + 14), (player_position[1] + 14), 100, 100, 1)
        pyxel.text((player_position[0] + 45), (player_position[1] + 25), "MENU_PAUSE", 3)

        if menu_pause_select == 0:
          pyxel.text((player_position[0] + 42), (player_position[1] + 40), "<  START  >", 4)
        else:  
          pyxel.text((player_position[0] + 54), (player_position[1] + 40), "START", 4)

        if menu_pause_select == 1:
          pyxel.text((player_position[0] + 44), (player_position[1] + 60), "<  QUIT  >", 4)
        else: 
          pyxel.text((player_position[0] + 56), (player_position[1] + 60), "QUIT", 4)

# MENU egnime
class Menu_egnime:
    def upate(self) -> None:
      global menu_egnime_select, menu_egnime_select_range, menu_egnime, menu_pause, menu_start

      if pyxel.btnp(pyxel.KEY_E) and not menu_pause and not menu_start:
        if menu_egnime == False:
          menu_egnime = True
          menu_egnime_select = 0
        else:
          menu_egnime = False

      if menu_egnime:
        if pyxel.btnp(pyxel.KEY_UP):
          menu_egnime_select -= 1
          if menu_egnime_select < 0:
            menu_egnime_select = menu_egnime_select_range
        if pyxel.btnp(pyxel.KEY_DOWN):
          menu_egnime_select += 1
          if menu_egnime_select > menu_egnime_select_range:
            menu_egnime_select = 0

        if pyxel.btnp(pyxel.KEY_RETURN):
          if menu_egnime_select == 3:
              pass
          if menu_egnime_select == 2:
            pass
          if menu_egnime_select == 1:
              pass
          if menu_egnime_select == 0:
            pass

    
    def draw(self) -> None:
  
      global menu_egnime_select, menu_egnime_select_range, egnime, player_position, menu_egnime, menu_pause, menu_start
      if menu_egnime:
        pyxel.rect((player_position[0] + 14), (player_position[1] + 14), 100, 100, 1)

        # rajouter le trucs pour choisir l'egnime
        pyxel.text((player_position[0] + 45), (player_position[1] + 25), "MENU_EGNIME", 3)
        pyxel.text((player_position[0] + egnime[0]["x"]), player_position[1] + 40, egnime[0]["text"], 4)
        

        # btn1
        if menu_egnime_select == 0:
          pyxel.text((player_position[0] + 36), player_position[1] + 70, f"<  {egnime[0]['A']}  >", 4)
        else:  
          pyxel.text((player_position[0] + 48), player_position[1] + 70, f"{egnime[0]['A']}", 4)

        # btn2
        if menu_egnime_select == 1:
          pyxel.text((player_position[0] + 36), (player_position[1] + 80), f"<  {egnime[0]['B']}  >", 4)
        else:  
          pyxel.text((player_position[0] + 48), (player_position[1] + 80), f"{egnime[0]['B']}", 4)

        # btn3
        if menu_egnime_select == 2:
          pyxel.text((player_position[0] + 36), (player_position[1] + 90), f"<  {egnime[0]['C']}  >", 4)
        else:  
          pyxel.text((player_position[0] + 48), (player_position[1] + 90), f"{egnime[0]['C']}", 4)

        # btn4
        if menu_egnime_select == 3:
          pyxel.text((player_position[0] + 36), (player_position[1] + 100), f"<  {egnime[0]['D']}  >", 4)
        else:  
          pyxel.text((player_position[0] + 48), (player_position[1] + 100), f"{egnime[0]['D']}", 4)


# système 
class Overlay:
    # cp (140,11) & (149,19)
    # cv (170,11) & (159,20)

    def life(self) -> None:
        global player_position, player_life, player_keys, player_clue, player_skip
        pyxel.rect(player_position[0], player_position[1], 34, 11, 2) # fond (life)
        for i in range(3): # life
           if i <= player_life:
              pyxel.blt(player_position[0] + (i*11)+1, player_position[1] + 1,0,140,11,10,9,5) # coeur plein
           else:
              pyxel.blt(player_position[0] + (i*11)+1, player_position[1] + 1,0,140,11,10,9,5) # coeur vide
              
    
    def item(self) -> None:
      global player_position, player_life, player_keys, player_clue, player_skip
      pyxel.rect(player_position[0] + 78, player_position[1], 68, 11, 2) # fond (item)
      # items
      pyxel.blt(player_position[0]+78, player_position[1] + 3,0,121,76,6,5,5) # coeur jaune (indice)
      pyxel.text(player_position[0]+88, player_position[1] + 3, f"{player_clue}", 3)
      pyxel.blt(player_position[0]+95, player_position[1] + 3,0,131,76,6,5,5) # coeur bleue (skip)
      pyxel.text(player_position[0]+105, player_position[1] + 3, f"{player_skip}", 3)
      pyxel.blt(player_position[0]+112, player_position[1] + 3,0,63,103,3,6,5) # clé (key)
      pyxel.text(player_position[0]+122, player_position[1] + 3, f"{player_keys}", 3)



# 120.75
# 127.81


      
          # pyxel.blt(player_position[0] + (i*11)+1, player_position[1] + 1,0,140,11,10,9,5) # coeur vide


class Player:
    def update(self) -> None:
        global player_position, menu_pause, menu_start, menu_egnime
        # [0] -> x
        # [1] -> y
        print(player_position)
        if not menu_start and not menu_pause and not menu_egnime:
            if pyxel.btn(pyxel.KEY_RIGHT):
                player_position[0] += 1.5
            if pyxel.btn(pyxel.KEY_LEFT):
                player_position[0] -= 1.5
            if pyxel.btn(pyxel.KEY_UP):
                player_position[1] -= 1.5
            if pyxel.btn(pyxel.KEY_DOWN): 
                player_position[1] += 1.5

    def draw(self) -> None:
        global player_position
        pyxel.camera(player_position[0], player_position[1])
        pyxel.blt((player_position[0] + 59), (player_position[1] + 59),0,132,42,6,8,5)

# Map

class Map: 
  def draw(self) -> None:
    pyxel.bltm(0,0,0,0,0,255*8,255*8) 
  def chest(self) -> None:
    global coffres
    for i in range(5):
      tile = [0,0]
      if coffres[i]["open"]:
        tile = [[41,103],[9,7]]
      else:
        tile = [[31,102],[8,8]]
      pyxel.blt(coffres[i]["x"], coffres[i]["y"],0,tile[0][0],tile[0][1],tile[1][0],tile[1][1],5)


# collision
class collision:
  """Système de collisions (non finit)"""
  def update(self) -> None: 
    global mur, player_position
    # for i in mur:
    #   if i["a"]["x"] == player_position[0]
  

# app

class App:
    def __init__(self) -> None:
        pyxel.init(128,128, title="Labyr1th (v0.0.1)")
        pyxel.load("5.pyxres")
        pyxel.run(self.upate, self.draw)
    
    def upate(self) -> None:
        global menu_start
        # -----------------------
        #   Map < Player < Menu
        # -----------------------
        # -=-=-=-=-=-=-=-=-=-
        # Map


        # -=-=-=-=-=-=-=-=-=-
        # Player
        Player().update()

        # -=-=-=-=-=-=-=-=-=-
        # Menu
        if menu_start:
          Menu_Start().upate()
          
        Menu_egnime().upate()
        Menu_Pause().upate()


    
    def draw(self) -> None:
        global menu_pause, menu_egnime, menu_start
        # -----------------------
        #   Map < Player < Menu
        # -----------------------
        pyxel.cls(0)
        # -=-=-=-=-=-=-=-=-=-
        # Map
        Map().draw()
        Map().chest()
        
        # -=-=-=-=-=-=-=-=-=-
        # Player
        Player().draw()

        # -=-=-=-=-=-=-=-=-=-
        # Overlay
        if not menu_start:
          Overlay().life()
          Overlay().item()


        # -=-=-=-=-=-=-=-=-=-
        # Menu
        if menu_start:
          Menu_Start().draw()
        
        Menu_Pause().draw()
        Menu_egnime().draw() 
App() 