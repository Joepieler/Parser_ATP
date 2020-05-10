# German - -
The German -- code is based on a mix of German and code. The intention was to learn a little German for the summer and to fulfill the assignment. 

## Key words

| Function| Keyword |
|--|--|
| VARIABLE | can be everything  |
| plus | addiere |
| min | zähle |
| multiply | multiplizieren |
| divide | teilen |
| is | ist |
| if |wenn|
|while | solange|
|end | ende|
|smaler| kleiner|
|same | gleichwie|
|larger |größer|
| print | abdrucken
| printall variable names| alle_variable_drucken|


### if statment
In C++ 

    if (2 > 1){
      std::cout<< 1;
     }
In German - -

    wenn 2 größer 1
    abdrucken 1
    ende

### while loop
In C++ 

	int a = 0
    while(a < 10){
	   a++;
       std::cout<< a;
     }
In German- -
	
    a ist 0
    solange a kleiner 10
    a ist a addiere 1
    abdrucken a
    ende
# How to run

    start_compiling("filename.gmm")

# test code

```
a ist 0
abdrucken 1
wenn 2 größer 1
abdrucken 2
wenn 1 größer 1
abdrucken 3
ende
abdrucken 4
ende
abdrucken 5
abdrucken 6
wenn 1 kleiner 2
abdrucken 7
ende
solange a kleiner 10
a ist a addiere 1
abdrucken a
ende
b ist 10
solange b größer 0
b ist b zähle 1
wenn b kleiner 5
abdrucken b
ende
abdrucken8
ende
alle_variable_drucken
ende
```

Gives as output

```
1
2
4
5
6
7
1
2
3
4
5
6
7
8
9
10
4
3
2
1
0
lines: 
a
b
```
