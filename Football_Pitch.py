import matplotlib.pyplot as plt

def draw_football_pitch(l=120, w=80):
    plt.axes()

    pitch = plt.Rectangle((0, 0), l, w, fc='green', ec='white')
    plt.gca().add_patch(pitch)

    half_yard_line = plt.Line2D([l // 2, l // 2], [w, 0], color='white', lw=1)
    plt.gca().add_line(half_yard_line)

    center_circle = plt.Circle((l // 2, w // 2), 10, fc='green', ec='white')
    plt.gca().add_patch(center_circle)

    left_d = plt.Rectangle((0, (w - 44) // 2), 18, 44, fc='green', ec='white')
    plt.gca().add_patch(left_d)

    left_six_yard_box = plt.Rectangle((0, (w - 20) // 2), 6, 20, fc='green', ec='white')
    plt.gca().add_patch(left_six_yard_box)

    right_d = plt.Rectangle((l - 18, (w - 44) // 2), 18, 44, fc='green', ec='white')
    plt.gca().add_patch(right_d)

    right_six_yard_box = plt.Rectangle((l - 6, (w - 20) // 2), 6, 20, fc='green', ec='white')
    plt.gca().add_patch(right_six_yard_box)
    
    #left_penalty_spot
    plt.plot(12, w // 2,'wo', ms=2)
    
    #right_penalty_spot
    plt.plot(l - 12, w // 2,'wo', ms=2)
    
    #center spot
    plt.plot(l // 2, w // 2,'wo', ms=2)
