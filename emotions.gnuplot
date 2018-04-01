
set terminal jpeg giant font "Helvetica" 16

set output 'emotions.jpg'
set key right
set grid y

set style data histogram
set style histogram rowstacked
set style fill solid
set border 3
set boxwidth 0.6

set title 'Emotions from Advertisement 0'
set ylabel '% Total'
set xlabel 'Image Number'
set xtics 1

set xrange [0.5:10]
set yrange [0:100]

plot "emotions.dat"        using 2 t "Happy" lt rgb "green", '' using 3 t "Sad" lt rgb "gray", '' using 4 t "Surprised" lt rgb "yellow" 
