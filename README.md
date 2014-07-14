mapreduce
=========

These python programs demonstrate how MapReduce works.

You can use, `python test.py` for example usage.

The program `splitter.py` is used to simulate hadoop's dispersal of reduce tasks across multiple systems by leveraging multiple processors.

wordcount
---

Word count is the classic MapReduce version of hello world. It just takes and counts the words in a file.
Example usage:

    cat book.txt | python wc_mapper.py | python wc_reducer.py | sort -grk 2 | head -n 50

sum
---

The map reduce pair `sum_mapper.py` and `sum_reducer.py` simply sum large numbers together.
Also, `gen.py` produces random numbers for input to this MR job.
Example usage:

    cat nums.dat | ./sum_mapper.py | ./sum_reducer.py
  
prime
-----

The MR tasks `prime_mapper.py` and `prime_reducer.py` can be used to factor large numbers.
Example usage:

    echo "12938485279" | ./prime_mapper.py | ./prime_reducer.py

more
----

See <a href="http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/">this</a> blog entry for more about
about writing hadoop streaming jobs in python.
