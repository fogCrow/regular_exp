123456
# regular_exp
## varity normal regular expression ,save your  brain labor.
   
* so far only support python.

update continuously...

regular_expression about digital :see [reg_digital.py](https://github.com/fogCrow/regular_exp/blob/master/reg_digital.py)

```
#include: positive integer(0 not included) eg: 1 2 3 4
#([1-9][0-9]*)

#include:integer(0 include) 、decimal eg:-1   0     1   2   3   4
#(-?(0|([1-9][0-9]*)))

#include:integer(0 include) 、decimal eg:-1   0     1    0.2    2.3    2.01
#(-?((0|([1-9][0-9]*))(\.[0-9]*[1-9])?))  

#include:integer(0 include) 、decimal、percentage eg:-1   0  0.2/0.3    2.3    2/1  

#(-?((0|([1-9][0-9]*))(\.[0-9]*[1-9])?))(/(-?(0\.[0-9]*[1-9])|([1-9][0-9]*(\.[0-9]*[1-9])?)))?
```

14:04
15:10
