# Log Day4
今天要做的是把从hand上提取的21个feature~~用解析几何的方法~~分类
如果有图的话可以更清晰，不过现在就先这样写，到之后再改。
最初的想法是用两条直线作为判别标准
5-17和0-5是两条直线
判断的方式是点到距离直线（三角形求高）和点是否在直线同一侧（行列式面积正负性比较）
通过判断指尖和第二指节距离，以及二者是否位于同一侧判断
大拇指和小拇指是否在0-5不同侧，可以判断大拇指是不是伸出去了（五和四的差别在此）
食指指尖距离5-17是否大于食指第二指节距离5-17，可以判断食指是否折起来（三和四的差别在此）
然后，用有几根手指的指尖与5-17距离大于第二指节与5-17距离判断其他数字
以此类推，我们可以构建一个不错的模型。
为了省时间，我写了一个很不美观的if来判断手，然后又写了一个很不美观的if来控制数码管。

