---




---

[TOC]

# Problems that can be solved via linear algebra

## 1. Simultaneous equations

I bought two apples and thee bananas for eight dollars, the i bought ten apples and one banana for 13 dollars. What is the cost of one banana and one apple?

```math
SIMULTANEOUS EQUATIONS

2a + 3b = 8
10a + 1b = 13
```

![https://i.kym-cdn.com/entries/icons/original/000/021/256/horse_algebra_question.jpg](https://i.kym-cdn.com/entries/icons/original/000/021/256/horse_algebra_question.jpg)



* It's useful to have a computer algorithm that solves that in the general case



We got coefficients `2, 3, 10, 1`, input variables `a, b` and output `8, 13`

This can be written as matrix and vector operations:

$$\begin{pmatrix} 2, 3 \\ 3, 4\end{pmatrix} * \begin{bmatrix} a \\ b\end{bmatrix} = \begin{bmatrix} 8 \\ 13\end{bmatrix}$$



## 2. Fit a equation to data

![image-20200122181204854](01.assets/image-20200122181204854.png)

How to pick best parameters that will generate a curve that best describes the histogram's data?

# Vectors

![Resultado de imagem para linear algebra memes"](01.assets/images.jpeg)

![image-20200122181514826](01.assets/image-20200122181514826.png)

Find the equation

* The equation will have two parameters, the center of the distribution ($\mu$) and how wide it is ($\sigma$) 



![image-20200122181728030](01.assets/image-20200122181728030.png)



**Equation:** normal or Gaussian distribution



**How to guess $\mu$ and $\sigma$**



![image-20200122181840769](01.assets/image-20200122181840769.png)



Use the over-fits and under-fits to say how good the values are. Plot the variables and measure the difference between the goodness and badness.

![image-20200122201317598](01.assets/image-20200122201317598.png)

> In the center we got the point of best possible fit - a parameter space. Changing $\mu$ or $\sigma$ can get us near this point

If i do move a little bit in some direction, my results get better? This movement can be imagined as a vector that changes  the variables.

![image-20200122201457010](01.assets/image-20200122201457010.png)

Knowing the direction to aim will end the search for the best parameters earlier

With vectors and calculus we can make little moves towards the center, finding the best possible fit. 

**Downhill** problems



# Vectors carry information

A vector is a list, a list can carry all information about something. A car for example:

![image-20200122202150169](01.assets/image-20200122202150169.png)



With three parameters we can imagine a landscape map, finding the answer to what are the best values for this parameters (minimizing them) would seem like walking trough this landscape towards the bottom of the hills to find the lowest point in this landscape.

# More concepts on vectors

![Resultado de imagem para shadow -motor"](01.assets/images-1580592672138.jpeg)

* **Length** or **size**
* **Dot** product or inner scalar **projection product**



Independently of the coordinate system used, a vector has two properties: its **size** and **direction**

![image-20200122204018790](01.assets/image-20200122204018790.png)



If the coordinate system consists in two orthogonal unit vectors:

![image-20200122204151002](01.assets/image-20200122204151002.png)

![image-20200122204225254](../../../image-20200122204225254.png)

The hat denotes size one



**from Pythagoras**

![image-20200122204353148](01.assets/image-20200122204353148.png)



# Dot product - multiplying two vectors together

![image-20200122204503194](01.assets/image-20200122204503194.png)



![image-20200122204533766](01.assets/image-20200122204533766.png)

![image-20200122204606868](01.assets/image-20200122204606868.png)



## Properties

### Commutative

$r \cdot s = s \cdot r$

The way of the dot product doesn't changes the result

### **Distributive** over addition

$ r \cdot (s + t) = r \cdot s + r \cdot t $

![image-20200122204958673](01.assets/image-20200122204958673.png)



### **Associativity** over multiplication

$r \cdot (a*S) = a (r \cdot s)$

$a$ is a scalar





**Derived properties**

![image-20200122205521302](01.assets/image-20200122205521302.png)

This gives you the size of the vector



# Cosine dot product

On school math

![image-20200122205638893](01.assets/image-20200122205638893.png)

On vector notation

![image-20200122205709034](01.assets/image-20200122205709034.png)

![image-20200122205939972](01.assets/image-20200122205939972.png)



> The **dot product** gets the size of the two vectors and multiplies by the cosine of the angle between them - it tells us something about the extent to which the two vector got in the same direction

![image-20200122211520597](01.assets/image-20200122211520597.png)



![image-20200122211543369](01.assets/image-20200122211543369.png)



## Projection

![image-20200123132623803](01.assets/image-20200123132623803.png)

![image-20200123132656956](01.assets/image-20200123132656956.png)

![image-20200123133509137](01.assets/image-20200123133509137.png)





![image-20200123133546364](01.assets/image-20200123133546364.png)



# Changing basis

![image-20200123134003580](01.assets/image-20200123134003580.png)

![image-20200123134036470](01.assets/image-20200123134036470.png)





![image-20200123134134263](01.assets/image-20200123134134263.png)



### How to represent $r$ in terms of $b_1$ and $b_2$?

* **IF the angle between the unit vectors of the new base is $90°$ (ORTHOGONAL to each other)**
  * Then the projection or dot product can be used to do the transformation
  * Using the orthogonal representation makes computations much easier and faster



![image-20200123162933542](01.assets/image-20200123162933542.png)



**If the new basis vector aren't orthogonal, the dot product can't be used for changing from one basis to another, matrices and matrix operations will be used instead**



# Basis, vector space and linear independence

###  Basis

* A base is a set of $n$ vectors that
  * Are not linear combinations of each other (**linearly independent**)
    * I can't write any of them using a combination of the other ones
  * Span the space they describe
    * The space is then *n-dimensional*

**linearly independent**

![image-20200123163439426](01.assets/image-20200123163439426.png)

It must be impossible to sum two vectors and get the third



In linear algebra, the space can't be warped or folded, all transformations to one base from another keeps the vector space being a regularly spaced grid.



![image-20200123163852089](01.assets/image-20200123163852089.png)



The vector rules will hold if the grid is always regularly spaced - things can be stretched, sheared, inverted or rotated, but linear combinations still work.



# Basis change applications 😮🤯

1. We got a set of 2D data points

![image-20200123164758626](01.assets/image-20200123164758626.png)

2. The points can be more or less described by a line (linear regression ;) 

![image-20200123164917436](01.assets/image-20200123164917436.png)

3. Now we can imagine mapping the data from the $x,y$ plane onto the line, the new $x$ would be how far the line goes and the new $y$ would indicate the distance from the points to the line, in other words, the noisiness of the data.

![image-20200123165159374](01.assets/image-20200123165159374.png)

4. The noise dimension tells how good the fit is.

![image-20200123180410976](01.assets/image-20200123180410976.png)

5. Both coordinate system uses orthogonal basis vectors, the dot-product can be used to map the points between them - projecting from x, y to line, noisiness



> A neural network that identifies faces, for example, could apply some transformation to the pixel data, putting it into a new basis that describes the nose shape, skin hue, eye distance - the real work of the neural network will be to somehow derive a set of basis vector that extract the most information-rich features of faces





A neural network could identify a face by deriving the best features from an image, creating basis vectors that extracts the most rich features of the faces.



https://www.youtube.com/watch?v=LyGKycYT2v0

<iframe width="1908" height="807" src="https://www.youtube.com/embed/LyGKycYT2v0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# Matrices, vectors and solving simultaneous equations

![Resultado de imagem para matrix"](01.assets/images-1580592560979.jpeg)

## Price discovery



The following equation



$$2a + 3b = 8$$

$$10a + 1b = 13$$



Can be represented as



$$\begin{pmatrix} 2, 3 \\ 10, 1\end{pmatrix}  \begin{bmatrix} a \\ b\end{bmatrix} = \begin{bmatrix} 8 \\ 13\end{bmatrix}$$



$$\begin{pmatrix} 2a + 3b \\ 10a + 1b\end{pmatrix} = \begin{bmatrix} 8 \\ 13\end{bmatrix}$$



![image-20200124160347574](01.assets/image-20200124160348317.png)





# How matrices transform space

* The grid stays evenly spaced for any transformation
* The origin doesn't move
* The vector sum still works on the transformed space



![image-20200128170930674](01.assets/image-20200128170930674.png)



> We can think about matrix multiplication as just being the **multiplication** of the **vector sum** of the **transformed basis vectors**
>
> The transformation tell us to where the **basis vector** goes



# Types of matrix transformation

![](01.assets/giphy.gif)

https://www.geogebra.org/m/dcnBMXhN



## Identity matrix

Multiplying by the basis vectors doesn't change the vector - this is called the **identity matrix**, represented by $I$

![image-20200128171321901](01.assets/image-20200128171321901.png)

## Changing the diagonal values

### Positive case

The basis vectors get bigger or smaller - space gets scaled

![image-20200128171552060](01.assets/image-20200128171552060.png)

The unit square can be a square or a rectangle

![image-20200128171710882](01.assets/image-20200128171710882.png)

### Fractions

The basis vectors would get squished



### Negative case

![image-20200128171848723](01.assets/image-20200128171848723.png)

The basis vectors will flip to the other side

![image-20200128171931019](01.assets/image-20200128171931019.png)



**Inverting both axis**

![image-20200128172022053](01.assets/image-20200128172022053.png)

That is called an **inversion**

### Mirroring

![image-20200128172137985](01.assets/image-20200128172137985.png)





![image-20200128172803693](01.assets/image-20200128172803693.png

![image-20200128173301783](01.assets/image-20200128173301783.png)

![image-20200128173313244](01.assets/image-20200128173313244.png)

![image-20200128173320933](01.assets/image-20200128173320933.png)

![image-20200128173332570](01.assets/image-20200128173332570.png)

![image-20200128174310085](01.assets/image-20200128174310085.png)

### Shears

![image-20200128174339485](01.assets/image-20200128174339485.png)

![image-20200128174350854](01.assets/image-20200128174350854.png)

### Rotations

**By 90 deg**

 

![image-20200128174553262](01.assets/image-20200128174553262.png)



**by any angle $\theta$**

![image-20200128174631419](01.assets/image-20200128174631419.png)

# Composition or combination of matrix transformations

![](https://media.giphy.com/media/MY6LrEW1m6rgA/giphy.gif)

$$A_2(A_1(r))$$



* $A_1$ is a $90 \deg$ rotation counterclockwise
  * ![image-20200128174930823](01.assets/image-20200128174930823.png)

* $A_2$ is a vertical mirror
  * ![image-20200128175125861](01.assets/image-20200128175125861.png)



The result is

![image-20200128175147868](01.assets/image-20200128175147868.png)



To solve it without needing to draw

![image-20200129192529963](01.assets/image-20200129192529963.png)

![image-20200129192647041](01.assets/image-20200129192647041.png)



# Gaussian Elimination

![](01.assets/giphy-1580593099304.gif)

![](01.assets/giphy-1580593147535.gif)

**Inverse matrix**: given a matrix $A$, its inverse ($A^{-1}$) is the matrix that when multiplied by $A$ gives the **identity matrix** ($I$) as the result

## Apples and Bananas problem



![image-20200129192901237](01.assets/image-20200129192901237.png)



1. Multiplying an matrix by its inverse gives the identity matrix as the result
2. The identity matrix is the matrix that does not change the vector $r$
3. Multiplying both sides of the equation by the inverse, we can change
   1. $A^{-1}A = I$
   2. $I$ can be simply removed, since it does not change the result
4. Then, finding the inverse of $A$, can lead us to the result



It's easier to solve this specific problem just by substitutions. A more complex problem:



![image-20200129194409306](01.assets/image-20200129194409306.png)

This problem can be solved via a process of elimination by subtracting the first row from the other ones

![image-20200129194946668](01.assets/image-20200129194946668.png)

The matrix is **triangular**: everything below the body diagonal is zero = "*Echelon Form*"



Then, the problem can be solved by subtracting rows from each other and substituting the rows with known answers until the answer is found

![image-20200129195236889](01.assets/image-20200129195236889.png)



**We didn't need to compute the inverse, but, we solved this problem only yo this specific output $s$ ($A \cdot r = s$) - CALCULATING THE INVERSE MATRIX WE COULD SOLVE IT TO ANY $s$**

   

![image-20200129195556427](01.assets/image-20200129195556427.png)

In solving this problem we end up with the identity matrix

# From Gaussian elimination to the inverse matrix

![image-20200129195858707](01.assets/image-20200129195858707.png)

![image-20200129200003191](01.assets/image-20200129200003191.png)

Can be solved by elimination and back substitution for each column of $B$ - **but it can be done to all rows at the same time**



Subtracting from the first row

![image-20200129200231028](01.assets/image-20200129200231028.png)

Multiplying the third row by $-1$ 

![image-20200129200335351](01.assets/image-20200129200335351.png)

Substituting by the last row - note that we are multiplying by $3$ to get $0$ on the first row

![image-20200129200500402](01.assets/image-20200129200500402.png)



![image-20200129200617459](01.assets/image-20200129200617459.png)

![image-20200129201957138](01.assets/image-20200129201957138.png)

# Determinant and inverses

![image-20200129202533228](01.assets/image-20200129202533228.png)

**General case**

![image-20200129202624645](01.assets/image-20200129202624645.png)

![image-20200129202951022](01.assets/image-20200129202951022.png)

![image-20200129203012400](01.assets/image-20200129203012400.png)



**For a 2 x 2**

![image-20200129203549165](01.assets/image-20200129203549165.png)





----

![image-20200129203744751](01.assets/image-20200129203744751.png)

* Both basis vectors are points in the same line
* They are multiples
* They aren't linearly independent

 

**The determinant is $0$** - because the area is zero

$|A| = 0$



In a **3x3** if one of the new basis vectors is a linear multiple of the other two (not linearly independent)

* It's a line or a plane
* The volume is zero
* The determinant is zero

![image-20200129204230840](01.assets/image-20200129204230840.png)



Reduce to **echelon form**

![image-20200129204317278](01.assets/image-20200129204317278.png)

$C$ can be just any number - there is no enough information to solve the problem



In the apples in bananas problem, it would be like you have bought just the sum of the last two days



The matrix **has no determinant**, therefore, there is no **inverse** - it would be great if we could **collapse** the number of dimensions to two

- That comes with a cost - some information is lost - **the transformation can't be undone**



# Einstein Summation conversion and dosimetry of the dot product



![image-20200131162600409](01.assets/image-20200131162600409.png)



![image-20200131162618033](01.assets/image-20200131162618033.png)

![image-20200131162654818](01.assets/image-20200131162654818.png)



![image-20200131162810106](01.assets/image-20200131162810106.png)

Can be multiplied if the number of $j$ is the same



![image-20200131162927665](01.assets/image-20200131162927665.png)



![image-20200131162955061](01.assets/image-20200131162955061.png)



**PROJECTION IS THE DOT PRODUCT**

# Changing Basis

![image-20200131163401224](01.assets/image-20200131163401224.png)



Bears basis vectors $$\begin{bmatrix} 3 \\ 1\end{bmatrix}$$, $$\begin{bmatrix} 1 \\ 1\end{bmatrix}$$ in **my** frame

Therefore, the transformation matrix is:

$$\begin{bmatrix} 3  ~~ 1\\ 1 ~~ 1\end{bmatrix}$$

Taking a vector in the bears perspective

$$\begin{bmatrix} 3  ~~ 1\\ 1 ~~ 1\end{bmatrix}\begin{bmatrix} 3\over2\\ 1\over2\end{bmatrix} = \begin{bmatrix} 5\\ 2\end{bmatrix}$$

![image-20200131164109761](01.assets/image-20200131164109761.png)

Transforms bears vectors into my world - how to reverse this process? - **the inverse!**



![image-20200131164408133](01.assets/image-20200131164408133.png)





## Using projections

If both basis vectors are orthogonal 



# Transformation of transformed vectors

![image-20200131173610351](01.assets/image-20200131173610351.png)

How to write a $45\deg$ rotations in bear's perspective?

![image-20200131173705071](01.assets/image-20200131173705071.png)

1.  Transform to my coordinate frame
2. Apply the transformation
3. Transform back



$$B^{-1} R B = R_B$$

![image-20200131173907422](01.assets/image-20200131173907422.png)



# Orthogonal Matrices

## Transpose $A_{(i,j)}^T = A_{(j,i)}$

![image-20200131174231205](01.assets/image-20200131174231205.png)



If they are orthogonal and are the basis vectors

Is another orthogonal basis set



$A^T \cdot A = A^TA = the~identity~matrix$ 

$A^TA = I$

![image-20200131174540138](01.assets/image-20200131174540138.png)

The determinant is $+1$ or $-1$



**In data science**

* Wherever possible we ant to use an **orthonormal** basis vector set when we transform our data

  * Our transformation matrix to be an orthogonal matrix

* Then

  * The inverse is easy to compute
  * The transformation is reversible (we are not collapsing space) 
  * The projection is the dot product
  * Arranging the basis vectors in the right order, the determinant will be $1$ or $-1$ - its easy to change a pair and make the determinant to be $1$ rather then $-1$
  * Heaven, nice, pleasant and easy

  



# The Gram Schmidt process

Live is much easier if we can construct an *orthonormal* basis vector set - **how to do it?**



Taking (and linearly independent) basis vectors set: $b = \{v_1, v_2, ..., v_n\}$

They're not:

* Orthogonal to each other
* Are not of unit length

**Remember:** not linearly independent if the determinant is $0$

**Gram-Schmidt Process** - transforms it to orthonormal



* Normalization of one vector to be of unit length $e_1 = \frac{v_1}{|v_1|}$

![image-20200201183749959](01.assets/image-20200201183749959.png)

* $v_2$ will have a component in the direction of $v_1$ plus a component perpendicular to it

  

  $$v_2 = (v_2 \cdot e_1) \frac{e_1}{|e1|}$$

  $$v_2 = (v_2 \cdot e_1) \frac{e_1}{1}$$

  $$v_2 = (v_2 \cdot e_1)\ e1$$

  $$v_2 = v_2 - (v_2 \cdot e_1)\ e1$$

  

  

  

  ![image-20200201183900488](01.assets/image-20200201183900488.png)

  ![image-20200201184140961](01.assets/image-20200201184140961.png)

  ![image-20200201184148511](01.assets/image-20200201184148511.png)

  

  

  

* $v_3$ - project on the plane

$$v_3 = v_3 - (v_3 \cdot e_1) e_1 - (v_3 \cdot e_2) e_2$$



Normalizing

$$\frac{v3}{|v3|}=e_3$$



# Mirror example

![image-20200201184943409](01.assets/image-20200201184943409.png)

1. Doing the Gram-Schmidt process



![image-20200201185003644](01.assets/image-20200201185003644.png)

![image-20200201185059222](01.assets/image-20200201185059222.png)



![image-20200201185212956](01.assets/image-20200201185212956.png)



![image-20200201185228177](01.assets/image-20200201185228177.png)





![image-20200201185308918](01.assets/image-20200201185308918.png)





![image-20200201185521806](01.assets/image-20200201185521806.png)

The answer is in the basis of the plane's vector set



![image-20200201185718660](01.assets/image-20200201185718660.png)

![image-20200201185736017](01.assets/image-20200201185736017.png)





![image-20200201185914120](01.assets/image-20200201185914120.png)



![image-20200201190001132](01.assets/image-20200201190001132.png)



# Eigenvalues and eigenvectors

![](01.assets/giphy-1580593510758.gif)

**Eigen** - German for *"characteristic"*

* Related to: *what happens to **all** vector in space when a transformation is applied?*



![image-20200201190527864](01.assets/image-20200201190527864.png)



![image-20200201190533272](01.assets/image-20200201190533272.png)

**Note:** 

* *Direction and length* - some vectors are scaled, but their still pointing in the same direction
* The angle of the diagonal vector has increased
* Just the **horizontal** and **vertical** vectors will keep its direction, any other vector will be pointing to a different direction after the transformation - they are **special**
  * They are a characteristic of this transform
  * They are called ==eigenvectors==
  *  The length of the **horizontal** one does not changed, its ==eigenvalue== is $1$
  * The length of the **vertical** one doubled, therefore, its ==eigenvalue== is $2$



**Key concept:** 

* Find the vectors whose the span (direction of pointing) does not changed after a transformation
* Then, measure how much they have grown or shrieked





![image-20200201191339264](01.assets/image-20200201191339264.png)

**Pure shear**: the horizontal vector



![image-20200201191429872](01.assets/image-20200201191429872.png)

**Rotation**: all changed - no eigenvectors 





# Eigenvalues and eigenvectors - special cases

## Uniform scaling

![image-20200201191621823](01.assets/image-20200201191621823.png)

![image-20200201191627518](01.assets/image-20200201191627518.png)

**ANY VECTOR IS AN ==EIGENVECTOR==**



## Rotation

![image-20200201191653279](01.assets/image-20200201191653279.png)



![image-20200201191827350](01.assets/image-20200201191827350.png)

**ONLY IN ROTATIONS OF $180°$** - the vectors lay on the same line, but point to the opposite direction

So the eigenvalues are $-1$



## Horizontal shear & vertical scaling

![image-20200201191928421](01.assets/image-20200201191928421.png)

![image-20200201191937732](01.assets/image-20200201191937732.png)





This transformation has two eigenvectors - the green one and the white one

![image-20200201192030052](01.assets/image-20200201192030052.png)

>  Eigenvectors are not so easy to spot...

Applying the inverse

![image-20200201192109411](01.assets/image-20200201192109411.png)



## In 3D

![image-20200201192146717](01.assets/image-20200201192146717.png)

![image-20200201192150631](01.assets/image-20200201192150631.png)

The eigenvector of rotation also tells the axis of rotation - in rotation in 3D



# Calculating eigenvectors

Eigenvector $x$

Transformation $A$

$$Ax = \lambda x$$ 

$\lambda$ is just a number



Target: *find values of $x$ that makes both sides equal*

![image-20200201195658877](01.assets/image-20200201195658877.png)

![image-20200201195711328](01.assets/image-20200201195711328.png)

**EXAMPLE**

![image-20200201195743333](01.assets/image-20200201195743333.png)

![image-20200201195818348](01.assets/image-20200201195818348.png)

![image-20200201195906839](01.assets/image-20200201195906839.png)

![image-20200201195937238](01.assets/image-20200201195937238.png)

# Eigenvectors as basis - basis change

 

![image-20200201201855237](01.assets/image-20200201201855237.png)

![image-20200201201927622](01.assets/image-20200201201927622.png)

![image-20200201201950111](01.assets/image-20200201201950111.png)



![image-20200201202034383](01.assets/image-20200201202034383.png)



  # Eigenbasis example

![image-20200201202126750](01.assets/image-20200201202126750.png)

![image-20200201202150719](01.assets/image-20200201202150719.png)

![image-20200201202210865](01.assets/image-20200201202210865.png)

![image-20200201202308942](01.assets/image-20200201202308942.png)

![image-20200201202332030](01.assets/image-20200201202332030.png)



![image-20200201202410160](01.assets/image-20200201202410160.png)



![image-20200201202449286](01.assets/image-20200201202449286.png)



## Eigenbasis approach



![image-20200201202509224](01.assets/image-20200201202509224.png)

![image-20200201202533421](01.assets/image-20200201202533421.png)



![image-20200201202817584](01.assets/image-20200201202817584.png)



# PageRank

* The importance of a site is related to its links from and to other sites



![image-20200201203012017](01.assets/image-20200201203012017.png)



Using a procrastinator - a imaginary person that will randomly clicks in links from one site to the other

Goal - to make a model that  shows how many time the imaginary person spent in each site

![image-20200201203247157](01.assets/image-20200201203247157.png)

Normalizing

![image-20200201203330720](01.assets/image-20200201203330720.png)



The problem is self referential - the probability to end up in one page depends on the probability to get in the others



**Solving for page A**

Needed to be known for every page in the Internet

* What is your rank?
* How many links yo A do you have?
* How many outgoing links do you have in total?





![image-20200201203636253](01.assets/image-20200201203636253.png)



Write this to all pages and solve it for all of them

The problem will be iteratively solved until convergence



## Damping factor

![image-20200201204024389](01.assets/image-20200201204024389.png)

Probability of typing the address instead of clicking a link

Helps to find a compromise between speed and good results - efficiency



