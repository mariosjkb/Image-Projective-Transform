# εισαγωγή χρήσιμων βιβλιοθηκών
import numpy as np
import sys
import cv2
import matplotlib
from PIL import Image
from matplotlib import pyplot as plt

# handler για το γεγονός αριστερού κλικ στην εικόνα
def onMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: # αν ο χρήστης πατήσει αριστερό κλικ στο ποντίκι
        T = [x,y] # τοποθέτηση των συντεταγμένων σε πίνακα
        spots.append(T) # προσθήκη σημείου στον πίνακα σημείων

# εύρεση πλευρών 
def find_sides(spots):
    x_values = [] # πίνακας με τις συντεταγμένες x των σημείων
    right_side = [] # σημεία δεξιάς πλευράς
    left_side = [] # σημεία αριστερής πλευράς
    for i in range(0,len(spots)):
        x_values.append(spots[i][0]) # τοποθέτηση συντεταγμένων χ στον αντίστοιχο πίνακα
    for j in range(0,len(x_values)):
        if j < 2: # οι δυο μικρότερες τιμές συντεταγμένων x θα βρίσκονται στα αριστερά της εικόνας
            x = min(x_values) # εύρεση μικρότερης συντεταγμένης x
            for k in range(0,len(spots)): # εύρεση της συντεταγμένης y που αντιστοιχεί στο x που βρήκαμε πριν
                if x == spots[k][0]:
                    y = spots[k][1]
                    break
            left_side.append([x,y]) # τοποθέτηση σημείου στον πίνακα με τα αριστερά σημεία
            x_values.remove(x) # αφαίρεση ελάχιστης τιμής συντεταγμένης x αφού πλέον δεν την χρειαζόμαστε
        else: # οι δυο μεγαλυτερες τιμές συντεταγμένων x θα βρίσκονται στα δεξιά της εικόνας
            x = min(x_values)  # εύρεση μικρότερης συντεταγμένης x
            for k in range(0,len(spots)):# εύρεση της συντεταγμένης y που αντιστοιχεί στο x που βρήκαμε πριν
                if x == spots[k][0]:
                    y = spots[k][1]
                    break
            right_side.append([x,y])# τοποθέτηση σημείου στον πίνακα με τα δεξιά σημεία
            x_values.remove(x) # αφαίρεση ελάχιστης τιμής συντεταγμένης x αφού πλέον δεν την χρειαζόμαστε
    return [left_side,right_side]

input_filename = sys.argv[1]
output_filename = sys.argv[2]

image = np.array(Image.open(input_filename)) # άνοιγμα εικόνας
spots = [] # σημεία που δοθήκαν από τον χρήστη
left_side = [] # σημεία αριστερής πλευράς
right_side = [] # σημεία δεξιάς πλευράς
up_left_spot = [] # πάνω αριστερό σημείο
down_left_spot = [] # κάτω αριστερό σημείο
up_right_spot = [] # πάνω δεξιά σημείο
down_right_spot = [] # κάτω δεξιά σημείο

# σημείο x1'
x1_output = 0
y1_output = 0

# σημείο x2'
x2_output = 999
y2_output = 0

# σημείο x3'
x3_output = 0
y3_output = 999

# σημείο x4'
x4_output = 999
y4_output = 999


cv2.namedWindow("Image",cv2.WINDOW_NORMAL) # δημιούργησε παράθυρο
cv2.setMouseCallback("Image",onMouse) # bind μεταξύ παραθύρου και handler 
cv2.imshow("Image",image) # προβολή εικόνας
cv2.waitKey(0) # αναμονή για κλικ από χρήστη
cv2.destroyWindow("Image") # καταστροφή παραθύρου

# έλεγχος αριθμού σημείων που δόθηκαν από τον χρήστη
if len(spots) != 4:
    print("4 spots needed.Exiting...")
