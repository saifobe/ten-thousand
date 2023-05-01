# My chatGBT Request 
```
if new_counter[1] == 3:
            unbanked_points += 1000
        if new_counter[2] == 3:
            unbanked_points += 200
        if new_counter[3] == 3:
            unbanked_points += 300
        if new_counter[4] == 3:
            unbanked_points += 400
        if new_counter[5] == 3:
            unbanked_points += 500
        if new_counter[6] == 3:
            unbanked_points += 600 convert this python code to for loop
```

chatGPT response:
```python
for i in range(2, 7):
    if new_counter[i] == 3:
        unbanked_points += i * 100
```

### on chatGPT I've put the error that ouccured to ous
My chatGBT Request
```python
test_input = (2, 2, 3, 3, 6, 6), expected = 1500

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (tuple(), 0),
            ((1,), 100),
            ((1, 1), 200),
            ((1, 1, 1), 1000),
            ((1, 1, 1, 1), 2000),
            ((1, 1, 1, 1, 1), 4000),
            ((1, 1, 1, 1, 1, 1), 8000),
            ((2,), 0),
            ((2, 2), 0),
            ((2, 2, 2), 200),
            ((2, 2, 2, 2), 400),
            ((2, 2, 2, 2, 2), 800),
            ((2, 2, 2, 2, 2, 2), 1600),
            ((3,), 0),
            ((3, 3), 0),
            ((3, 3, 3), 300),
            ((3, 3, 3, 3), 600),
            ((3, 3, 3, 3, 3), 1200),
            ((3, 3, 3, 3, 3, 3), 2400),
            ((4,), 0),
            ((4, 4), 0),
            ((4, 4, 4), 400),
            ((4, 4, 4, 4), 800),
            ((4, 4, 4, 4, 4), 1600),
            ((4, 4, 4, 4, 4, 4), 3200),
            ((5,), 50),
            ((5, 5), 100),
            ((5, 5, 5), 500),
            ((5, 5, 5, 5), 1000),
            ((5, 5, 5, 5, 5), 2000),
            ((5, 5, 5, 5, 5, 5), 4000),
            ((6,), 0),
            ((6, 6), 0),
            ((6, 6, 6), 600),
            ((6, 6, 6, 6), 1200),
            ((6, 6, 6, 6, 6), 2400),
            ((6, 6, 6, 6, 6, 6), 4800),
            ((1, 2, 3, 4, 5, 6), 2000),
            ((2, 2, 3, 3, 4, 6), 0),
            ((2, 2, 3, 3, 6, 6), 1500),
            ((1, 1, 1, 2, 2, 2), 2400),
        ],
    )
    def test_all(test_input, expected):
        actual = GameLogic().calculate_score(test_input)
>       assert actual == expected
E       assert 0 == 1500

tests/test_calculate_score.py:145: AssertionError
```
chatGPT response:
```python
if len(new_counter) == 3 and all(value == 2 for value in new_counter.values()):
            unbanked_points += 1500
```

### give me a function for determining the dice that are scoring.get_scorers(input): Returns a tuple

### My chatGBT Request

```python

input_counter = Counter(input)
        scoring_dice = []
        if input_counter[1] >= 1 and input_counter[1] < 3:
            scoring_dice.append(1)
        if input_counter[5] >= 1 and input_counter[5] < 3:
            scoring_dice.append(5)
        if input_counter[1] == 3:
            scoring_dice.append(1)
        for i in range(2, 7):
            if input_counter[i] == 3:
                scoring_dice.append(i)
        return tuple(scoring_dice)
```
