λ = int(input())

if 620 <= λ <= 780:
    c = "Red"
elif 590 <= λ < 620:
    c = "Orange"
elif 570 <= λ < 590:
    c = "Yellow"
elif 495 <= λ < 570:
    c = "Green"
elif 450 <= λ < 495:
    c = "Blue"
elif 425 <= λ < 450:
    c = "Indigo"
elif 380 <= λ < 425:
    c = "Violet"
else:
    c = "Unknown"
print(c)
