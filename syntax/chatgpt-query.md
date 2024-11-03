Given the following input form, now you have to write a corresponding C++17 code which can get these standard inputs via cin.
Note that you can only use standard code, not the compiler-dependent code. Note that you also need to explicitly show dependencies, like #include. You are good to assume `using namespace std;`
You are good to use vector std.
For example, when
```
// inputSample: Get single integer
1
```
is given, your code should be

```
// codeSample
#include <iostream>

int num1;
cin >> num1;
```

===================================

```
// inputA: Get two integers in one line
1 2
```

```
// inputB: Given the number of integers n, get n integers in one line
7
1 1 2 3 5 8 13
```

```
// inputC: Given the number of integers n, get n integers in n lines
7
1
1
2
3
5
8
13
```

```
// inputD: Get string without whitespace
aa
```

```
// inputE: Get two space-seperated string (["aa", "bb"])
aa bb
```

```
// inputF: Get one space-containing string ("aa bb")
aa bb
```

```
// inputE: Given integer n, get n space-seperated string (["aa", "bb", "cc", "dd"])
4
aa bb cc dd
```

```
// inputF: Get multiple space-containing string (["aa bb", "ccc dd", "eeeeee ff"])
aa bb
ccc dd
eeeeee ff
```