import pytest
from load_data import load_files_for_bits
from king import king_mask


@pytest.mark.parametrize("files", load_files_for_bits('../0.BITS 2/1.Bitboard - Король'))
def test_king_mask(files):
    in_pos, out_cnt,out_mask = files
    assert king_mask(in_pos)[1] == out_mask
    assert king_mask(in_pos)[0] == out_cnt
