<!--     範例 App_51  Markdown         -->

### 
<!--                 
# \[{  \color{Fuchsia}精\;銳\; \color{Purple}矩\;陣\;  \color{Red}計\;算\; \color{Green} 求\;解\;器  }\] 
-->  
![](Images/11-10-01.png) 


<!--         
#### \[{  \color{Fuchsia} 【 \color{Green}  Sharp \; Matrix \; Solver \;  \color{Brown} \iff  \;  \color{Red} S\;M\;S】 }\]  
-->  
![](Images/11-10-02.png)  

---

<!--   
## \[{ \color{Fuchsia} Time-Frequency-Signal \;(Response) \quad Solution  }\] 
-->
![](Images/11-30-01.png)    

 
<!--     ##### \[ using \]   -->
<!--  ![](Images/11-30-07.png)  -->   
##### $$using$$

<!--   
## \[  \color{Red} Precisely \; Numerical \; Value \; Computations  \]  
-->  
![](Images/11-30-02.png) 

  
<!--     ##### \[ with \]   -->   
<!--    ![](Images/11-30-08.png)   -->   
##### $$with$$

<!--   
## \[{ \color{Green} Real \; \color{Red} And \; \color{magenta} Complex \quad \; \color{Brown} Matrix \;\; Transform  }\] 
-->
![](Images/11-30-03.png)  

  
<!--         ##### \[ Part \; 1 \]    -->   
<!--    ![](Images/11-30-09.png)     -->   
##### $$Part \quad 3$$

####

---  

# $$時\quad頻\quad數\quad值\quad計\quad算$$   

### $$Precisely \quad Time-Frequency \quad Numerical \quad Computations$$  

# $$本實例程式碼\quad請參見本儲存庫$$ 

## $$已知實例如下 ：$$

$$y(t) = 
\begin{Bmatrix} 
2 \times t \\\\ 
\cos(10 \times t^2 + 100 \times t) \\\\  
\cos(60 \times t) \\\\ 
\cos(40 \times t) \\\\ 
\cos(t^2 + 20 \times t) \\\\ 
\cos(0.5 \times t^2 + 5 \times t) \\\\ 
1.0 
\end{Bmatrix}
$$ 

### $$條 \quad 件 \quad ： \quad t \geq 0 \quad 且 \quad t \leq \quad 2 \times \pi$$  

##  [參見 : https://www.nature.com/articles/s41588-020-72193-2](https://www.nature.com/articles/s41598-020-72193-2)    

####  https://www.nature.com/articles/s41598-020-72193-2     


#
# $$結\quad論\quad如\quad下：$$

### **1. $\quad$訊號輸出響應值y，參見本儲存庫"時間與振幅圖.pnd"檔案。** 

### **2. $\quad$已知角頻率是時間的變數(Time Variant)。**

### **3. $\quad$參見App_48儲存庫，由微分方程式，求得實數系統矩陣A，再求得複數特徵值矩陣D，和複數特徵向量Q。**  

### **4. $\quad$本實例的頻率為已知，係人工自行設定，是實數但隨時間而變化，故沒有特徵值為複數的狀況。**  

### **5. $\quad$使用Hexp(D, Q, t)轉換矩陣【系由本人推導並以CSharp程式碼撰寫】，惟本實例無須使用到。**

### **6. $\quad$求得多個不同狀態變數的響應值，參見App_6J ... App_48儲存庫中的程式碼**


###  

---  

#

![](Images/name_card.png)  

##
##
