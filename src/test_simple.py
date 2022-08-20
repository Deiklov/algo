import pytest
from load_data import load_files_for_bits
from figures import bishop_mask, king_mask, horse_mask, queen_mask, rook_mask


@pytest.mark.parametrize("files", load_files_for_bits('../0.BITS 2/1.Bitboard - Король'))
def test_king_mask(files):
    in_pos, out_cnt, out_mask = files
    assert king_mask(in_pos)[1] == out_mask
    assert king_mask(in_pos)[0] == out_cnt


@pytest.mark.parametrize("files", load_files_for_bits('../0.BITS 2/2.Bitboard - Конь'))
def test_horse_mask(files):
    in_pos, out_cnt, out_mask = files
    assert horse_mask(in_pos)[0] == out_cnt
    assert horse_mask(in_pos)[1] == out_mask


@pytest.mark.parametrize("files", load_files_for_bits('../0.BITS 2/3.Bitboard - Ладья'))
def test_rook_mask(files):
    in_pos, out_cnt, out_mask = files
    assert rook_mask(in_pos)[0] == out_cnt
    assert rook_mask(in_pos)[1] == out_mask


@pytest.mark.parametrize("files", load_files_for_bits('../0.BITS 2/4.Bitboard - Слон'))
def test_bishop_mask(files):
    in_pos, out_cnt, out_mask = files
    assert bishop_mask(in_pos)[0] == out_cnt
    assert bishop_mask(in_pos)[1] == out_mask


@pytest.mark.parametrize("files", load_files_for_bits('../0.BITS 2/5.Bitboard - Ферзь'))
def test_queen_mask(files):
    in_pos, out_cnt, out_mask = files
    assert queen_mask(in_pos)[0] == out_cnt
    assert queen_mask(in_pos)[1] == out_mask
