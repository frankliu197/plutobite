# Creates a Script to create a graph using gnuplot.
import os
from string import Template

feelings = ['contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']

def get_graph(input_file):
    #writes a script with the input file given. Assumes coherance to the general naming convention of the images.
    #if the input_file name is ad1.bat, the output_file is graphs/ad1.jpg, and creates the ad graph
    #if the output_file name is overall.bat, the output_file is graphs/overall.jpg, and creates the overall graph
    #assumes input_file is in temp folder
    #outputs to images/

    file_name = input_file[0:input_file.index(".")]
    ad_number = file_name[len(file_name) - 1:len(file_name)]

    #the specific properties of the dat_file script, look below
    dic_ad  = {"graphs/output_file" : file_name + ".jpg", "title" : "Emotions from Advertisement " + str(ad_number), 
        "x_label" : "Image Number", "y_label" : "% Total", "x_max" : 10 , 
        "y_max" : 100, "temp/input_file": file_name + ".dat", 
        "plot_style" : """using 2 t "Contempt" lt rgb "green", '' using 3 t "Disgust" lt rgb "gray", '' using 4 t "Fear" lt rgb "yellow", '' using 5 t "Happiness", '' using 6 t "Neutral", '' using 7 t "Sadness", '' using 8 t "Surprised"
        """
    }

    dic_overall = {"graphs/output_file" : file_name + ".jpg", "title" : "Emotions from all the Advertisements", 
        "x_label" : "Advertisement Number", "y_label" : "Number of Images", "x_max" : "auto" , 
        "y_max" : "auto", "temp/input_file": file_name + ".dat", 
        "plot_style" : """using 2 t "Happy" lt rgb "green", '' using 3 t "Sad" lt rgb "gray", '' using 4 t "Surprised" lt rgb "yellow" """
    }

    #there are two dics to use, specify the one to use here
    dic = dic_ad
    if file_name.lower() == "overall":
           dic = dic_overall

    #the generalized dat file giving a bar graph look. Change the qualities of the script with the dictionary files above
    dat_file = Template("""
    set terminal jpeg giant font "Helvetica" 16
        
    set output '$output_file'
    set key right
    set grid y
    
    set style data histogram
    set style histogram rowstacked
    set style fill solid
    set border 3
    set boxwidth 0.6
    
    set title '$title'
    set ylabel '$y_label'
    set xlabel '$x_label'
    set xtics 1
    
    set xrange [0.5:$x_max]
    set yrange [0:$y_max]
    
    plot "$input_file"\
            $plot_style
    """).substitute(dic)
    
    #Writes the dat_file code into a script
    gnuplot_name = "temp/" + file_name + ".gnuplot"
    script = open(gnuplot_name, 'w')
    script.write(dat_file)
    script.close()

    #execute the script
    os.system("gnuplot -e \"filename=\'" + dic["input_file"] + "\'\" " + gnuplot_name)
    os.system("rm " + gnuplot_name)




