from svmutil import *
y,x = svm_read_problem('scaled')
m = svm_train(y[:400],x[:400],'-c 4')
p_label,p_acc,p_val = svm_predict(y[400:],x[400:],m)
