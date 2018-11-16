#include <stdio.h>
#include <math.h>
#include <string.h>
#include "boolean.h"

#define Fail -9999999
#define MathError -9999998
char *now;

// List perintah
boolean IsDigit(char c);
float charTofloat(char c);
boolean FailedInput(float x);
boolean CanBeInteger(float x);

float checksign();
float digit();
float plusminus();
float timesdiv();
float brackets();
float power();
float executePower(float x);


// Implementasi perintah-perintah

boolean IsDigit(char c)
// Mengembalikan nilai true jika char tersebut adalah digit
{
  return (c >= '0' && c <= '9');
}

float charTofloat(char c)
// Mengganti karkater ke float
{
  return (c - '0');
}

boolean FailedInput(float x)
// Memberikan nilai true jika x adalah Fail
{
  return ((x == Fail) || (x == MathError));
}

boolean CanBeInteger(float x)
// Memberikan nilai true jika x dapat diconvert menjadi integer
{
  return (ceil(x) == x);
}

float checksign()
// Mengecek apakah digit tersebut memiliki nilai negatif, tanda kurung
// atau hanya bilangan biasa saja
{
  float checker;

  if (*now == '-')
  {
    now++;
    if (*now == '(')
    {
      now++;
      checker = brackets();
    }
    else
    {
      checker = digit();
    }
    if (!FailedInput(checker))
    {
      return ((-1) * checker);
    }
    else
    {
      return (checker);
    }
  }
  else if (*now == '(')
  {
    now++;
    return (brackets());
  }
  else
  {
    return (digit());
  }
}

float digit ()
// Menghasilkan digit angka pada bilangan
{
  float temp = 0;
  if (IsDigit(*now))
  {
    while (IsDigit(*now))
    {
      temp = (temp*10) + charTofloat(*now);
      now++;
    }
    if (*now == '.')
    {
      now++;
      float multiplier = 0.1;
      if (!IsDigit(*now))
      {
        return (Fail);
      }
      else
      {
        while (IsDigit(*now))
        {
          temp = temp + charTofloat(*now)*multiplier;
          multiplier /= 10;
          now++;
        }
      }
    }
    return (temp);
  }
  else
  {
    return (Fail);
  }
}

float plusminus ()
// Menghasilkan hasil penjumlahan dan pengurangan
{
  float x = timesdiv();
  if (FailedInput(x))
  {
    return (x);
  }
  else
  {
    while (*now == '+' || *now == '-')
    {
      char opr = *now;
      now++;
      float y = timesdiv();
      if (FailedInput(y))
      {
        return (y);
      }
      if (opr == '+')
      {
        x += y;
      }
      else
      {
        x -= y;
      }
    }
    return x;
  }
}

float timesdiv ()
// Menghasilkan hasil perkalian dan pembagian
{
  float x = power();
  if (FailedInput(x))
  {
    return (x);
  }
  while (*now == '*' || *now == '/')
  {
    char opr = *now;
    now++;
    float y = power();
    if (FailedInput(y))
    {
      return (y);
    }
    if (opr == '*')
    {
      x *= y;
    }
    else
    {
      if (y == 0)
      {
        x = MathError;
        break;
      }
      else
      {
        x /= y;
      }
    }
  }
  return x;
}

float brackets ()
// Menghasilkan hasil dari tanda kurung jika berhasil
{
  float res = plusminus();
  if (*now != ')')
  {
    return Fail;
  }
  else
  {
    now++;
    return res;
  }
}

float power ()
// Mengembalikan hasil perpangkatan dari sebuah bilangan
{
  float x = checksign();
  if (*now == '^' && !FailedInput(x))
  {
    now++;
    x = executePower(x);
  }
  return (x);
}

float executePower (float x)
// Membantu perpangkatan dengan pemanggilan rekursif
{
  float y = checksign();
  if (FailedInput(y))          // Basis
  {
    return (y);
  }
  else if (*now != '^')   // Basis
  {
    if (x == 0 && y <= 0)
    {
      return (MathError);
    }
    else if (x < 0 && !CanBeInteger(y))
    {
      return (MathError);
    }
    else
    {
      return (pow(x,y));
    }
  }
  else                    // Rekurens
  {
    now++;
    float z = executePower(y);
    if (z != Fail)
    {
      return (pow(x,z));
    }
    else
    {
      return (Fail);
    }
  }
}

int main ()
{
  char input[50];
  printf("Masukkan operasi yang ingin dilakukan!\n");
  scanf ("%s", input);
  now = input;

  float count = plusminus();
  if (count == Fail || *now != '\0')
  {
    printf("Syntax error\n");
  }
  else if (count == MathError)
  {
    printf("Math error\n");
  }
  else
  {
    printf("Result = %.2f", count);
  }
  return 0;
}
