import pygame
import random
bubbles = [
('images/A.png'), ('images/B.png'), ('images/C.png'),
('images/D.png'),('images/E.png'),('images/F.png'),
('images/G.png'),('images/H.png'),('images/I.png'),
('images/J.png'),('images/K.png'),('images/L.png'),
('images/M.png'),('images/N.png'),('images/O.png'),
('images/P.png'),('images/Q.png'),('images/R.png'),
('images/S.png'),('images/T.png'),('images/U.png'),
('images/V.png'),('images/W.png'),('images/X.png'),
('images/Y.png'),('images/Z.png')]
letters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

lvl1 = random.choice(letters)

words2 = [('F','A','T'), ('A','C','T'), ('C','A','N'), ('R','U','N'), ('T','A','X'), ('I','L','L')]
lvl2 = random.choice(words2)
print(lvl2)