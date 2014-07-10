mapreduce
=========

These python programs demonstrate how MapReduce works.

You can use, `python test.py` for example usage.

The program `splitter.py` is used to simulate hadoop's dispersal of reduce tasks across multiple systems by leveraging multiple processors.

sum
---

The map reduce pair `sum_mapper.py` and `sum_reducer.py` simply sum large numbers together.
Also, `gen.py` produces random numbers for input to this MR job.
Example usage:

    cat nums.dat | python sum_mapper.py | python sum_reducer.py
  
prime
-----

The MR tasks `prime_mapper.py` and `prime_reducer.py` can be used to factor large numbers.
Example usage:

    echo "12938485279" | python prime_mapper.py | python prime_reducer.py
