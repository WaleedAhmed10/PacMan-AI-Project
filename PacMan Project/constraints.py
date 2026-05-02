SCR_WIDTH  = 1360
SCR_HEIGHT = 768
TILE_SIZE  = 32
FPS        = 60
COLS       = SCR_WIDTH  // TILE_SIZE   # 42
ROWS       = SCR_HEIGHT // TILE_SIZE   # 24

BLACK            = (0,   0,   0  )
YELLOW           = (255, 255, 0  )
FRIGHTENED_COLOR = (0,   0,   200)   # renamed — was clashing with state
BLUE             = (0,   0,   255)
WHITE            = (255, 255, 255)
RED              = (255, 0,   0  )
PINK             = (255, 184, 255)
CYAN             = (0,   255, 255)
ORANGE           = (255, 184, 81 )
DARK_BLUE        = (0,   0,   139)

UP    = (0,  -1)
DOWN  = (0,   1)
LEFT  = (-1,  0)
RIGHT = (1,   0)

EMPTY        = 0
DOT          = 1   # renamed score to DOT_SCORE below
WALL         = 2
POWER_PELLET = 3   # renamed score to POWER_PELLET_SCORE below
GHOST_HOUSE  = 4
TUNNEL       = 5

CHASE           = "chase"
SCATTER         = "scatter"
FRIGHTENED_STATE= "frightened"   # renamed — was clashing with color
EATEN           = "eaten"
HOUSE           = "house"

START     = "start"
PLAYING   = "playing"
PAUSED    = "paused"
GAME_OVER = "game_over"
WIN       = "win"

DOT_SCORE          = 10
POWER_PELLET_SCORE = 100
GHOST_SCORE        = 200    # renamed from GHOST
GHOST_SCORE_1      = 400    # 1st ghost eaten during power-up
GHOST_SCORE_2      = 800    # 2nd ghost
GHOST_SCORE_3      = 1600   # 3rd ghost
GHOST_SCORE_4      = 3200   # 4th ghost

POWER_UP_DURATION = 7000
SCATTER_DURATION  = 7000
CHASE_DURATION    = 20000
GHOST_FLASH_START = 3000