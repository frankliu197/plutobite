from string import Template
import os

dic = {"output" : "emotions_test", "title" : "Emotions", "x_label" : "title", "y_label" : "title", "x_max" : 10 , "y_max" : 100}

dat_file = Template("""
set terminal jpeg giant font "Helvetica" 16

set output '$output.jpg'
set key right
set grid y

set style data histogram
set style histogram rowstacked
set style fill solid
set border 3
set boxwidth 0.6

set title '$title'
set ylabel '$x_label'
set xlabel '$y_label'
set xtics 1

set xrange [0.5:$x_max]
set yrange [0:$y_max]

plot "emotions.dat"\
        using 2 t "Happy" lt rgb "green", \
        '' using 3 t "Sad" lt rgb "gray", \
        '' using 4 t "Surprised" lt rgb "yellow" 
""").substitute(dic)

output = open("tester.dat", "w")
output.write(dat_file)
output.close()

os.system("cat tester.dat")
