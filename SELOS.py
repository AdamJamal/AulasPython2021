def calculo(RS,PE,PS,QS,QE):

    if(RS==0):
        return int(min(QS,QE))
    else:
        falta=0

        if QS>QE:
            falta=(QS-QE)*PE
        elif QE>QS:
            falta=(QE-QS)*PS

        quantia=RS-falta
        
        if(quantia<0):
            if QS>QE:
                while QS>=QE and RS>0:
                    RS -= PS
                    QE += 1
            elif QE>QS:
                while QE>=QS and RS>0:
                    RS -= PE
                    QS += 1
            return int(min(QS,QE))

        cartas=(RS-falta)//(PE+PS) 
        return int((cartas)+max(QS,QE))
        return calculo(RS,PE,PS,QS,QE)


RS= float(input())
PE = float(input())
PS = float(input())
QS = int(input())
QE = int(input())     
print(calculo(RS,PE,PS,QS,QE))                     