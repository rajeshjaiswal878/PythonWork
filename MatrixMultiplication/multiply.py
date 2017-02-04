import MapReduce
import sys

"""
Title:Matrix multiplication in the Simple Python MapReduce Framework
Dated:4th feb 2017
Name: XYZ
"""

'''
map_reduce is an object of class MapReduce
'''
map_reduce = MapReduce.MapReduce()


def mapperfunction(record):
    matrixname = record[0]
    if matrixname == 'a': #chnage matrix name according to your input file if 'A' mentioned in value
        map_reduce.storematrixvalue(matrixname, [record[1], record[2], record[3]])
    else:
        map_reduce.storematrixvalue(matrixname, [record[2], record[1], record[3]])


def reducerfunction(matrixname, list_of_values):
    a={}  #Intialize matrix a with null values
    b={}  #Intialize matrix b with null values
    if matrixname == 'a': #chnage matrix name according to your input file if 'A' mentioned in value
        for v in list_of_values:
            a[(v[0], v[1])] = v[2]
        for r in map_reduce.intermediate['b']:
            b[(r[0], r[1])] = r[2]
        '''
        Through this loop will handlle missing value and replace them with 0
        '''
        for i in range(0, C1):
            for j in range(0, C1):
                if (i, j) not in a.keys():
                    a[(i, j)] = 0
                if (j,i) not in b.keys():
                    b[(j, i)] = 0
        result = 0

        '''
        Here We are going to compute Actual multiplication both Matrix
        '''

        for i in range(0, C1):
            for j in range(0, C1):
                for k in range(0, C1):
                    result += a[(i, k)]*b[(j, k)]
                map_reduce.display((i, j, result))
                result = 0
'''
This is main function of this python program
R1,C1 is the 1st Matrix dimension(Row by Column)
R2,C2 is the 2nd Matrix dimension(Row by Column)

Will do multiplication only if column count of 1st matrix(C1) is equal to the row count of 2nd Matrix i.e(C2==R1)

Ways to pass matrix value in command line:
1)python multiply.py R1 C1 R2 C2 datafilename

'''

if __name__ == '__main__':
    R1 =int(sys.argv[1])
    #print("1st Matrix rowcount:"+R1)
    C1 = int(sys.argv[2])
    #print("1st Matrix column-count:"+C1)
    R2 = int( sys.argv[3])
    #print("2nd Matrix rowcount:"+R2)
    C2 = int(sys.argv[4])
    #print("2nd Matrix column-count:"+C2)
    inputdata = open(sys.argv[5])
    if(C1==R2):
        print ("Resultant Matrix will be of:")
        print (C1)
        print ("by")
        print (R2)
        map_reduce.multiplication(inputdata, mapperfunction, reducerfunction)
    else:
        print("1st Matrix column count: C1 and 2nd Matrix Row count:R2 Not equal so Multiplication is not Possible")