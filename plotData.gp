#!/usr/bin/gnuplot

reset

# png
set terminal pngcairo size 800,600 enhanced font 'Verdana,10'
set output 'Collatz_steps.png'

# color definitions
#set border linewidth 1.5
set style line 1 lc rgb '#0060ad' pt 5 ps 0.5 lt 1 lw 1 # --- blue

set xrange [0:10000]
set yrange [0:261]

plot 'steps_data.txt' using 1:2 pt 7 ps 0.1
