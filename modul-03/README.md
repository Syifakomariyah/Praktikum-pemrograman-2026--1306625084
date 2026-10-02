# Modul [03] - [Trigonometri]

**Nama:** [Nama : Syifa Komariyah Septi Ningsih]  
**NIM:** [NIM : 1306625084]  
**Kelas:** [Kelas : Fisika C]  

---

## 1. Problem Statement
> Membuat program untuk menghitung nilai sin dan cos dengan pendekatan deret Mc Laurin

## 2. Mathematical Equation
    a. Deret Mclaurin untuk sinus:
>$$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n \, x^{2n+1}}{(2n+1)!}$$
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$  
    b. Deret Mclaurin untuk cos:
>$$\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n \, x^{2n}}{(2n)!}$$
>$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$$
    c. Rumus Relative Error (Er):
>$$E_r = \left| \frac{x_{\text{approx}} - x_{\text{true}}}{x_{\text{true}}} \right|$$
>$$E_r = \left| \frac{x_{\text{approx}} - x_{\text{true}}}{x_{\text{true}}} \right| \times 100\%$$

## 3. Algorithm
> Mulai
> print("Program Trigonometri")
> print("Nama : Syifa Komariyah")
> print("NIM : 1306625084")
> 
