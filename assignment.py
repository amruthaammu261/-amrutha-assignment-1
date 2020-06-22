{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Simple Calculator\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "65\n",
      "25\n",
      "2.25\n",
      "900\n",
      "5\n",
      "1159445329576199417209625244140625\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "a=45\n",
    "b=20\n",
    "print(a+b)\n",
    "print(a-b)\n",
    "print(a/b)\n",
    "print(a*b)\n",
    "print(a%b)\n",
    "print(a**b)\n",
    "print(a//b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Simple Interest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The simple interest is 6.00\n"
     ]
    }
   ],
   "source": [
    "p=100\n",
    "t=2\n",
    "r=3\n",
    "si=(p*t*r)/100\n",
    "print('The simple interest is %0.2f'%si)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Area of circle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of circle is91.62\n"
     ]
    }
   ],
   "source": [
    "radius=5.4\n",
    "PI=3.142\n",
    "area=PI*(radius*radius)\n",
    "print('The area of circle is%0.2f'%area)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Area of triangle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the area of the triangle is 14.70\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "b=6\n",
    "c=7\n",
    "s=(a+b+c)/2\n",
    "area=(s*(s-a)*(s-b)*(s-c))**0.5\n",
    "print('the area of the triangle is %0.2f'%area)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Fahrenheit to Celsius"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The answere is:99.50\n"
     ]
    }
   ],
   "source": [
    "celsius=37.5\n",
    "fahrenheit=(celsius*1.8)+32\n",
    "print('The answere is:%0.2f'%fahrenheit)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Celsius to Fahrenheit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The answere is :35.00\n"
     ]
    }
   ],
   "source": [
    "f=95\n",
    "c=(f-32)/1.8\n",
    "print('The answere is :%0.2f'%c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Area of triangle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of rectangle is:3329.73\n"
     ]
    }
   ],
   "source": [
    "lenght=60.26\n",
    "width=55.256\n",
    "area=lenght*width\n",
    "print('The area of rectangle is:%0.2f'%area)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Area of square"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of square is:2012.19\n"
     ]
    }
   ],
   "source": [
    "side1=23.3\n",
    "side2=86.36\n",
    "area=side1*side2\n",
    "print('The area of square is:%0.2f'%area)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Circumference of a circle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The circumference of circle is:40.85\n"
     ]
    }
   ],
   "source": [
    "PI=3.142\n",
    "radius=6.5\n",
    "circumference=2*PI*radius\n",
    "print('The circumference of circle is:%0.2f'%circumference)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Swapping of numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the value of x after swapping is:26\n",
      "the value of y after swapping is:4\n"
     ]
    }
   ],
   "source": [
    "x=4\n",
    "y=26\n",
    "temp=x\n",
    "x=y\n",
    "y=temp\n",
    "print('the value of x after swapping is:{}'.format(x))\n",
    "print('the value of y after swapping is:{}'.format(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
