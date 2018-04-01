
    set terminal jpeg giant font "Helvetica" 16
        
    set output 'overall/overall.jpg'
    set key right
    set grid y

    set style data histogram
    set style histogram rowstacked
    set style fill solid
    set border 3
    set boxwidth 0.8 relative
    
    set title 'Emotions from all the Advertisements'
    set ylabel '% Total Emotions'
    set xlabel 'Advertisement Number'
    set xtics 1
    

    set xrange [*<-0.5:5<*]
    set yrange[0:100] 

    plot "overall/overall.txt"            using 2 t "Anger", ''  using 3 t "Contempt", ''  using 4 t "Disgust", ''  using 5 t "Fear", ''  using 6 t "Happiness", ''  using 7 t "Neutral", ''  using 8 t "Sadness", ''  using 9 t "Surprise"
    