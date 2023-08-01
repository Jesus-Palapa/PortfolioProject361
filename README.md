## PortfolioProject361
//PokeFax: A Pokemon Dictionary
//Name: Jesus Palapa
//Course: CS 361
//Email: palapacj@oregonstate.edu

**Description:** This program will allow new and old Pokemon fans to search their favorite pokemon by name and get pokemon data such as - type, number, name, weight, height, moves.
The user can also see lists of pokemon and save their favorite pokemon.

**Communication Contract:** Communication will be done throguh sockets with port number 1800 and host IP of '127.0.0.1' between my program file and the microservice my partner has established.
A connection betweem the microservice and program will be established. The program will send a pokemon name using sockets and the microservice will return pokemon data. For example, a user will use send() method to send a pokemon name "pikachu". The microservice will process the name and gather the pokemon's type, number, name, weight, height, moves.This information will be sent back to the program and be received using the recv() method.


**UML Sequence Diagram**



[UML Sequence Diagram.pdf](https://github.com/Jesus-Palapa/PortfolioProject361/files/12224798/UML.Sequence.Diagram.pdf)

<img width="517" alt="Screenshot 2023-07-31 at 10 02 54 PM" src="https://github.com/Jesus-Palapa/PortfolioProject361/assets/114314987/21f33192-871e-4540-b030-805bda288124">






Using API PYPOKEDEX
//MIT License

Copyright (c) 2018-2023 Arnav Borborah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
