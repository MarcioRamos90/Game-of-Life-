from src.game.game_of_life import LIVE, DEAD
from src.output.terminal import build_grid, CHAR_DEAD, CHAR_LIVE

def test_str_build():
    fake_grid = [
        [DEAD,LIVE,DEAD,DEAD],
        [LIVE,DEAD,LIVE,DEAD],
        [DEAD,DEAD,DEAD,DEAD],
    ]

    expect = "\n"\
        f"{CHAR_DEAD}{CHAR_LIVE}{CHAR_DEAD}{CHAR_DEAD}\n"\
        f"{CHAR_LIVE}{CHAR_DEAD}{CHAR_LIVE}{CHAR_DEAD}\n"\
        f"{CHAR_DEAD}{CHAR_DEAD}{CHAR_DEAD}{CHAR_DEAD}"

    result = build_grid(fake_grid)

    assert result == expect
