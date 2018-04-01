#Created by Frank Liu
# Creates a Script to create a graph using gnuplot.
import os
from string import Template

feelings = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']

def get_graph(ad_num=0):
    #writes a script with the input ad given.
    #if an ad_num is given, the function will search for the bat file and output the graph as "graphs/ad#{ad_num}.jpg
    #if no ad_num is given, or if ad_num is 0 the overall graph will be greated in overall/overall.jpg
    #returns the location of the graph made

    def add_colors(str1, str2, str3=''):
        #adds the colors to the corrosponding emotions
        pass

    def add_emotions():
        #adds emotions to plot_style for dic_overall
        s = ""
        for i in range(len(feelings)):
            s+= "using " + str(i + 2) + " t \"" + feelings[i] + "\""
            if i < len(feelings) - 1:
                s+= ", ''  "
        return s

    #the specific properties of the dat_file script, look below
    dic_ad  = {"output_file" : "graphs/ad" + str(ad_num) + ".jpg", "title" : "Emotions from Advertisement " + str(ad_num), 
        "x_label" : "Emotions", "y_label" : "% of Emotion", "x_scale" :"set xrange [-0.5:8.5]", 
        "y_scale": "set autoscale y", "set_key": "unset key", "input_file": "data/ad" + str(ad_num) + ".txt",  "plot_type": "", "x_fonts":"set xtics nomirror rotate by -45 scale 0 font \",13\"",
        "plot_style" : "using 2:xtic(1)"
    }

    dic_overall = {"output_file" : "overall/overall.jpg", "title" : "Emotions from all the Advertisements",
        "x_label" : "Advertisement Number", "y_label" : "% Total Emotions", "x_scale" : "set xrange [*<0:8<*]" , 
        "y_scale" : "set yrange[0:100]", "input_file": "overall/overall.txt", "plot_type": "set style histogram rowstacked",  
        "plot_style" : add_emotions(), "set_key": "set key right", "x_fonts":""
        #"""using 2 t "Happy" lt rgb "green", '' using 3 t "Sad" lt rgb "gray", '' using 4 t "Surprised" lt rgb "yellow" """
    }

    #there are two dics to use, specify the one to use here
    dic = dic_ad
    if ad_num == 0:
           dic = dic_overall

    #the generalized dat file giving a bar graph look. Change the qualities of the script with the dictionary files above
    dat_file = Template("""
    set terminal jpeg giant font "Helvetica" 16
        
    set output '$output_file'
    $set_key
    set key font ",8"
    set key spacing 0.5
    set grid y

    set style data histogram
    $plot_type
    set style fill solid
    set border 3
    set boxwidth 0.8 relative
    
    set title '$title'
    set ylabel '$y_label'
    set xlabel '$x_label'
    set xtics 1
    $x_fonts

    $x_scale
    $y_scale 

    plot "$input_file"\
            $plot_style
    """).substitute(dic)
    
    #Writes the dat_file code into a script
    gnuplot_name = "dat/" + str(ad_num) + ".gnuplot"
    script = open(gnuplot_name, 'w')
    script.write(dat_file)
    script.close()

    #execute the script
    os.system("gnuplot -e \"filename=\'" + dic["input_file"] + "\'\" " + gnuplot_name)
    #os.system("rm " + gnuplot_name)
    return dic['output_file']    



