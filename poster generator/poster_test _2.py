# !/usr/bin/env python
'''
gimp poster manipulation
'''
 
 
from gimpfu import *
 
 
def poster_test_2(background,file1, file2, file3, text1,size1,text2,size2,text3,size3):
     gimp.message("Started to process\n")
 
     # make some colors to work with
     bColor = gimpcolor.RGB(250, 10, 10)
     fColor = gimpcolor.RGB(251, 219, 0)
     textColor = gimpcolor.RGB(255,255,255)
 
     gimp.set_background(bColor)
     gimp.set_foreground(fColor)
     gimp.message("Colors setup\n")
 
     # make an empty image and display it
     posterW, posterH = 2480, 3508
     posterImage = gimp.Image(posterW, posterH, RGB)
     gimp.message("poster created\n")
 
     # make the background layer
     backLayer = gimp.Layer(posterImage, "background", posterW, posterH, RGB_IMAGE, 100, NORMAL_MODE)
     posterImage.add_layer(backLayer)

     backgroundImage = pdb.file_png_load(background, background)
     pdb.gimp_image_scale(backgroundImage, posterW, posterH)
     pdb.gimp_edit_copy(backgroundImage.layers[0])
     floatingLayer = pdb.gimp_edit_paste(backLayer, False) # returns a floating selection
     pdb.gimp_floating_sel_anchor(floatingLayer)
     backLayer.update(0, 0, posterW, posterH)


     #pdb.gimp_drawable_fill(backLayer, 1)
     # ??? we can also have gradient background ??? 
     gimp.message("background created\n")
 
     # make the 1st image layer
     layer1 = gimp.Layer(posterImage, "image 1", posterW, 1880, RGBA_IMAGE, 100, NORMAL_MODE)
     posterImage.add_layer(layer1)
 
     image1 = pdb.file_png_load(file1, file1)
     pdb.gimp_image_scale(image1,posterW, 1880)
     pdb.gimp_edit_copy(image1.layers[0])
     floatingLayer = pdb.gimp_edit_paste(layer1, False) # returns a floating selection
     pdb.gimp_floating_sel_anchor(floatingLayer)
     layer1.update(0, 0, posterW, 1880)
 
     #layer1.translate(-posterW/3, -posterH/3)
     gimp.message("layer image 1 created\n")
 
     # make the 2nd image layer
     layer2 = gimp.Layer(posterImage, "image 2", 1600, 1100, RGBA_IMAGE, 100, NORMAL_MODE)
     posterImage.add_layer(layer2)
 
     image2 = pdb.file_png_load(file2, file2)
     pdb.gimp_image_scale(image2, 1600, 1100)
     pdb.gimp_edit_copy(image2.layers[0])
     floatingLayer = pdb.gimp_edit_paste(layer2, False) # returns a floating selection
     pdb.gimp_floating_sel_anchor(floatingLayer)
     layer2.update(0, 0, 1600, 1100)
 
     layer2.translate(0,2400)
     gimp.message("layer image 2 created\n")

     # make the 3rd image layer
     layer3 = gimp.Layer(posterImage, "image 3", 1000, 800, RGBA_IMAGE, 100, NORMAL_MODE)
     posterImage.add_layer(layer3)
 
     image3 = pdb.file_png_load(file3, file3)
     pdb.gimp_image_scale(image3, 1000, 800)
     pdb.gimp_edit_copy(image3.layers[0])
     floatingLayer = pdb.gimp_edit_paste(layer3, False) # returns a floating selection
     pdb.gimp_floating_sel_anchor(floatingLayer)
     layer3.update(0, 0, 1000, 800)
 
     layer3.translate(1480, 2700)
     gimp.message("layer image 3 created\n")
 

     # make 3 text layers
     font = "Arial"
     textLayer1 = pdb.gimp_text_fontname(posterImage, None, 0, 0, text1, 10, True, size1, PIXELS, font)
     textLayer1.translate(50, 1600)

     gimp.set_foreground(textColor) 
     textLayer2 = pdb.gimp_text_fontname(posterImage, None, 0, 0, text2, 10, True, size2, PIXELS, font)
     textLayer2.translate(50, 1850)

     gimp.set_foreground(fColor) 
     textLayer3 = pdb.gimp_text_fontname(posterImage, None, 0, 0, text3, 10, True, size3, PIXELS, font)
     
    
     textLayer3.translate(50, 2300)
    
 
 
     gimp.Display(posterImage)
 
 
 
 
#
 
register(
     "python_fu_poster_test_2",
     "Covid Poster Maker",
     "Covid Poster maker with some interface",
     "Yuan Liu",
     "@MSCIM2021",
     "2021",
     "Covid Poster Maker",
     "",
     [# add input arguments
          (PF_FILE, "background", "Choose background", ""),
          (PF_FILE, "file1", "Choose Image 1", ""),
          (PF_FILE, "file2", "Choose Image 2", ""),
          (PF_FILE, "file3", "Choose Image 3", ""),
          (PF_STRING, "text1", "Title", "Heroes in Harm's way"),
          (PF_SPINNER, "size1", "Font Size", 240, (100, 240, 0)),
          (PF_STRING, "text2", "CopyWrite1", " Every crisis has its heroes. \n Firefighters race into burning buildings. \n Police officers place themselves in the line of fire.\n Soldiers march into war."),
          (PF_SPINNER, "size2", "Font Size", 105, (100, 220, 0)),
          (PF_STRING, "text3", "CopyWrite2", " Now doctors in the world are fighting \n in the front line."),
          (PF_SPINNER, "size3", "Font Size", 140, (100, 220, 0))
          
 
     ],
     [],
     poster_test_2,
     menu = "<Image>/File/CS6102/"
)
 
main()
 
