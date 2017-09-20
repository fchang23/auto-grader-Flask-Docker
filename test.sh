#!/bin/bash
tmpoutput=`echo -e freddy '\n' susan | ./a.out` 

CORRECT=0
f1=`echo $tmpoutput | grep -q 'freddy'` 

if [ $? = 0 ]; then
  let CORRECT=CORRECT+1 
fi

f1=`echo $tmpoutput | grep -q 'susan'` 
if [ $? = 0 ]; then
  let CORRECT=CORRECT+1 
fi

exit $CORRECT
