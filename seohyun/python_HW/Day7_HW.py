import matplotlib.pyplot as plt

subjec=["MATH","ENGLISH"]
counts=[100,50]
subject=["SOCIAL STUDIES","SCIENCE","KOREAN"]
count=[80,30,70]
bar_color=["black"]
창,내용=plt.subplots(1,2)
내용[0].bar(subjec,counts,color=bar_color)
내용[1].barh(subject,count,color=bar_color)
plt.show()