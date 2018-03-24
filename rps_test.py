import rps
import pytest
import subprocess
import sys

def test_rock_is_valid_play():
        assert rps.is_valid_play('rock') is True

def test_paper_is_valid_play():
        assert rps.is_valid_play('paper') is True

def test_scissors_is_valid_play():
        assert rps.is_valid_play('scissors') is True

def test_lizard_is_valid_play():
        assert rps.is_valid_play('lizard') is False

def test_spock_is_valid_play():
        assert rps.is_valid_play('sock') is False

def test_random_valid_play_is_valid():
	for _ in range (100):
		play = rps.random_play()
		assert rps.is_valid_play(play)

def test_random_play_is_fairish():
	plays = [rps.random_play() for _ in range (100)]
	assert plays.count('rock') > 10
	assert plays.count('paper') > 10
	assert plays.count('scissors') > 10

def test_paper_beats_rock():
	assert rps.determine_game_result('paper', 'rock') == 'human'

def input_fake_rock(fake):
	def input_fake(prompt):
		print(prompt)
		return fake
	return input_fake
	
#decorator pro pytest - předávám parametry, abych nemusela psát ten test 3x
@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors'])
#při monkeypatchování přidám parametr do funkce - monkeypatch
def test_whole_game(capsys, play):
#	monkeypatch.setattr('builtins.input', input_fake_rock)
	rps.main(input=input_fake_rock(play)) #dependency injection namísto monkeypatch - nebezpečný způsob podvrhnutí dat
	print('haha')
	out, err = capsys.readouterr()
	assert 'rock, paper or scissors?' in out
	assert ('computer wins' in out or 'human wins' in out or 'it\'s a tie' in out)

def test_game_asks_again_if_wrong_input():
	cp = subprocess.run([sys.executable, 'rps.py'],
			input = 'asdf\nrock',
			encoding = 'utf-8',
			stdout = subprocess.PIPE)
	assert cp.stdout.count('rock, paper or scissors?') == 2
