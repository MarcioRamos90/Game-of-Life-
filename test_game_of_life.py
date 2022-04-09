import pytest
from itertools import chain

from game_of_life import (
    LIVE,
    DEAD,
    makegrid,
    initialize,
    next_generation,
    qtd_live_neighbors
)


def test_make_grid_with_20_columns_20_rows():
    # Arrange
    columns, rows = 20, 20

    # Action
    result = makegrid(columns=columns, rows=rows)

    # Assert
    assert len(result) == 20
    assert len(result[0]) == 20


def test_initialize_with_random_0_or_1_in_each_fields():
    # Arrange
    columns, rows = 20, 20

    grid = makegrid(columns=columns, rows=rows)

    # Action
    result = list(chain.from_iterable(initialize(grid=grid)))

    # Assert
    assert sum(result) > len(result) / 4


def test_qtd_live_neighbors_():
    # Arrange
    fake_grid = [
        [DEAD,LIVE,DEAD,LIVE],
        [LIVE,DEAD,LIVE,DEAD],
        [DEAD,DEAD,DEAD,LIVE],
    ]

    x, y = 1, 1

    # Action
    result = qtd_live_neighbors(grid=fake_grid, row=x, col=y, len_row=3, len_col=4)

    # Assert
    assert result == 3


@pytest.mark.skip()
def test_should_live_if_have_3_neighbors():
    # Arrange
    fake_grid = [
        [DEAD,LIVE,DEAD,DEAD,LIVE],
        [LIVE,DEAD,LIVE,DEAD,DEAD],
        [DEAD,DEAD,DEAD,DEAD,DEAD],
        [DEAD,DEAD,DEAD,DEAD,DEAD],
    ]

    expected_grid = [
        [DEAD,LIVE,DEAD,DEAD,LIVE],
        [LIVE,LIVE,LIVE,DEAD,DEAD],
        [DEAD,DEAD,DEAD,DEAD,DEAD],
        [DEAD,DEAD,DEAD,DEAD,DEAD],
    ]

    # Action
    result = next_generation(fake_grid)

    # Assert
    assert expected_grid == result
