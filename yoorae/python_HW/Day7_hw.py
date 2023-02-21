import matplotlib.pyplot as plt
rhkahr=["Math","English"]
rhkahremf=[85,100]
과목=["Social Study","Science","Korean"]
counts=[80,90,95]
bar_color=["black","black","black","black"]
창,내용=plt.subplots(1,2)
내용[0].bar(rhkahr,rhkahremf,color=bar_color)
내용[1].barh(과목,counts,color=bar_color)
plt.show()