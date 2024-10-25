from flask import Flask, redirect, url_for, render_template, request, session
from emoji import emojize
from function import win_check, place_emoji
#1 for x 2 for o
# temp var
moon = emojize(":waxing_gibbous_moon:")
star = emojize(":star:")
import os
#-----------------------------------------------------------------------------------






def place_symbol(array,pos1, pos2):

  if session['arrey'][pos1][pos2] == 0:
    array[pos1][pos2] = 1
    session['arrey'][pos1][pos2] = 1
    session['turn'] +=1

  else:
    print("Position taken")
  




  #odd is moom, x
  # even is star, y 
def alternate_turn(x_array,y_array,pos1,pos2):
  turn = session['turn']

  if turn %2 == 0:   
    place_symbol(y_array, pos1, pos2)
  else:
    place_symbol(x_array, pos1, pos2)




#---------------------
app = Flask(__name__)
app.secret_key = "hello"
@app.route("/")
def start():
  session['x_array'] = [[0,0,0],[0,0,0],[0,0,0] ]
  session['y_array'] = [ [0,0,0], [0,0,0], [0,0,0]  ]
  session['turn'] = 1
  session['emoji_cordinates'] = emoj_cordinates = [["","",""],["","",""],["","",""]]
  session['arrey'] = [[0,0,0],[0,0,0],[0,0,0] ]
  return redirect (url_for('home'))
#-----

@app.route("/home")
def home():
  place_emoji(session['x_array'],  session['emoji_cordinates'],moon)
  place_emoji(session['y_array'],  session['emoji_cordinates'],star)
  if win_check(session['x_array']):
    win_text1 = f"{moon} wins!!!"
    return render_template('end2.html', titl = win_text1)
  
  elif win_check(session['y_array']):
    win_text2 = f"{star} wins!!!"
    return render_template('end3.html', titl = win_text2, )
  elif session['arrey'] == [ [1,1,1], [1,1,1],[1,1,1]]:
    win_text3 = "Tie??"
    return render_template('end.html', titl = win_text3 )
  
  else:
    pass
  print(session['turn'])
  print(session['x_array'])
  print(session['y_array'])
  return render_template('index.html', vary = session['emoji_cordinates'])

@app.route("/1-1")
def input_0():
  alternate_turn(session['x_array'], session['y_array'],0,0)

  
  return redirect(url_for('home'))

@app.route("/1-2")
def input_1():
  alternate_turn(session['x_array'],session['y_array'] , 0,1)

  return redirect(url_for('home'))


@app.route("/1-3")
def input_2():
  alternate_turn(session['x_array'],session['y_array'],0,2)
  
  return redirect(url_for('home'))

@app.route("/2-1")
def input_3():
  alternate_turn(session['x_array'],session['y_array'],1,0)

  return redirect(url_for('home'))

@app.route("/2-2")
def input_4():
  alternate_turn(session['x_array'],session['y_array'],1,1)

  return redirect(url_for('home'))

@app.route("/2-3")
def input_5():
  alternate_turn(session['x_array'],session['y_array'],1,2)

  return redirect(url_for('home'))

@app.route("/3-1")
def input_6():
  alternate_turn(session['x_array'],session['y_array'],2,0)

  return redirect(url_for('home'))

@app.route("/3-2")
def input_7():
  alternate_turn(session['x_array'],session['y_array'],2,1)

  return redirect(url_for('home'))

@app.route("/3-3")
def input_8():
  alternate_turn(session['x_array'],session['y_array'],2,2)

  return redirect(url_for('home'))






if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
