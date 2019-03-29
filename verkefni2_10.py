#verkefni2_10
import string
import re
import itertools
def css_properties(css):

  curly_braces_ingrediant = "{([^}]*)}" #get strings between curly brackets
  css = css.replace('\n', '')
  reg = re.findall(curly_braces_ingrediant, css)
  properties = []
  for c in reg:
    class_splitted = c.split(';') #; delimiter tells us when a key value pair has ended
    for p in class_splitted:
      properties.append(p)
  
  properties = list(filter(lambda x: not all(letter.isspace() for letter in x), properties)) #get rid of empty spaces
  l = []
  for p in properties:
    values = p.split(':')
    values =  map(lambda x: x.strip(), values) 
    l.append(tuple(values))
  print(l)
  return l

css_properties("""
#LasVegas .billboard { text-decoration: blink; }

.ninja, #Snowden { visibility: hidden; }


.oliveoil
{
  z-index: 1;
}
.water
{
  z-index: 0;
}

#poop {
  float  : none  ;
  color  : brown ;

  width  : 15cm  ;
  height : 120cm ;
}

.God { position: absolute; display: none; }
#blackhole { padding: -9999em; }

.word {  font-family:    "Comic Sans", "Times New Roman", sans-serif  ;  }
""")
