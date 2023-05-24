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

# >>> -- Player -- <<<
player_position = [0,0]

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
      "y": 222,
    },
    "d": {
      "x": 231,
      "y": 222,
    },
  },
   {
    "a": {
      "x": 15,
      "y": 12,
    },
    "b": {
      "x": 15,
      "y": 12,
    },
    "c": {
      "x": 15,
      "y": 14,
    },
    "d": {
      "x": 15,
      "y": 14,
    },
  },
]


# <<< ============ >>>

#  menu
class Menu_Start:
    def upate(self) -> None:
      global menu_start_select
      global menu_start_select_range
      global menu_start

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

      global menu_start_select
      global menu_start_select_range
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
      global menu_pause_select
      global menu_pause_select_range
      global menu_pause

      if pyxel.btnp(pyxel.KEY_TAB):
        if menu_pause == False:
          menu_pause = True
          menu_pause_select = 0
        else:
          menu_pause = False


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
      global menu_pause_select, menu_pause_select_range, player_position
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


# système 
class Overlay:
    def __init__(self) -> None:
        pass

    def life(self) -> None:
        global player_position
        pyxel.rect()

class Player:
    def __init__(self) -> None:
        pass
    
    def update(self) -> None:
        global player_position, menu_pause, menu_start
        # [0] -> x
        # [1] -> y
        print(player_position)
        if not menu_start and not menu_pause:
            if pyxel.btn(pyxel.KEY_RIGHT):
                player_position[0] += 1
            if pyxel.btn(pyxel.KEY_LEFT):
                player_position[0] -= 1
            if pyxel.btn(pyxel.KEY_UP):
                player_position[1] -= 1
            if pyxel.btn(pyxel.KEY_DOWN):
                player_position[1] += 1

    def draw(self) -> None:
        global player_position
        pyxel.camera(player_position[0], player_position[1])
        pyxel.blt((player_position[0] + 59), (player_position[1] + 59),0,132,42,6,8,5)




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
        if not menu_start:
          Menu_Pause().upate()


    
    def draw(self) -> None:
        global menu_start
        global menu_pause
        # -----------------------
        #   Map < Player < Menu
        # -----------------------
        pyxel.cls(0)
        # -=-=-=-=-=-=-=-=-=-
        # Map
        pyxel.rect(0,0,120,120,6)

        # -=-=-=-=-=-=-=-=-=-
        # Player
        Player().draw()

        # -=-=-=-=-=-=-=-=-=-
        # Menu
        if menu_start:
          Menu_Start().draw()
        if menu_pause:
          Menu_Pause().draw()
App() 