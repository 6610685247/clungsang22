#
# FILE: convert_BMI.py
# TASK: convert_BMI
# LANG: PYTHON
# ID:   6610685247
#

unit, m, h = input().split()

m = float(m)
h = float(h)

if 1000 < h or h < 0 or 1000 < m or m < 0:
    print("Error")
else:
    if unit == "i" or unit == "I":  # input value is in imperial unit
        BMI = (m / (h**2)) * 703
    elif unit == "m" or unit == "M":  # input value is in metric unit
        BMI = m / (h**2)

if BMI <= 15:
    print("%.1f" % BMI, "1(Very severely underweight)")
elif 15 <= BMI < 16:
    print("%.1f" % BMI, "2(Serverely underweight)")
elif 16 <= BMI < 18.5:
    print("%.1f" % BMI, "3(Underweight)")
elif 18.5 <= BMI < 25:
    print("%.1f" % BMI, "4(Normal/Healthy weight)")
elif 25 <= BMI < 30:
    print("%.1f" % BMI, "5(Overweight)")
elif 30 <= BMI < 35:
    print("%.1f" % BMI, "6(Obese Class I/Moderately obese)")
elif 35 <= BMI < 40:
    print("%.1f" % BMI, "7(Obese Class II/Severely obese)")
else:
    print("%.1f" % BMI, "8(Obese Class III/Very severely obese)")
