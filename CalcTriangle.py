import math

def triangle_area_by_sides(a, b, c):
    # 计算三角形面积，已知三边长度
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def triangle_area_by_sas(a, b, angle_c, angle_unit='radians'):
    # 计算三角形面积，已知两边和一个角
    if angle_unit == 'degrees':
        angle_c = math.radians(angle_c)
    area = 0.5 * a * b * math.sin(angle_c)
    return area

def triangle_area_by_base_height(base, height):
    # 计算三角形面积，已知底和高
    area = 0.5 * base * height
    return area

def is_right_angle_triangle(a, b, c):
    # 判断是否为直角三角形
    sides = sorted([a, b, c])
    return abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < 1e-9

def main():
    print("请选择输入模式：")
    print("1. 输入三边计算面积")
    print("2. 输入两条边和夹角计算面积")
    print("3. 输入底和高计算面积")
    print("4. 输入两角一边计算面积")
    print("5. 输入两条边和一角计算面积，该角不是夹角")
    choice = int(input())

    if choice == 1:
        a = float(input("请输入三角形第一条边的长度："))
        b = float(input("请输入三角形第二条边的长度："))
        c = float(input("请输入三角形第三条边的长度："))
        if a+b>c and a+c>b and b+c>a:
            area = triangle_area_by_sides(a, b, c)
        else:
            print("错误，输入三条边无法构成三角形！")
            return
        
    elif choice == 2:
        a = float(input("请输入三角形第一条边的长度："))
        b = float(input("请输入三角形第二条边的长度："))
        angle_unit = input("忽略大小写，角度输入使用弧度制不使用π(默认)，还是弧度制使用π(radians)，还是角度值(degrees)？:")

        if angle_unit == 'degrees':
            angle_c = float(input("请输入三角形夹角的度数："))
            # 确保输入角度在正确范围内
            if angle_c <= 0 or angle_c >= 180:
                print("角度值输入应在(0, 180)之间！")
                return
            area = triangle_area_by_sas(a, b, angle_c, angle_unit)
            
        elif angle_unit == 'radians':
            angle_c = float(input("请输入三角形夹角的弧度值nπ中的n："))
            if angle_c <=0 or angle_c >=1:
                print("弧度值nπ输入应在(0, 1)之间！")
                return
            
            area = triangle_area_by_sas(a, b, math.pi * angle_c, angle_unit)
            
        else:

            angle_c = float(input("请输入三角形夹角的弧度值："))
            # 确保输入角度在正确范围内
            if angle_c <= 0 or angle_c >= math.pi:
                print("弧度值输入应在(0, π)之间！")
                return
            area = triangle_area_by_sas(a, b, angle_c, angle_unit)

        
    elif choice == 3:
        base = float(input("请输入三角形底的长度："))
        height = float(input("请输入三角形高的长度："))
        if base <=0 or height <=0:
            print("底和高输入错误，必须是正数！")
            return
        area = triangle_area_by_base_height(base, height)
    elif choice == 4:
        a = float(input("请输入已知边长a的长度:"))
        angle_type = input("两角的类型是什么？可以是对角+邻角形式，也可以是双邻角形式：(例子：AB/AC是一对角和邻角种，BC是另一种双邻角)")
        if angle_type == "BC" or angle_type == "CB":
            #双邻角B和C
            angle_unit1 = input("忽略大小写，角度输入使用弧度制不使用π(默认)，还是弧度制使用π(radians)，还是角度值(degrees)？:")
            
            if angle_unit1 == 'degrees':
                known_angle1 = float(input("请输入已知角1的度数："))
                known_angle2 = float(input("请输入已知角2的度数："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= 180 or known_angle2 <= 0 or known_angle2 >= 180 or known_angle1+known_angle2>=180:
                    print("角度值输入应在(0, 180)之间。")
                    return
                known_angle1 = math.radians(known_angle1)
                known_angle2 = math.radians(known_angle2)

                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1)) / ( 2* math.sin(known_angle1+known_angle2))  
            elif angle_unit1 == 'radians':
                known_angle1 = float(input("请输入已知角1nπ的n："))
                known_angle2 = float(input("请输入已知角2nπ的n："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= 1 or known_angle2 <= 0 or known_angle2 >= 1 or known_angle1+known_angle2>=1:
                    print("角度值nπ输入应在(0, 1)之间。")
                    return
                known_angle1 = math.pi * known_angle1
                known_angle2 = math.pi * known_angle2

                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1)) / ( 2* math.sin(known_angle1+known_angle2))
            else:
                known_angle1 = float(input("请输入已知角1的弧度值："))
                known_angle2 = float(input("请输入已知角2的弧度值："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= math.pi or known_angle2 <= 0 or known_angle2 >= math.pi or known_angle1+known_angle2>=math.pi:
                    print("弧度值输入应在(0, π)之间。")
                    return
                
                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1)) / ( 2* math.sin(known_angle1+known_angle2))
        elif angle_type == "AB" or angle_type == "BA":
            #邻角B和对角A
            angle_unit1 = input("忽略大小写，角度输入使用弧度制不使用π(默认)，还是弧度制使用π(radians)，还是角度值(degrees)？:")
            
            if angle_unit1 == 'degrees':
                known_angle1 = float(input("请输入已知角A的度数："))
                known_angle2 = float(input("请输入已知角B的度数："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= 180 or known_angle2 <= 0 or known_angle2 >= 180 or known_angle1+known_angle2>=180:
                    print("角度值输入应在(0, 180)之间。")
                    return
                known_angle1 = math.radians(known_angle1)
                known_angle2 = math.radians(known_angle2)

                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1+known_angle2)) / ( 2* math.sin(known_angle1))  
            elif angle_unit1 == 'radians':
                known_angle1 = float(input("请输入已知角A nπ的n："))
                known_angle2 = float(input("请输入已知角B nπ的n："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= 1 or known_angle2 <= 0 or known_angle2 >= 1 or known_angle1+known_angle2>=1:
                    print("角度值nπ输入应在(0, 1)之间。")
                    return
                known_angle1 = math.pi * known_angle1
                known_angle2 = math.pi * known_angle2

                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1+known_angle2)) / ( 2* math.sin(known_angle1)) 
            else:
                known_angle1 = float(input("请输入已知角A的弧度值："))
                known_angle2 = float(input("请输入已知角B的弧度值："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= math.pi or known_angle2 <= 0 or known_angle2 >= math.pi or known_angle1+known_angle2>=math.pi:
                    print("弧度值输入应在(0, π)之间。")
                    return
                
                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1+known_angle2)) / ( 2* math.sin(known_angle1)) 
        elif angle_type== "AC" or angle_type == "CA":
            #邻角C和对角A
            angle_unit1 = input("忽略大小写，角度输入使用弧度制不使用π(默认)，还是弧度制使用π(radians)，还是角度值(degrees)？:")
            
            if angle_unit1 == 'degrees':
                known_angle1 = float(input("请输入已知角A的度数："))
                known_angle2 = float(input("请输入已知角C的度数："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= 180 or known_angle2 <= 0 or known_angle2 >= 180 or known_angle1+known_angle2>=180:
                    print("角度值输入应在(0, 180)之间。")
                    return
                known_angle1 = math.radians(known_angle1)
                known_angle2 = math.radians(known_angle2)

                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1+known_angle2)) / ( 2* math.sin(known_angle1))  
            elif angle_unit1 == 'radians':
                known_angle1 = float(input("请输入已知角A nπ的n："))
                known_angle2 = float(input("请输入已知角C nπ的n："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= 1 or known_angle2 <= 0 or known_angle2 >= 1 or known_angle1+known_angle2>=1:
                    print("角度值nπ输入应在(0, 1)之间。")
                    return
                known_angle1 = math.pi * known_angle1
                known_angle2 = math.pi * known_angle2

                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1+known_angle2)) / ( 2* math.sin(known_angle1)) 
            else:
                known_angle1 = float(input("请输入已知角A的弧度值："))
                known_angle2 = float(input("请输入已知角C的弧度值："))
                # 确保输入角度在正确范围内
                if known_angle1 <= 0 or known_angle1 >= math.pi or known_angle2 <= 0 or known_angle2 >= math.pi or known_angle1+known_angle2>= math.pi:
                    print("弧度值输入应在(0, π)之间。")
                    return
                
                area =  (a*a*math.sin(known_angle2)*math.sin(known_angle1+known_angle2)) / ( 2* math.sin(known_angle1)) 
        else:
            print("输入的angle_type错误，应该输入AB或BC或AC，输入的是：\n")
            print(angle_type)
            return 404
    elif choice == 5:
        a = float(input("请输入已知边长a的长度："))
        b = float(input("请输入已知边长b的长度："))
               
        angle_unit = input("忽略大小写，角度输入使用弧度制不使用π(默认)，还是弧度制使用π(radians)，还是角度值(degrees)？:")
        if angle_unit == 'degrees':
            known_angle = float(input("请输入已知角的度数："))
            
            # 确保输入角度在正确范围内
            if known_angle <= 0 or known_angle >= 180:
                print("角度值输入应在(0, 180)之间。")
                return
            known_angle = math.radians(known_angle)

        if angle_unit == 'radians':
            known_angle = float(input("请输入已知角 nπ的n："))
            
            # 确保输入角度在正确范围内
            if known_angle <= 0 or known_angle >= 1:
                print("角度值nπ输入应在(0, 1)之间。")
                return
            known_angle = known_angle * math.pi
            
        else:
            known_angle = float(input("请输入已知角的弧度值："))
            
            # 确保输入角度在正确范围内
            if known_angle <= 0 or known_angle >= math.pi:
                print("弧度值输入应在(0, π)之间。")
                return
        
        angle_type0 = input("输入角的类型，是边a的邻角还是边b的邻角：(A/B)") 
        # 计算第二个已知角的度数
        if angle_type0 == 'A':
            A = known_angle
            sinBv = b * math.sin(A) / a
            if sinBv == 1:
                area = 0.5 * a * b * math.sin(math.pi / 2 - A)
                return 0
            elif sinBv <= 0 or sinBv >1:
                print("error!")
                return
            else:
                radians_B = math.asin(sinBv)#弧度制
                
                B1 = radians_B
                # 两个可能的角度值
                B2 = math.pi - radians_B
                print("角B的值是")
                print(B1)
                print("或者")
                print(B2)
                print("当是B1时，面积为：")
                area1 = 0.5 * a * b  * math.sin(A+B1)  
                area2 = 0.5 * a * b  * math.sin(A+B2)
                if area1 >=0:
                    print(area1)
                print("当是B2时，面积为：")
                if area2 >=0:
                    print(area2)
                return 0
        elif angle_type0 == 'B':
            B = known_angle
            sinAv = a * math.sin(B) / b
            if sinAv == 1:
                area = 0.5 * a * b * math.sin(math.pi / 2 - B)
                return 0
            elif sinAv <= 0 or sinAv >1:
                print("error!")
                return -1
            else:
                radians_A = math.asin(sinAv)#弧度制
                
                A1 = radians_A
                # 两个可能的角度值
                A2 = math.pi - radians_A
                print("角A的值是")
                print(A1)
                print("或者")
                print(A2)
                
                area1 = 0.5 * a * b  * math.sin(A1+B)  
                area2 = 0.5 * a * b  * math.sin(A2+B)
                if area1 >=0:
                    print("当是A1时，面积为：")
                    print(area1)
                
                if area2 >=0:
                    print("当是A2时，面积为：")
                    print(area2)
                return 0
        else:
            print("无效的角类型输入!")
            print(angle_type0)
            return -3




    else:
        print("无效的选择。")
        return

    print(f"三角形的面积为：{area}")
    return 0

if __name__ == "__main__":
    main()