else:
    sides = find_sides(spots) # εύρεση αριστερών και δεξιών σημείων


    left_side = sides[0] # σημεία αριστερής πλευράς
    right_side = sides[1] # σημεία δεξιάς πλευράς

    # ορισμός ακριβούς θέσης των σημείων με χρήση των διαφορών των συντεταγμενων y
    if left_side[0][1] >= left_side[1][1]: # αν y0 >= y1
        down_left_spot = left_side[0]
        up_left_spot = left_side[1]
    else:
        up_left_spot = left_side[0]
        down_left_spot = left_side[1]
        
    if right_side[0][1] >= right_side[1][1]: # αν y0 >= y1
        down_right_spot = right_side[0]
        up_right_spot = right_side[1]
    else:
        up_right_spot = right_side[0]
        down_right_spot = right_side[1]

    # ορισμός x1 και y1 ως πάνω αριστερό σημείο για λόγους παρουσίασης
    x1 = up_left_spot[0]
    y1 = up_left_spot[1]

    # ορισμός x2 και y2 ως πάνω δεξί σημείο για λόγους παρουσίασης
    x2 = up_right_spot[0]
    y2 = up_right_spot[1]

     # ορισμός x3 και y3 ως πάνω δεξί σημείο για λόγους παρουσίασης
    x3 = down_left_spot[0]
    y3 = down_left_spot[1]

     # ορισμός x4 και y4 ως πάνω δεξί σημείο για λόγους παρουσίασης
    x4 = down_right_spot[0]
    y4 = down_right_spot[1]

    # ορισμός πίνακα συντελεστών που προκύπτει από τον πολλαπλασιασμό των ομογενών συντεταγμένων των δοθέντων σημείων με τον πίνακα προβολικού μετασχηματισμού 
    A = np.array([[x1,y1,1,0 ,0 ,0 ,-x1*x1_output,-y1*x1_output],
                [0 ,0 ,0,x1,y1,1 ,-x1*y1_output,-y1*y1_output],
                [x2,y2,1,0, 0 ,0,-x2*x2_output, -y2*x2_output],
                [0, 0, 0, x2,y2,1,-x2*y2_output,-y2*y2_output],
                [x3,y3,1, 0,0,0,-x3*x3_output,  -y3*x3_output],
                [0,0,0,x3,y3,1,-x3*y3_output,   -y3*y3_output],
                [x4,y4,1,0,0,0,-x4*x4_output,   -y4*x4_output],
                [0,0,0,x4,y4,1,-x4*y4_output,   -y4*y4_output]])
    X = np.zeros((8,1)) # ορισμός πίνακα διαστάσεων 8x1
    b = np.array([x1_output,y1_output,x2_output,y2_output,x3_output,y3_output,x4_output,y4_output]) # ορισμός πίνακα b όπου βρίσκονται οι συντεταγμένες των θέσεων όπου θα τοποθετήσουμε τα νέα σημεία

    # αν η ορίζουσα του πίνακα Α δεν είναι μηδέν τότε υπολόγισε τον αντίστροφο 
    if (np.linalg.det(A) != 0):
        A_inverted = np.linalg.inv(A)
        X = A_inverted @ b # πολλαπλασιασμός αντίστροφου πίνακα με τον πίνακα b για επίλυση του συστήματος
    else:
        X = np.linalg.solve(A,b) # αν η ορίζουσα είναι μηδέν λύση του συστήματος με απαλοιφή Gauss
    
    # ορισμός παραμέτρων για τον πίνακα μετασχηματισμού
    a1 = X[0]
    a2 = X[1]
    a3 = X[2]
    a4 = X[3]
    a5 = X[4]
    a6 = X[5]
    a7 = X[6]
    a8 = X[7]

    # ορισμός πίνακα μετασχηματισμού
    T = np.array([[a1,a2,a3],
                [a4,a5,a6],
                [a7,a8,1]])
    output = cv2.warpPerspective(image,T,(1000,1000)) # εφαρμογή προβολικού μετασχηματισμού στην αρχική εικόνα με τον πίνακα που μόλις υπολογίσαμε

    matplotlib.image.imsave(output_filename,output)
    plt.imshow(output) # εμφάνιση αποτελέσματος
    plt.show() 