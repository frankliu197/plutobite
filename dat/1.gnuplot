
    set terminal jpeg giant font "Helvetica" 16
        
    set output 'graphs/ad1.jpg'
    
    set grid y
    
    set style data histogram
    
    set style fill solid
    set border 3
    set boxwidth 0.8
    
    set title 'Emotions from Advertisement 1'
    set ylabel '% of Emotion'
    set xlabel 'Emotions'
    set xtics 1
    
    set xrange [0.5:8.5]
    set yrange [0:auto]
    
    plot "data/ad1.txt"            
    