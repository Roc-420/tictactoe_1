from function import win_check
def test_horizontal_check():
  array= [
    [1,1,1],
    [0,0,0],
    [0,0,0]
  ]
  assert win_check(array) == True
  array= [
    [0,0,0],
    [1,1,1],
    [0,0,0]
  ]
  assert win_check(array) == True
  array= [
  [0,0,0],
  [0,0,0],
  [1,1,1]
 ]
  assert win_check(array) == True


def test_vertical_check():
  array= [
    [1,0,0],
    [1,0,0],
    [1,0,0]
  ]
  assert win_check(array) == True
  array= [
    [0,1,0],
    [0,1,0],
    [0,1,0]
  ]
  assert win_check(array) == True
  array= [
    [0,0,1],
    [0,0,1],
    [0,0,1]
  ]
  assert win_check(array) == True

def test_cross_check():
  array= [
    [0,0,1],
    [0,1,0],
    [1,0,0]
  ]
  assert win_check(array) == True
  array= [
    [1,0,0],
    [0,1,0],
    [0,0,1]
  ]
  assert win_check(array) == True

def test_none_check():
  array= [
      [0,0,0],
      [0,0,0],
      [0,0,0]
    ]
  assert win_check(array) == False
  array= [
    [1,0,1],
    [0,0,0],
    [0,0,1]
  ]
  assert win_check(array) == False
  array= [
    [1,0,1],
    [0,1,0],
    [0,0,0]
  ]
  assert win_check(array) == False



