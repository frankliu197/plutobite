
    set terminal jpeg giant font "Helvetica" 16
        
    set output 'graphs/ad2.jpg'
    
    set grid y

    set style data histogram
    
    set style fill solid
    set border 3
    set boxwidth 0.8 relative
    
    set title 'Emotions from Advertisement 2'
    set ylabel '% of Emotion'
    set xlabel 'Emotions'
    set xtics 1
    set xtics nomirror rotate by -45 scale 0 font ",13"

    set xrange [-0.5:8.5]
    set autoscale y 

    plot "data/ad2.txt"            using 2:xtic(1)
    