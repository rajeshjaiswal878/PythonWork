import MapReduce
import sys

"""
Compute the matrix multiplication in the Simple Python MapReduce Framework
"""

map_reduce = MapReduce.MapReduce()


def mapper(record):
    matrixname = record[0]
    if matrixname =='a':
      map_reduce.storematrixvalue(matrixname, [record[1], record[2], record[3]])
    else:
      map_reduce.storematrixvalue(matrixname, [record[2], record[1], record[3]])


def reducer(matrixname, list_of_values):

   a={}
   b={}
   if matrixname=='a':

        for v in list_of_values:
            a[(v[0], v[1])]=v[2]  
        for r in map_reduce.intermediate['b']:
            b[(r[0], r[1])]=r[2]  

        for i in range(0,C1):
             for j in range(0,C1):
                  if (i,j) not in a.keys():
                       a[(i,j)]=0
                  if (j,i) not in b.keys():
                       b[(j,i)]=0
        result=0


       #compute the multiplication A*Bij = SUM(Aik * Bkj) for k in 0..4  
        for i in range(0,C1):
             for j in range(0,C1):
                  for k in range(0,C1):
                       result+=a[(i,k)]*b[(j,k)]
                  map_reduce.display((i,j,result))
                  result=0

# Do not modify below this line
# =============================
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
        map_reduce.multiplication(inputdata, mapper, reducer)
    else:
        print("1st Matrix column count: C1 and 2nd Matrix Row count:R2 Not equal so Multiplication is not Possible")