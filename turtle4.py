from turtle import*
shape("turtle")
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
  color(col[i])
  circle(100)    #半径１００の円を描くこと
  left(72)      #72度曲がること
done()